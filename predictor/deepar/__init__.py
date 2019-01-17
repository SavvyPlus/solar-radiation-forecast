from .sagemaker_invoker import predict_single_timeseries

from predictor import BasePredictor



# TODO: import endpoint_name from somewhere else e.g. config file
Q1 = '0.2'
Q2 = '0.9'
NUM_SAMPLES = 100
OUTPUT_TYPES = ["mean", "quantiles", "samples"]


class DeepARPredictor(BasePredictor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)

        try:
            self.cat = kwargs['cat']
        except KeyError:
            raise ValueError('cat is requied for DeepARPrediction class')

        self.quantiles = kwargs.get('quantiles', [Q1, Q2])
        self.num_samples = kwargs.get('num_samples', NUM_SAMPLES)
        self.output_types = kwargs.get('output_types', OUTPUT_TYPES)

    def make_predict(self):
        results = predict_single_timeseries(self.ts_values[0], self.y_values,
                                            self.cat, self.quantiles,
                                            self.num_samples, self.output_types)
        return results
