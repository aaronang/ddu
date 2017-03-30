import os
import csv

import matplotlib.pyplot as plt
from functools import reduce

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

    normalized_density = list(filter(lambda x: x not in [-1, 0], _get_column(data, 'normalized_density', to_float)))
    print(reduce(lambda x, y: x + y, normalized_density) / len(normalized_density))

    plt.hist(normalized_density, bins=[float(x) / 10 for x in range(0, 10)])
    plt.xlabel('Normalized density')
    plt.ylabel('Frequency')
    plt.title('Normalized density of classes')
    plt.grid(True)

    plt.show()
