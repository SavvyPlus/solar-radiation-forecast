from collections import Counter
import numpy as np
import pandas as pd


def get_night_patterns(df, index_col='date', val_col='radiation', limit=17520):
    """Short summary.

    Parameters
    ----------
    df : type
        Description of parameter `df`.
    limit : type
        Description of parameter `limit`.

    Returns
    -------
    type
        Description of returned object.

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
    """Short summary.

    Parameters
    ----------
    pattern : type
        Description of parameter `pattern`.

    Returns
    -------
    type
        Description of returned object.

    """
    counter = dict(Counter(pattern))
    counter_values = np.array(list(counter.values()))
    valid_point = np.percentile(counter_values, 50)
    valid_values = [key for key in counter.keys()
                    if counter[key] >= valid_point]
    return valid_values



def fill_night_value(df, night_patterns, index_col='ds', value=0):
    """Short summary.

    Parameters
    ----------
    df : type
        Description of parameter `df`.
    value : type
        Description of parameter `value`.

    Returns
    -------
    type
        Description of returned object.

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



# df = pd.read_csv('../../big_data/full/dni/filled/14.1.csv')
# night_patterns = get_night_patterns(df, index_col='date', val_col='radiation', limit=17520)
#
# df = fill_night_value(df, night_patterns, index_col='date', value=22222)
# print(df.head(100))
