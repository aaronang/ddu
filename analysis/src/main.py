import math
import json
import os
import csv

import scipy.stats.stats as st
import scipy.stats as stats
import matplotlib.pyplot as plt

from functools import reduce
from spectra import csv_to_spectra
from matrix import transpose, unique

def to_float(s):
    try:
        return float(s)
    except ValueError:
        return s

def package_dicts(packages):
    return { package: {} for package in packages }

def spectra_to_dict(spectra):
    return { c[0]: c[1:] for c in spectra }

def density(activity):
    a = sum(activity, [])
    try:
        return sum(a) / len(a)
    except ZeroDivisionError:
        return 0

def normalized_density(activity):
    p = density(activity)
    return 1 - math.fabs(1 - 2 * p)

def remove_no_hit(transactions, transaction):
    if sum(transaction) > 0:
        transactions += [transaction]
    return transactions

def diversity(activity):
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

def uniqueness(activity):
    g = unique(activity)
    try:
        return len(g) / len(activity)
    except ZeroDivisionError:
        return 0

def unit_vs_integration(components_activity):
    transactions = transpose(components_activity)
    integration_tests = len(list(filter(lambda t: sum(t) > 1, transactions)))
    unit_tests = len(transactions) - integration_tests
    try:
        return unit_tests / integration_tests
    except ZeroDivisionError:
        return -1

def compute_metrics(spectra, packages):
    spectra = transpose(spectra)[1:]
    spectra_dict = spectra_to_dict(spectra)
    ddus = package_dicts(packages)
    for p, cs in packages.items():
        components_activity = list(map(lambda c: spectra_dict[c], cs))
        transactions = transpose(components_activity)
        transactions = reduce(remove_no_hit, transactions, [])
        components_activity = transpose(transactions)
        ddus[p]['number_of_classes'] = len(cs)
        ddus[p]['number_of_tests'] = len(transactions)
        ddus[p]['density'] = density(components_activity)
        ddus[p]['normalized_density'] = normalized_density(components_activity)
        ddus[p]['diversity'] = diversity(components_activity)
        ddus[p]['uniqueness'] = uniqueness(components_activity)
        ddus[p]['ddu'] = ddus[p]['normalized_density'] * ddus[p]['diversity'] * ddus[p]['uniqueness']
        ddus[p]['unit_vs_integration'] = unit_vs_integration(components_activity)
    return ddus

def pp(data):
    print(json.dumps(data, indent=4))

def print_spectra(spectra):
    components_activity = transpose(spectra)

    s = [c for c in components_activity if 'translate' in c[0] or len(c[0]) == 0]
    s = transpose(s)
    ts = [t for t in s[1:] if sum(t[1:]) > 0]
    ts = [s[0]] + ts
    for t in ts:
        print(t)

def write_to_csv(csvname, ddus):
    with open('../output/' + csvname, 'w', newline='') as csvfile:
        fieldnames = ['package', 'number_of_classes', 'number_of_tests', 'density', 'normalized_density', 'diversity', 'uniqueness', 'ddu', 'unit_vs_integration']
        writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for package, data in ddus.items():
            row = { 'package': package }
            row.update(data)
            writer.writerow(row)

def metric_to_csv(csvname):
    spectra, components = csv_to_spectra('../data/spectra/' + csvname)
    metrics = compute_metrics(spectra, components)
    write_to_csv(csvname, metrics)

def metrics_to_csv(dir):
    for filename in os.listdir(dir):
        if filename.endswith(".csv"):
            print('Computing metrics for', dir + filename)
            metric_to_csv(filename)
            print('Successfully written metrics to', dir + filename)

def get_column(data, c):
    return list(map(lambda r: to_float(r[c]), data))

