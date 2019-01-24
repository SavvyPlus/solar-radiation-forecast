import math
import json
import glob

import numpy as np


def write_dicts_to_file(path, data):
    """Write list of dicts to file.

    Args:
        path (string): where file is saved.
        data (list): list of dicts.

    Returns:
        type: None.

    """
    with open(path, 'wb') as fp:
        for d in data:
            fp.write(json.dumps(d).encode("utf-8"))
            fp.write("\n".encode('utf-8'))


def get_files_in_directory(path, pattern="*.csv"):
    """Retun a list of files name in a directory
    with pattern. Eg: "*.* for all
    Args:
        path (string): path to the directory
        pattern (string): Eg: "*.* for all, ".*" for zip files
    """
    return glob.glob(path+"/"+pattern)


def series_to_obj(ts, cat=None):
    def handle_na(value):
        if math.isnan(value):
            return None
        return value
    ts_list = list(ts)
    ts_list = [handle_na(value) for value in ts_list]

    obj = {"start": str(ts.index[0]), "target": ts_list}
    if cat is not None:
        obj["cat"] = cat
    return obj

def series_to_jsonline(ts, cat=None):
    return json.dumps(series_to_obj(ts, cat))
