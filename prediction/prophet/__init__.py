"""
"""
import pandas as pd
from fbprophet import Prophet

from prediction import BasePrediction


class ProphetPrediction(BasePrediction):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.periods = kwargs.get('periods', 12)
        self.freq = kwargs.get('freq', 'M')
        # TODO: ignore for make_predict func or check value here
        # if self.freq not in [None, 'M']:
        #     raise ValueError('Only None or M is allowed for Prophet frequency')


    def create_dataframe(self):
        """
        The input to Prophet is always a dataframe with two columns: ds and y.
        The ds (datestamp) column should be of a format expected by Pandas,
        ideally YYYY-MM-DD for a date or YYYY-MM-DD HH:MM:SS for a timestamp.
        The y column must be numeric, and represents the measurement we wish to forecast.
        https://facebook.github.io/prophet/docs/quick_start.html#python-api

        Parameters
        ----------
        ds : list
            List of timestamps.
        y : list
            List of numeric numbers.

        Returns
        -------
        df : DataFrame
            Input DataFrame for Prophet.

        """
        data = {
            'ds': self.ts_values,
            'y': self.y_values
        }
        df = pd.DataFrame(data=data)
        return df


    def make_predict(self):
        df = self.create_dataframe()
        m = Prophet(changepoint_prior_scale=0.5)
        m.fit(df)
        if self.freq == 'M':
            future = m.make_future_dataframe(periods=self.periods, freq='M')
        else:
            future = m.make_future_dataframe(periods=self.periods)
        forecast = m.predict(future)
        predicted_data = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(self.periods)

        results = {
            'ds': [str(ds) for ds in list(predicted_data['ds'])],
            'y_mean': list(predicted_data['yhat']),
            'y_q1': list(predicted_data['yhat_lower']),
            'y_q2': list(predicted_data['yhat_upper']),
        }
        return results
