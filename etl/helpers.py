import config


def categorize_from_filename(filename, radiationtype):
    """For POP purpose only
       1, 2, 3, 15
       15 is changed to 4
    """
    real_cat_num = int(filename.split('.')[0])
    if real_cat_num == 15:
        real_cat_num = 4
    if radiationtype == 'dni':
        return [real_cat_num -1]
    else:
        return [(real_cat_num -1) + config.NUM_CATEGORIES]
