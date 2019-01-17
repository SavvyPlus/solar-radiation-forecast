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
        resutls = self.predictor.make_predict()
        return resutls


def create_predictor(predictor_type, *args, **kwargs):
    from . import deepar
    from . import prophet

    MAP_PREDICTOR = {
        'deepar': deepar.DeepARPredictor,
        'prophet': prophet.ProphetPredictor
    }

    try:
        predictor_cls = MAP_PREDICTOR[predictor_type]
        predictor_obj = PredictorFactory(predictor_cls, *args, **kwargs)
        return predictor_obj
    except KeyError:
        raise ValueError('Only suport deepar and prophet predictor')
