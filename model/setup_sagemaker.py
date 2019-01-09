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

train_key = ''
test_key = ''

train_path  = sagemaker_session.upload_data(train_key, bucket=bucket, key_prefix=train_prefix)
test_path   = sagemaker_session.upload_data(test_key,  bucket=bucket, key_prefix=test_prefix)
output_path = 's3://{}/{}'.format(bucket, output_prefix)



# init sagemaker
sagemaker_session = sagemaker.Session()
role = get_execution_role()
region = boto3.Session().region_name

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
    "time_freq": freq, # daily series
    "context_length": str(prediction_length),
    "prediction_length": str(prediction_length), # number of data points to predict
    "num_cells": "40",
    "num_layers": "2",
    "likelihood": "gaussian",
    "epochs": "250",
    "mini_batch_size": "32",
    "learning_rate": "0.00001",
    "dropout_rate": "0.05",
    "early_stopping_patience": "10" # stop if loss hasn't improved in 10 epochs
}

estimator.set_hyperparameters(**hyperparameters)


# Run training job
print(train_path)
print(test_path)
print(output_path)

data_channels = {"train": train_path, "test": test_path}

%%time
estimator.fit(inputs=data_channels)
