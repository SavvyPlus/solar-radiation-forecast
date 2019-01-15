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


def plot_series(yhat, yhat_lower, yhat_upper, truth=False, truth_data=None, truth_label='Truth', prediction_length=24):
    x = range(0,prediction_length)
    plt.gcf().clear()
    mean_label,   = plt.plot(x, y_mean, label='mean')
    q1_label,     = plt.plot(x, y_q1, label='yhat_lower')
    q2_label,     = plt.plot(x, y_q2, label='yhat_upper')

    if truth:
        ground_truth, = plt.plot(x, truth_data, label=truth_label)
        plt.legend(handles=[ground_truth, q2_label, mean_label, q1_label])
    else:
        plt.legend(handles=[q2_label, mean_label, q1_label])
    plt.yticks(np.arange(5.0, 12.0, 0.5))
    plt.show()
