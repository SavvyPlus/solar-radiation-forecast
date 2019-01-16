from sagemaker_invoker import predict_single_timeseries

from prediction import BasePrediction


# TODO: import endpoint_name from somewhere else e.g. config file
Q1 = '0.2'
Q2 = '0.9'
NUM_SAMPLES = 100
OUTPUT_TYPES = ["mean", "quantiles", "samples"]


class DeepARPrediction(BasePrediction):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.cat = kwargs.get('cat', [])
        self.quantiles = kwargs.get('quantiles', [Q1, Q2])
        self.num_samples = kwargs.get('num_samples', NUM_SAMPLES)
        self.output_types = kwargs.get('output_types', OUTPUT_TYPES)
