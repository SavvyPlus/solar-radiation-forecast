from etl import create_query, transform

# create_query.create_sql_scripts('./etl/get_data.sql')
# transform.split_radiationtype('./data/raw')

# dni_ghi_raw = ['./data/dni/raw', './data/ghi/raw']
# for path in dni_ghi_raw:
#     transform.convert_to_timeseries(path)

ts_paths = [
    {'path': './data/dni/ts', 'radiationtype': 'dni'},
    {'path': './data/ghi/ts', 'radiationtype': 'ghi'}
]

transform.create_json_files(ts_paths)
