import csv
import os
from functools import reduce

import matplotlib.pyplot as plt
import scipy.stats.mstats as mst
import scipy.stats.stats as st


def _get_column(data, c):
    return list(map(lambda r: r[c], data))


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

    # plot_effort_ddu(data, efforts)
    # plot_effort_density(data, efforts)
    # plot_effort_diversity(data, efforts)
    # plot_effort_uniqueness(data, efforts)
    # plot_percentage_ddu(data, percentages)
    # plot_normalized_density(data)
    # plot_diversity(data)
    # plot_uniqueness(data)
    # plot_ddu(data)
    # plot_uniqueness_vs_num_of_components(data)
    percentage_couple_components_uniqueness(data)
    # plot_uniqueness_and_tests(data)


def plot_uniqueness_and_tests(data):
    """
    Test correlation between uniqueness and number of tests only for classes that have two or more components.
    """
    uniqueness = _get_column(data, 'uniqueness')
    components = _get_column(data, 'number_of_components')
    tests = _get_column(data, 'number_of_tests')
    d = zip(uniqueness, components, tests)
    d = [(float(u), int(c), int(t)) for u, c, t in d if u and c and t]
    d = [(u, c, t) for u, c, t in d if c > 1]
    u, c, t = zip(*d)
    print("Normal test uniqueness:", mst.normaltest(u))
    print("Normal test components:", mst.normaltest(t))
    print("[Pearson]", st.pearsonr(u, t))
    print("[Spearman]", st.spearmanr(u, t))

    plt.scatter(u, t)
    plt.xlabel('Uniqueness')
    plt.ylabel('Number of components')
    plt.title('Uniqueness vs. number of components')
    plt.grid(True)
    plt.show()


def percentage_couple_components_uniqueness(data):
    uniqueness = _get_column(data, 'uniqueness')
    components = _get_column(data, 'number_of_components')
    ts = zip(uniqueness, components)
    ts = [(float(u), int(c)) for u, c in ts if u and c]
    optimal_uniquenesses = [(u, c) for u, c in ts if u == 1.0]
    less = [(u, c) for u, c in optimal_uniquenesses if c < 2]
    print(len(less))
    print(len(optimal_uniquenesses))
    print(len(less) / float(len(optimal_uniquenesses)))


def plot_uniqueness_vs_num_of_components(data):
    def transform(tuples):
        return [(float(u), int(c)) for u, c in tuples if u and c]

    uniqueness = _get_column(data, 'uniqueness')
    num_of_components = list(_get_column(data, 'number_of_components'))
    t = zip(uniqueness, num_of_components)
    u, c = zip(*transform(t))

    print("Normal test uniqueness:", mst.normaltest(u))
    print("Normal test components:", mst.normaltest(c))
    print("[Pearson]", st.pearsonr(u, c))
    print("[Spearman]", st.spearmanr(u, c))

    plt.scatter(u, c)
    plt.xlabel('Uniqueness')
    plt.ylabel('Number of components')
    plt.title('Uniqueness vs. number of components')
    plt.grid(True)
    plt.show()


def plot_percentage_ddu(data, percentages):
    a = []
    for class_name, percentage in percentages.items():
        class_data = list(filter(lambda x: x['parent'] == class_name, data))[0]
        a.append((float(class_data['ddu']), percentage))
    x, y = zip(*a)
    plt.scatter(y, x)
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
    ddu = _get_column(data, 'ddu')
    ddu = [float(x) for x in ddu if x]
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
    diversity = _get_column(data, 'diversity')
    diversity = [float(x) for x in diversity if x]
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
    uniqueness = _get_column(data, 'uniqueness')
    uniqueness = [float(x) for x in uniqueness if x]
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
    normalized_density = _get_column(data, 'normalized_density')
    normalized_density = [float(x) for x in normalized_density if x]
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
