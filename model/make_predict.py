# Deploy model

%%time

job_name = estimator.latest_training_job.name

endpoint_name = sagemaker_session.endpoint_from_job(
    job_name=job_name,
    initial_instance_count=1,
    instance_type='ml.t2.medium',
    deployment_image=image_name,
    role=role
)

predictor = sagemaker.predictor.RealTimePredictor(
    endpoint_name,
    sagemaker_session=sagemaker_session,
    content_type="application/json")



def build_prediction_data(start, target, cat, num_samples=100, q1='0.2', q2='0.9'):
    s = {"start": start, "target": target, "cat": cat}
    series = []
    series.append(s)
    configuration = {
        "output_types": ["mean", "quantiles", "samples"],
        "num_samples": num_samples,
        "quantiles": [q1, q2]
    }
    http_data = {
        "instances": series,
        "configuration": configuration
    }
    return json.dumps(http_data)

# Get predicted series from response
def get_predicted_series(result, q1='0.2', q2='0.9'):
    import random
    json_result = json.loads(result)
    y_data      = json_result['predictions'][0]
    y_mean      = y_data['mean']
    y_q1        = y_data['quantiles'][q1]
    y_q2        = y_data['quantiles'][q2]
    y_sample    = y_data['samples'][random.randint(0, num_samples)]

    #print("Mean: %s\n" % y_mean)
    #print("Quartile %s: %s\n" % (q1, y_q1))
    #print("Quartile %s: %s\n" % (q2, y_q2))
    return y_mean, y_q1, y_q2, y_sample

# Plot predicted series and ground truth

def plot_series(result, truth=False, truth_data=None, truth_label=None, q1='0.2', q2='0.9'):
    x = range(0,prediction_length)
    y_mean, y_q1, y_q2, y_sample = get_predicted_series(result)
    plt.gcf().clear()
    mean_label,   = plt.plot(x, y_mean, label='mean')
    q1_label,     = plt.plot(x, y_q1, label=q1)
    q2_label,     = plt.plot(x, y_q2, label=q2)
    sample_label, = plt.plot(x, y_sample, label='sample')

    if truth:
        ground_truth, = plt.plot(x, truth_data, label=truth_label)
        plt.legend(handles=[ground_truth, q2_label, mean_label, q1_label, sample_label])
    else:
        plt.legend(handles=[q2_label, mean_label, q1_label, sample_label])
    plt.yticks(np.arange(5.0, 12.0, 0.5))
    plt.show()


q1 = '0.2'         # compute p20 quantile
q2 = '0.9'         # compute p90 quantile
num_samples = 100  # predict 100 sample series


data = get_data_to_forecast(test_key)

historical_length = prediction_length*2

truth_data = data['target'][-prediction_length:]
historical_data = data['target'][-historical_length:-prediction_length]
cat = data['cat']
historical_start = ts_indexes[-(prediction_length*2)]

prediction_data = build_prediction_data(historical_start, historical_data, cat,
                                        num_samples=num_samples, q1=q1, q2=q2)

result = predictor.predict(prediction_data).decode('utf-8')

plot_series(result,
           truth=True,
           truth_data=truth_data,
           truth_label='truth',
           iq1=iq1,
           iq2=iq2)
