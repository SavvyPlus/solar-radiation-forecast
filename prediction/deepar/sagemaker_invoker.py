"""Invoke SageMaker runtime from outside
"""
import json
import random

import boto3
import sagemaker

# init sagemaker
SAGEMAKER_SESSION = sagemaker.Session()


# TODO: import endpoint_name from somewhere else e.g. config file
ENDPOINT_NAME = ''

PREDICTOR = sagemaker.predictor.RealTimePredictor(
    ENDPOINT_NAME,
    sagemaker_session=SAGEMAKER_SESSION,
    content_type="application/json")


# TODO: import endpoint_name from somewhere else e.g. config file
Q1 = '0.2'
Q2 = '0.9'
NUM_SAMPLES = 100


def build_request_data(start, target, cat, quantiles,
                       num_samples, output_types):
    """
    Build DeepAR JSON tequest formats.
    https://docs.aws.amazon.com/sagemaker/latest/dg/deepar-in-formats.html

    Parameters
    ----------
    start : str
        Timestamp for starting time of historical data.
    target : list
        Historical data values.
    cat : list
        An array of categorical features that can be
        used to encode the groups that the record belongs to.
    quantiles : list
        The quantile values is returned as a time series.
    num_samples : int
        Number of sample paths that the model generates
        to estimate the mean and quantiles.
    output_types : list
        Valid values are "mean" "quantiles" and "samples".

    Returns
    -------
    request_data : JSON

    """
    serie = {'start': start, 'target': target}
    if len(cat) > 0:
        serie['cat'] = cat
    series = [serie]

    configuration = {
        'output_types': output_types,
        'num_samples': num_samples,
        'quantiles': quantiles
    }
    http_data = {
        "instances": series,
        "configuration": configuration
    }
    request_data = json.dumps(http_data)
    return request_data


def get_predicted_series(result, num_samples, q1, q2):
    """
    Parse result from DeepAR JSON response.
    https://docs.aws.amazon.com/sagemaker/latest/dg/deepar-in-formats.html

    Parameters
    ----------
    result : dictionary
        Response from DeepAR.
    num_samples : int
        Number of sample paths that the model generates
        to estimate the mean and quantiles.
    q1 : string
        Lower quantile.
    q2 : string
        Upper quantile.

    Returns
    -------
    results : dict

    """
    json_result = json.loads(result)
    y_data      = json_result['predictions'][0]
    y_mean      = y_data['mean']
    y_q1        = y_data['quantiles'][q1]
    y_q2        = y_data['quantiles'][q2]
    y_sample    = y_data['samples'][random.randint(0, num_samples)]

    results = {
        'y_mean': y_mean,
        'y_q1': y_q1,
        'y_q2': y_q2,
        'y_sample': y_sample
    }
    return results


def predict_single_timeseries(start, target, cat=[],
                              quantiles=[Q1, Q2],
                              num_samples=NUM_SAMPLES,
                              output_types=["mean", "quantiles", "samples"]):
    """Root function to make predict.

    Parameters
    ----------
    start : str
        Timestamp for starting time of historical data.
    target : list
        Historical data values.
    cat : list
        An array of categorical features that can be
        used to encode the groups that the record belongs to.
    quantiles : list
        The quantile values is returned as a time series.
    num_samples : int
        Number of sample paths that the model generates
        to estimate the mean and quantiles.
    output_types : list
        Valid values are "mean" "quantiles" and "samples".

    Returns
    -------
    predicted_data : dict

    """
    request_data = build_request_data(start, target, cat, quantiles,
                                      num_samples, output_types)
    predicted_response = PREDICTOR.predict(request_data).decode('utf-8')
    predicted_data = get_predicted_series(predicted_response, num_samples,
                                          quantiles[0], quantiles[1])
    return predicted_data
