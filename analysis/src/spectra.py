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
    transactions = spectra[1:]
    unique_components = set(components[1:])
    for component in unique_components:
        positions = _indexes(component, components)
        for j, transaction in enumerate(transactions):
            if sum([transaction[i] for i in positions]) > 0:
                for p in positions:
                    transactions[j][p] = 1
    data = [components] + transactions
    component_columns = transpose(data)
    return transpose(unique(component_columns))

def _is_test(x, y):
    if 'test' not in y[0] and 'Test' not in y[0]:
        x.append(y)
    return x

def _remove_tests(spectra):
    components = transpose(spectra)
    no_tests = reduce(_is_test, components, [])
    return transpose(no_tests)

def _unique_components(spectra):
    return set(spectra[0][1:])

def _get_package(name):
    n = name.split('.')
    n.pop()
    return '.'.join(n)

def _get_packages(spectra):
    components = _unique_components(spectra)
    packages = list(map(_get_package, components))
    packages = unique(packages)
    return reduce(_assign_package, components, _package_dict(packages))

def _assign_package(packages, component):
    key = _get_package(component)
    keys = [k for k in packages if k in key]
    for k in keys:
        packages[k].append(component)
    return packages

def _package_dict(packages):
    return { package: [] for package in packages }

def csv_to_spectra(input):
    with open(input) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        full_name_components = next(reader)
        components = list(map(_get_class, full_name_components))
        activity = reduce(_append, reader, [])
        spectra = [components] + activity
        filtered = _remove_tests(_filter_class(spectra))
        return filtered, _get_packages(filtered)
