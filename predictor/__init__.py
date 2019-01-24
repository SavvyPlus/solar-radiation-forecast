"""
"""
from abc import ABC, abstractmethod


class BasePredictor(ABC):
    def __init__(self, ts_values, y_values, **kwargs):
        self.ts_values = ts_values
        self.y_values = y_values

    @abstractmethod
    def make_predict(self):
        pass


class PredictorFactory(object):
    def __init__(self, predictor_cls, *args, **kwargs):
        self.predictor = predictor_cls(*args, **kwargs)

    def predict(self):
        """
        Example results
        ----------
        >>>
        results = {
            'y_mean': [...],
            'y_q1': [...],
            'y_q2': [...],
            'y_sample': [...]
        }
        `y_sample` only available for DeepAR
        """
        resutls = self.predictor.make_predict()
        return resutls


def create_predictor(predictor_type, ts_values, y_values, **kwargs):
    """
    Create predictor project based on predictor_type.

    Parameters
    ----------
    predictor_type : str, valid values are `deepar` and `prophet`
        Type of model to make predict.
    ts_values : list
        List of historical timestamps.
    y_values : list
        List of historical data.

    Keyword parameters:
    ----------
    periods : int, default 12
        How many periods we want to predict.
        Only for Prophet model, will be ignored if `predictor_type='deepar'`.
    freq : str, default 'M'
        Frequency we want to predict.
        Only for Prophet model, will be ignored if `predictor_type='deepar'`.
    cat : list, requied
        List of categories which the time seire belongs to
    quantiles : list, default [0.2, 0.9]
        https://docs.aws.amazon.com/sagemaker/latest/dg/deepar-in-formats.html
    output_types : list, default ["mean", "quantiles", "samples"]
        https://docs.aws.amazon.com/sagemaker/latest/dg/deepar-in-formats.html

    Returns
    -------
    predictor_obj : object
        Predictor object, call it's function `predict` to get predicted results.

    """
    from . import deepar
    from . import prophet

    MAP_PREDICTOR = {
        'deepar': deepar.DeepARPredictor,
        'prophet': prophet.ProphetPredictor
    }

    try:
        predictor_cls = MAP_PREDICTOR[predictor_type]
        predictor_obj = PredictorFactory(predictor_cls, ts_values, y_values, **kwargs)
        return predictor_obj
    except KeyError:
        raise ValueError('Only suport deepar and prophet predictor')
