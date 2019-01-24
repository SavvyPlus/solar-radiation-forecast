import pandas as pd


def transform_to_daily(file_path, parrent_folder='filled'):
    full_daily_path = file_path.replace(parrent_folder, 'full_daily')
    four_years_daily_path = file_path.replace(parrent_folder, 'four_years_daily')

    df = pd.read_csv(file_path, parse_dates=True, index_col=0)
    # remove last data only has one hour
    df = df[:len(df)-1]
    df = df.resample('D').sum()
    # save full daily
    df.to_csv(path_or_buf=full_daily_path, index_label='date')
    # save four years daily
    df.tail(1500).to_csv(path_or_buf=four_years_daily_path, index_label='date')
