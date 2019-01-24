# from etl import create_query, transform, full_transform

# create_query.create_sql_scripts('./etl/get_data_hourly.sql', format_query=create_query.FORMAT_QUERY_MONTHLY)
# transform.split_radiationtype('./data/raw')
# full_transform.split_radiationtype('./data/full/raw')
# from utils import files
#
#
#
# full_dni_ghi_raw = ['./data/full/dni/raw', './data/full/ghi/raw']
# for path in full_dni_ghi_raw:
#     raw_files = files.get_files_in_directory(path, "*.csv")
#     for raw_file in raw_files:
#         full_transform.fill_missing_data(raw_file)


# ts_paths = [
#     {'path': './data/dni/ts', 'radiationtype': 'dni'},
#     {'path': './data/ghi/ts', 'radiationtype': 'ghi'}
# ]
#
# transform.create_json_files(ts_paths)
import pandas as pd
from utils import files
from etl import helpers

def create_json_files(ts_list, prediction_length, final_path='./data/full/json', encoding="utf-8"):
    train = []
    test = []

    for ts_info in ts_list:
        ts_files = files.get_files_in_directory(ts_info['path'], '*.csv')
        for ts_file in ts_files:
            cat = helpers.categorize_from_filename(ts_file.split('/')[-1], ts_info['radiationtype'])
            ts = pd.read_csv(ts_file, header=0, index_col=0, parse_dates=True, squeeze=True)
            train.append(files.series_to_jsonline(ts[:-prediction_length], cat))
            test.append(files.series_to_jsonline(ts, cat))

    with open(final_path + '/train_four_years_daily.json', 'wb') as fp:
        for tr in train:
            fp.write(tr.encode(encoding))
            fp.write('\n'.encode(encoding))

    with open(final_path + '/test_four_years_daily.json', 'wb') as fp:
        for tr in test:
            fp.write(tr.encode(encoding))
            fp.write('\n'.encode(encoding))

nan_paths = [
    {'path': './data/full/dni/four_years_daily', 'radiationtype': 'dni'},
    {'path': './data/full/ghi/four_years_daily', 'radiationtype': 'ghi'}
]

create_json_files(nan_paths, 365, final_path='./data/full/json/four_years_daily', encoding="utf-8")
