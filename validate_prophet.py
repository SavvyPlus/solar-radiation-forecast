import sys
import logging

log_format = "%(asctime)s:%(levelname)s:%(name)s:%(lineno)d:%(funcName)s:%(message)s"

logging.basicConfig(level=logging.INFO, format=log_format)
logger = logging.getLogger(__name__)


import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

from prediction import prophet

from utils import files

PREDICTION_LENGTH = 24

ts_paths = [
    {'path': './data/dni/ts', 'radiationtype': 'dni'},
    {'path': './data/ghi/ts', 'radiationtype': 'ghi'}
]

import numpy as np
from matplotlib import pyplot as plt

def plot_series(op, yhat, yhat_lower, yhat_upper, truth=False,
                truth_data=None, truth_label='Truth', prediction_length=24):
    x = range(0, PREDICTION_LENGTH)
    plt.gcf().clear()
    mean_label,   = plt.plot(x, yhat, label='mean')
    q1_label,     = plt.plot(x, yhat_lower, label='yhat_lower')
    q2_label,     = plt.plot(x, yhat_upper, label='yhat_upper')

    if truth:
        ground_truth, = plt.plot(x, truth_data, label=truth_label)
        plt.legend(handles=[ground_truth, q2_label, mean_label, q1_label])
    else:
        plt.legend(handles=[q2_label, mean_label, q1_label])
    plt.yticks(np.arange(5.0, 12.0, 0.5))
    plt.savefig(op)

# with open('./prediction/prophet/validation.txt', 'w') as f:
counter = 1
for ts_info in ts_paths:
    ts_files = files.get_files_in_directory(ts_info['path'], '*.csv')
    for ts_file in ts_files:
        df = pd.read_csv(ts_file)
        truth_values = list(df.tail(PREDICTION_LENGTH)['radiation'])
        # create train data
        df = df[:len(df)-PREDICTION_LENGTH]
        ds_values = list(df['ts'])
        y_values = list(df['radiation'])
        p = prophet.ProphetPrediction(ds_values, y_values, periods=24)
        results = p.make_predict()
        op = './data/output/prophet/charts_scale/{}.png'.format(counter)
        plot_series(op, results['y_mean'], results['y_q1'], results['y_q2'],
                    truth=True, truth_data=truth_values)

        # f.write('Results for test case {}\n'.format(counter))
        #
        # mse_mean = mean_squared_error(truth_values, results['y_mean'])
        # f.write('MSE yhat: {}\n'.format(mse_mean))
        # mse_q1 = mean_squared_error(truth_values, results['y_q1'])
        # f.write('MSE yhat_lower: {}\n'.format(mse_q1))
        # mse_q2 = mean_squared_error(truth_values, results['y_q2'])
        # f.write('MSE yhat_upper: {}\n'.format(mse_q2))
        #
        # f.write('\n--\n\n')
        #
        # mae_mean = mean_absolute_error(truth_values, results['y_mean'])
        # f.write('MAE yhat: {}\n'.format(mae_mean))
        # mae_q1 = mean_absolute_error(truth_values, results['y_q1'])
        # f.write('MAE yhat_lower: {}\n'.format(mae_q1))
        # mae_q2 = mean_absolute_error(truth_values, results['y_q2'])
        # f.write('MAE yhat_upper: {}\n'.format(mae_q2))
        #
        # f.write('\n--\n\n')
        #
        # r2_mean = r2_score(truth_values, results['y_mean'])
        # f.write('r2_score yhat: {}\n'.format(r2_mean))
        # r2_q1 = r2_score(truth_values, results['y_q1'])
        # f.write('r2_score yhat_lower: {}\n'.format(r2_q1))
        # r2_q2 = r2_score(truth_values, results['y_q2'])
        # f.write('r2_score yhat_upper: {}\n'.format(r2_q2))
        #
        #
        # f.write('\n--------------------------------\n\n')

        counter+=1
