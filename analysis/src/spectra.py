import csv
import re

from functools import reduce
from matrix import transpose, unique


def _get_class(name):
    return re.split(r'[#$]+', name)[0]

def _append(a, b):
    c = list(map(lambda x: _to_int(x), b))
    a.append(c)
    return a

def _to_int(s):
    try:
        return int(s)
    except ValueError:
        return s

def _indexes(x, xs):
    return [i  for (i, c) in enumerate(xs) if x == c]

def _filter_class(spectra):
    components = spectra[0]
    activity = spectra[1:]
    unique_components = set(components[1:])
    for component in unique_components:
        positions = _indexes(component, components)
        for j, transaction in enumerate(activity):
            if sum([transaction[i] for i in positions]) > 0:
                for p in positions:
                    activity[j][p] = 1
    data = [components] + activity
    activity_columns = transpose(data)
    return transpose(unique(activity_columns))


def csv_to_spectra(input):
    with open(input) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        full_name_components = next(reader)
        components = list(map(_get_class, full_name_components))
        activity = reduce(_append, reader, [])
        spectra = [components] + activity
        return _filter_class(spectra)
