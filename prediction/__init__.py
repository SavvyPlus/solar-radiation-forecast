"""
"""
from abc import ABC, abstractmethod


class BasePrediction(ABC):
    def __init__(self, ts_values, y_values, **kwargs):
        self.ts_values = ts_values
        self.y_values = y_values


    @abstractmethod
    def make_predict(self):
        pass
