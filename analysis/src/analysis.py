import csv
import os
from functools import reduce

import matplotlib.pyplot as plt

from matrix import to_float


def _get_column(data, c, transform=(lambda x: x)):
    return list(map(lambda r: transform(r[c]), data))


def analyze(granularity):
    dir = os.path.dirname(__file__)
    directory = os.path.normpath(os.path.join(dir, '../output/%s' % granularity))
    data = []
    for filename in os.listdir(directory):
        if filename.endswith(".csv") and ("commons-text" in filename or
                                                  "commons-csv" in filename or
                                                  "guice" in filename or
                                                  "jsoup" in filename):
            print(os.path.join(directory, filename))
            with open(os.path.join(directory, filename)) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    data.append(row)

    plot_normalized_density(data)
    plot_diversity(data)
    plot_uniqueness(data)
    plot_ddu(data)

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
