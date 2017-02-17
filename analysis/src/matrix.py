from functools import reduce

def _to_float(s):
    try:
        return float(s)
    except ValueError:
        return s

def get_column(data, c):
    return list(map(lambda r: _to_float(r[c]), data))

def transpose(data):
    if len(data) == 0:
        return []
    return [[row[i] for row in data] for i in range(len(data[0]))]

def unique(matrix):
    return reduce(_uniq, matrix, [])

def _uniq(x, y):
    if y not in x:
        return x + [y]
    else:
        return x
