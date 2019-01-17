import boto3
import s3fs
import sagemaker
from sagemaker import get_execution_role


# config S3
bucket = 'solar-radiation-forecast'
prefix = 'sagemaker/deepar-monthly-solar-radiation'

train_prefix   = '{}/{}'.format(prefix, 'train')
test_prefix    = '{}/{}'.format(prefix, 'test')
output_prefix  = '{}/{}'.format(prefix, 'output')

train_key = 'train.json'
test_key = 'test.json'

# init sagemaker
sagemaker_session = sagemaker.Session()
role = get_execution_role()
region = boto3.Session().region_name


train_path  = sagemaker_session.upload_data(train_key, bucket=bucket, key_prefix=train_prefix)
test_path   = sagemaker_session.upload_data(test_key,  bucket=bucket, key_prefix=test_prefix)
output_path = 's3://{}/{}'.format(bucket, output_prefix)



# we configure the container image to be used for the region that we are running in
from sagemaker.amazon.amazon_estimator import get_image_uri
image_name = get_image_uri(boto3.Session().region_name, 'forecasting-deepar')

freq = 'M'
prediction_length = 24
context_length = 36

# Train a model
estimator = sagemaker.estimator.Estimator(
    sagemaker_session=sagemaker_session,
    image_name=image_name,
    role=role,
    train_instance_count=1,
    train_instance_type='ml.m5.large',
    base_job_name='POC-deepar-solar-forecast-model',
    output_path=output_path
)

# https://docs.aws.amazon.com/sagemaker/latest/dg/deepar_hyperparameters.html

hyperparameters = {
    "time_freq": freq, # monthly series
    # "context_length": str(prediction_length),
    "prediction_length": str(prediction_length), # number of data points to predict
    # "num_cells": "40",
    # "num_layers": "2",
    "likelihood": "gaussian",
    # "epochs": "250",
    # "mini_batch_size": "32",
    # "learning_rate": "0.00001",
    # "dropout_rate": "0.05",
    "early_stopping_patience": "40" # stop if loss hasn't improved in 10 epochs
}

estimator.set_hyperparameters(**hyperparameters)


from sagemaker.tuner import HyperparameterTuner, IntegerParameter, CategoricalParameter, ContinuousParameter

# hyperparameter_ranges = {'optimizer': CategoricalParameter(['sgd', 'Adam']),
#                          'learning_rate': ContinuousParameter(0.01, 0.2),
#                          'num_epoch': IntegerParameter(10, 50)}

hyperparameter_ranges = {
    'mini_batch_size': IntegerParameter(32, 800),
    'epochs': IntegerParameter(1, 800),
    'context_length': IntegerParameter(prediction_length, 100),
    'num_cells': IntegerParameter(30, 200),
    'num_layers': IntegerParameter(1, 8),
    'dropout_rate': ContinuousParameter(0.00, 0.2),
    'embedding_dimension': IntegerParameter(1, 50),
    'learning_rate': ContinuousParameter(1e-5, 1e-1)
}


objective_metric_name = 'test:RMSE'
metric_definitions = [{
   "Name": "test:RMSE",
   "Regex": ".*\\[[0-9]+\\].*#011test:RMSE:(\\S+)"
}]


tuner = HyperparameterTuner(estimator,
                            objective_metric_name,
                            hyperparameter_ranges,
                            metric_definitions,
                            max_jobs=20,
                            max_parallel_jobs=3)

data_channels = {"train": train_path, "test": test_path}

%%time
tuner.fit(inputs=data_channels)
