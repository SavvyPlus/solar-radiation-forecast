import config
import pandas as pd
import arrow

from utils import files
from . import helpers


def split_radiationtype(raw_path):
    raw_files = files.get_files_in_directory(raw_path, "*.csv")
    for raw_file in raw_files:
        df = pd.read_csv(raw_file)
        ghi_indexs = df['radiationtype'] == 'ghi'
        dni_indexs = df['radiationtype'] == 'dni'
        ghi_path = raw_file.replace('raw', 'ghi')
        dni_path = raw_file.replace('raw', 'dni')
        df[ghi_indexs].to_csv(path_or_buf=ghi_path, index=False, columns=['date', 'radiation'])
        df[dni_indexs].to_csv(path_or_buf=dni_path, index=False, columns=['date', 'radiation'])


def fill_missing_data(file_path):
    df = pd.read_csv(file_path, parse_dates=True, index_col=0)
    df.sort_index(inplace=True)
    for i in df[df['radiation']<0].index:
        arw = arrow.get(i)
        others_data = []
        shift = 1
        while True:
            previous_time = str(arw.shift(hours=-shift))
            try:
                previous_value = df.loc[previous_time, 'radiation']
                if previous_value >= 0:
                    others_data.append(previous_value)
            except KeyError:
                pass

            next_time = str(arw.shift(hours=+shift))
            try:
                next_value = df.loc[next_time, 'radiation']
                if next_value >= 0:
                    others_data.append(next_value)
            except KeyError:
                pass

            if len(others_data) > 0:
                break
            shift+=1
        df.loc[i, 'radiation'] = sum(others_data)/len(others_data)

    filled_path = file_path.replace('raw', 'filled')
    df.to_csv(path_or_buf=filled_path, index_label='date')
