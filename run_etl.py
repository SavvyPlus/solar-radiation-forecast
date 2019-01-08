from etl import create_query, transform

# create_query.create_sql_scripts('./etl/get_data.sql')
# transform.split_radiationtype('./data/raw')

dni_ghi_raw = ['./data/dni/raw', './data/ghi/raw']
for path in dni_ghi_raw:
    transform.convert_to_timeseries(path)
