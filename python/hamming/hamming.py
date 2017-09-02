def distance(str_1, str_2):
    if len(str_1) != len(str_2):
        raise ValueError
    return [str_2[x] == item for x, item in enumerate(str_1)].count(False)
