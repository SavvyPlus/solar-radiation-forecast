import config
import pandas as pd

from utils import files
from . import helpers


def split_radiationtype(raw_path):
    raw_files = files.get_files_in_directory(raw_path, "*.csv")
    for raw_file in raw_files:
        df = pd.read_csv(raw_file)
        ghi = df['radiationtype'] == 'ghi'
        dni = df['radiationtype'] == 'dni'
        ghi_path = raw_file.replace('raw', 'ghi')
        dni_path = raw_file.replace('raw', 'dni')
        df[ghi].sort_values(by=['year', 'month']).to_csv(path_or_buf=ghi_path, index=False)
        df[dni].sort_values(by=['year', 'month']).to_csv(path_or_buf=dni_path, index=False)


def convert_to_timeseries(raw_path):
    date_rng = pd.date_range(start='1/1/2008', end='31/08/2018', freq='m')
    raw_files = files.get_files_in_directory(raw_path, "*.csv")
    for raw_file in raw_files:
        df = pd.read_csv(raw_file)
        df = df.set_index(date_rng)
        df = df[:-1]
        df = df.drop(['year', 'month', 'radiationtype'], axis=1)
        ts_path = raw_file.replace('raw', 'ts')
        df.to_csv(path_or_buf=ts_path, index_label='ts')


def create_json_files(ts_list, final_path='./data/final', encoding="utf-8"):
    train = []
    test = []

    for ts_info in ts_list:
        ts_files = files.get_files_in_directory(ts_info['path'], '*.csv')
        for ts_file in ts_files:
            cat = helpers.categorize_from_filename(ts_file.split('/')[-1], ts_info['radiationtype'])
            ts = pd.read_csv(ts_file, header=0, index_col=0, parse_dates=True, squeeze=True)
            train.append(files.series_to_jsonline(ts[:-config.PREDICTION_LENGTH], cat))
            test.append(files.series_to_jsonline(ts, cat))

    with open(final_path + '/train.json', 'wb') as fp:
        for tr in train:
            fp.write(tr.encode(encoding))
            fp.write('\n'.encode(encoding))

    with open(final_path + '/test.json', 'wb') as fp:
        for tr in train:
            fp.write(tr.encode(encoding))
            fp.write('\n'.encode(encoding))
