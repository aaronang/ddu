import os
import math
import csv

from spectra import csv_to_spectra
from matrix import transpose, unique
from functools import reduce

def _spectra_to_dict(spectra):
    return { c[0]: c[1:] for c in spectra }

def _package_dicts(packages):
    return { package: {} for package in packages }

def _density(activity):
    a = sum(activity, [])
    try:
        return sum(a) / len(a)
    except ZeroDivisionError:
        return 0

def _normalized_density(activity):
    p = _density(activity)
    return 1 - math.fabs(1 - 2 * p)

def _remove_no_hit(transactions, transaction):
    if sum(transaction) > 0:
        transactions += [transaction]
    return transactions

def _diversity(activity):
    transactions = transpose(activity)
    unique_transactions = unique(transactions)
    buckets = list(map(lambda t: transactions.count(t), unique_transactions))
    numerator = reduce(lambda s, n: s + n * (n - 1), buckets, 0)
    num_of_transactions = len(transactions)
    denominator = num_of_transactions * (num_of_transactions - 1)
    try:
        return 1 - numerator / denominator
    except ZeroDivisionError:
        return 0

def _uniqueness(activity):
    g = unique(activity)
    try:
        return len(g) / len(activity)
    except ZeroDivisionError:
        return 0

def _unit_vs_integration(components_activity):
    transactions = transpose(components_activity)
    integration_tests = len(list(filter(lambda t: sum(t) > 1, transactions)))
    unit_tests = len(transactions) - integration_tests
    try:
        return unit_tests / integration_tests
    except ZeroDivisionError:
        return -1

def _compute_metrics(spectra, packages):
    spectra = transpose(spectra)[1:]
    spectra_dict = _spectra_to_dict(spectra)
    ddus = _package_dicts(packages)
    for p, cs in packages.items():
        components_activity = list(map(lambda c: spectra_dict[c], cs))
        transactions = transpose(components_activity)
        transactions = reduce(_remove_no_hit, transactions, [])
        components_activity = transpose(transactions)
        ddus[p]['number_of_classes'] = len(cs)
        ddus[p]['number_of_tests'] = len(transactions)
        ddus[p]['density'] = _density(components_activity)
        ddus[p]['normalized_density'] = _normalized_density(components_activity)
        ddus[p]['diversity'] = _diversity(components_activity)
        ddus[p]['uniqueness'] = _uniqueness(components_activity)
        ddus[p]['ddu'] = ddus[p]['normalized_density'] * ddus[p]['diversity'] * ddus[p]['uniqueness']
        ddus[p]['unit_vs_integration'] = _unit_vs_integration(components_activity)
    return ddus

def _write_to_csv(csvname, ddus):
    dir = os.path.dirname(__file__)
    filename = os.path.normpath(os.path.join(dir, '../output/' + csvname))
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['package', 'number_of_classes', 'number_of_tests', 'density', 'normalized_density', 'diversity', 'uniqueness', 'ddu', 'unit_vs_integration']
        writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for package, data in ddus.items():
            row = { 'package': package }
            row.update(data)
            writer.writerow(row)

def metric_to_csv(csvname):
    spectra, components = csv_to_spectra(csvname)
    metrics = _compute_metrics(spectra, components)
    _write_to_csv(csvname, metrics)

def metrics_to_csv():
    dir = os.path.dirname(__file__)
    directory = os.path.normpath(os.path.join(dir, '../data/spectra/'))
    output_dir = os.path.normpath(os.path.join(dir, '../output/'))
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            print('Computing metrics for', directory + '/' + filename)
            metric_to_csv(filename)
            print('Successfully written metrics to', output_dir + '/' + filename)