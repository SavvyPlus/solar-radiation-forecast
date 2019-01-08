import pandas as pd

from utils import files


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
