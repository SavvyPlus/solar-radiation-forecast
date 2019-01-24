from collections import Counter
import numpy as np
import pandas as pd


def get_night_patterns(df, index_col='date', val_col='radiation', limit=17520):
    """
    Based on historical data we get hours have zero radiation in each month.

    Parameters
    ----------
    df : DataFrame
        DataFrame of solar radiation historical data.
    index_col : str, default 'date'
        Name of timestamp column used to index.
    val_col : str, default 'radiation'
        Name of radiation column.
    limit : int, default 17520
        Maximum historical data to get patterns.

    Returns
    -------
    patterns : dict
        Ex: {'month': [hours have 0 value]}

    """

    patterns = {}

    # pre-process df
    df = df.set_index(pd.DatetimeIndex(df[index_col]))
    df = df.drop(columns=[index_col])

    df = df.tail(limit)
    df= df[df[val_col]==0]
    group_months = df.groupby(by=[df.index.month])
    df_mos = [group_months.get_group(g) for g in group_months.groups]
    # del df

    for df_mo in df_mos:
        years = sorted(set(df_mo.index.year), reverse=True)
        hours = None
        for year in years:
            if len(df_mo[df_mo.index.year==year]) < 300:
                continue
            hours = list(df_mo[df_mo.index.year==year].index.hour)
            break
        if not hours:
            hours = list(df_mo[df_mo.index.year==years[0]].index.hour)

        month = df_mo.index.month[0]
        patterns[month] = normalize_night_pattern(hours)

    return patterns


def normalize_night_pattern(pattern):
    """
    Due to missing data or incorrect data some hours may have zero
    radiation value. We only get common hours in a month which means hours
    appear less than 50 percentile will be removed.

    Parameters
    ----------
    pattern : list
        List of hours. Ex [0, 0, ..., 0, 1, 1, 1, ..., 8] 8 will be removed

    Returns
    -------
    valid_values : list
        List of hours should have zero value.

    """
    counter = dict(Counter(pattern))
    counter_values = np.array(list(counter.values()))
    valid_point = np.percentile(counter_values, 50)
    valid_values = [key for key in counter.keys()
                    if counter[key] >= valid_point]
    return valid_values



def fill_night_value(df, night_patterns, index_col='ds', value=0):
    """Update predicted night value by other value.

    Parameters
    ----------
    df : DataFrame
        DataFrame of predicted data need to change night time to zero.
    night_patterns : dict
        Result from `get_night_patterns()` function.
    index_col : str, default 'ds'
        Name of timestamp column used to index.
    value : int, default 0
        Replace predicted night value by this value

    Returns
    -------
    df: DataFrame
        DataFrame of predicted data with update night values.

    """
    # pre-process df
    indexes = df[index_col]
    df = df.set_index(pd.DatetimeIndex(df[index_col]))
    df = df.drop(columns=[index_col])

    for month in night_patterns.keys():
        df[(df.index.month==month) &
           (df.index.hour.isin(night_patterns[month]))] = value
    df.reset_index(inplace=True)
    return df


def replace_negative_values(df, val_col, threshold=0, replaced_value=0):
    df[df[val_col]<threshold] = replaced_value
    return df