def analyze():
    data = []
    for filename in os.listdir('../output'):
        if filename.endswith(".csv"):
            print(os.path.join('../output', filename))
            with open(os.path.join('../output', filename)) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    data.append(row)

    number_of_tests = get_column(data, 'number_of_tests')
    number_of_classes = get_column(data, 'number_of_classes')
    density = get_column(data, 'density')
    diversity = get_column(data, 'diversity')
    uniqueness = get_column(data, 'uniqueness')
    ddu = get_column(data, 'ddu')
    unit_vs_integration = get_column(data, 'unit_vs_integration')

    utddu = filter(lambda x: x[0] != -1, zip(unit_vs_integration, ddu))
    utddu = list(zip(*utddu))
    ut = utddu[0]
    dduu = utddu[1]
    # print('[Pearson] Number of tests vs. DDU', st.pearsonr(number_of_tests, ddu))
    # print('[Pearson] Number of tests vs. density',st.pearsonr(number_of_tests, density))
    # print('[Pearson] Number of classes vs. DDU',st.pearsonr(number_of_classes, ddu))
    # print('[Pearson] Number of classes vs. density',st.pearsonr(number_of_classes, density))
    # print('[Spearman] Number of tests vs. DDU', st.spearmanr(number_of_tests, ddu))
    # print('[Spearman] Number of tests vs. density',st.spearmanr(number_of_tests, density))
    # print('[Spearman] Number of tests vs. diversity', st.spearmanr(number_of_tests, diversity))
    # print('[Spearman] Number of tests vs. uniqueness',st.spearmanr(number_of_tests, uniqueness))
    # print('[Spearman] Number of classes vs. DDU',st.spearmanr(number_of_classes, ddu))
    # print('[Spearman] Number of classes vs. density',st.spearmanr(number_of_classes, density))
    # print('[Spearman] Number of classes vs. diversity',st.spearmanr(number_of_classes, diversity))
    # print('[Spearman] Number of classes vs. uniqueness',st.spearmanr(number_of_classes, uniqueness))
    #
    # print('[Spearman] density vs. diversity',st.spearmanr(density, diversity))
    # print('[Spearman] density vs. uniqueness',st.spearmanr(density, uniqueness))
    # print('[Spearman] diversity vs. uniqueness',st.spearmanr(diversity, uniqueness))

    # _, axarr = plt.subplot(1)

    # axarr[0, 0].set_title('Number of tests vs. DDU')
    # axarr[0, 0].scatter(number_of_tests, ddu)
    # axarr[0, 0].grid(True)
    # axarr[1, 0].set_title('Number of tests vs. density')
    # axarr[1, 0].scatter(number_of_tests, density)
    # axarr[1, 0].grid(True)
    # axarr[2, 0].set_title('Number of tests vs. diversity')
    # axarr[2, 0].scatter(number_of_tests, diversity)
    # axarr[2, 0].grid(True)
    # axarr[3, 0].set_title('Number of tests vs. uniqueness')
    # axarr[3, 0].scatter(number_of_tests, uniqueness)
    # axarr[3, 0].grid(True)
    # axarr[0, 1].set_title('Number of classes vs. DDU')
    # axarr[0, 1].scatter(number_of_classes, ddu)
    # axarr[0, 1].grid(True)
    # axarr[1, 1].set_title('Number of classes vs. density')
    # axarr[1, 1].scatter(number_of_classes, density)
    # axarr[1, 1].grid(True)
    # axarr[2, 1].set_title('Number of classes vs. diversity')
    # axarr[2, 1].scatter(number_of_classes, diversity)
    # axarr[2, 1].grid(True)

    print('[Spearman] Unit vs. integration vs. DDU',st.spearmanr(ut, dduu))
    print('[Pearson] Unit vs. integration vs. DDU',st.pearsonr(ut, dduu))

    print(stats.normaltest(ut))
    print(stats.normaltest(dduu))

    # plt.title('Unit vs. integration vs. DDU')
    # plt.scatter(ut, dduu)
    # plt.grid(True)
    #
    # plt.show()

def main():
    # ddus_to_csv('../data/spectra')
    # metrics_to_csv('commons-text.csv')
    # analyze()
    metrics_to_csv('../data/spectra/')


if __name__ == '__main__':
    main()
