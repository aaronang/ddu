import csv
import os
from functools import reduce

import scipy.stats.stats as st

import scipy.stats.mstats as mst

import matplotlib.pyplot as plt

from matrix import to_float


def _get_column(data, c, transform=(lambda x: x)):
    return list(map(lambda r: transform(r[c]), data))


def analyze(granularity):
    current_dir = os.path.dirname(__file__)
    directory = os.path.normpath(os.path.join(current_dir, '../output/%s' % granularity))
    data = []
    for filename in os.listdir(directory):
        if filename.endswith(".csv") and ("commons-text" in filename or
                                                  "commons-csv" in filename or
                                                  "guice" in filename or
                                                  "jsoup" in filename or
                                                  "commons-io" in filename):
            print(os.path.join(directory, filename))
            with open(os.path.join(directory, filename)) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    data.append(row)

    efforts = {}
    with open(os.path.join(current_dir, '../output/effort.csv')) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            efforts.update({row['class']: float(row['average_wasted_effort'])})

    percentages = {}
    with open(os.path.join(current_dir, '../output/percentages.csv')) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            percentages.update({row['class']: float(row['percentage'])})

    plot_effort_ddu(data, efforts)
    # plot_effort_density(data, efforts)
    # plot_effort_diversity(data, efforts)
    # plot_effort_uniqueness(data, efforts)
    # plot_percentage_ddu(data, percentages)
    # plot_normalized_density(data)
    # plot_diversity(data)
    # plot_uniqueness(data)
    # plot_ddu(data)


def plot_percentage_ddu(data, percentages):
    a = []
    for class_name, percentage in percentages.items():
        class_data = list(filter(lambda x: x['parent'] == class_name, data))[0]
        a.append((float(class_data['ddu']), percentage))
    x, y = zip(*a)
    plt.scatter(x, y)
    plt.xlabel('DDU')
    plt.ylabel('Faulty spectra')
    plt.title('DDU vs. faulty spectra')
    plt.grid(True)
    plt.show()


def plot_effort_ddu(data, efforts):
    a = []
    for class_name, effort in efforts.items():
        class_data = list(filter(lambda x: x['parent'] == class_name, data))[0]
        a.append((float(class_data['ddu']), effort))
    x, y = zip(*a)
    print("Normal test DDU:", mst.normaltest(x))
    print("Normal test effort:", mst.normaltest(y))
    print("[Pearson]", st.pearsonr(x, y))
    print("[Spearman]", st.spearmanr(x, y))
    plt.scatter(x, y)
    plt.xlabel('DDU')
    plt.ylabel('Average wasted effort')
    plt.title('DDU vs. average wasted effort')
    plt.grid(True)
    plt.xlim(0.0, 1.0)
    plt.ylim(0, 80)
    plt.show()


def plot_effort_density(data, efforts):
    a = []
    for class_name, effort in efforts.items():
        class_data = list(filter(lambda x: x['parent'] == class_name, data))[0]
        a.append((float(class_data['normalized_density']), effort))
    x, y = zip(*a)
    plt.scatter(x, y)
    plt.xlabel('density')
    plt.ylabel('Average wasted effort')
    plt.title('Density vs. average wasted effort')
    plt.grid(True)
    plt.show()


def plot_effort_diversity(data, efforts):
    a = []
    for class_name, effort in efforts.items():
        class_data = list(filter(lambda x: x['parent'] == class_name, data))[0]
        a.append((float(class_data['diversity']), effort))
    x, y = zip(*a)
    plt.scatter(x, y)
    plt.xlabel('Diversity')
    plt.ylabel('Average wasted effort')
    plt.title('Diversity vs. average wasted effort')
    plt.grid(True)
    plt.show()


def plot_effort_uniqueness(data, efforts):
    a = []
    for class_name, effort in efforts.items():
        class_data = list(filter(lambda x: x['parent'] == class_name, data))[0]
        a.append((float(class_data['uniqueness']), effort))
    x, y = zip(*a)
    plt.scatter(x, y)
    plt.xlabel('Uniqueness')
    plt.ylabel('Average wasted effort')
    plt.title('Uniqueness vs. average wasted effort')
    plt.grid(True)
    plt.show()


def plot_ddu(data):
    ddu = list(filter(lambda x: not (x < 0), _get_column(data, 'ddu', to_float)))
    print(ddu)
    print(reduce(lambda x, y: x + y, ddu) / len(ddu))

    bins = [float(x) / 10 for x in range(0, 10)]
    bins.append(1.0)
    plt.hist(ddu, bins=bins)
    plt.xlabel('DDU')
    plt.ylabel('Frequency')
    plt.title('DDU of classes')
    plt.grid(True)

    plt.show()


def plot_diversity(data):
    diversity = list(filter(lambda x: not (x < 0), _get_column(data, 'diversity', to_float)))
    print(diversity)
    print(reduce(lambda x, y: x + y, diversity) / len(diversity))

    bins = [float(x) / 10 for x in range(0, 10)]
    bins.append(1.0)
    plt.hist(diversity, bins=bins)
    plt.xlabel('Diversity')
    plt.ylabel('Frequency')
    plt.title('Diversity of classes')
    plt.grid(True)

    plt.show()


def plot_uniqueness(data):
    uniqueness = list(filter(lambda x: not (x < 0), _get_column(data, 'uniqueness', to_float)))
    print(uniqueness)
    print(reduce(lambda x, y: x + y, uniqueness) / len(uniqueness))

    bins = [float(x) / 10 for x in range(0, 10)]
    bins.append(1.0)
    plt.hist(uniqueness, bins=bins)
    plt.xlabel('Uniqueness')
    plt.ylabel('Frequency')
    plt.title('Uniqueness of classes')
    plt.grid(True)

    plt.show()


def plot_normalized_density(data):
    normalized_density = list(filter(lambda x: not (x < 0), _get_column(data, 'normalized_density', to_float)))
    print(normalized_density)
    print(reduce(lambda x, y: x + y, normalized_density) / len(normalized_density))

    bins = [float(x) / 10 for x in range(0, 10)]
    bins.append(1.0)
    plt.hist(normalized_density, bins=bins)
    plt.xlabel('Normalized density')
    plt.ylabel('Frequency')
    plt.title('Normalized density of classes')
    plt.grid(True)

    plt.show()
