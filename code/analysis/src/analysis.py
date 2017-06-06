import csv
import os
import numpy
from functools import reduce

import matplotlib.pyplot as plt
import scipy.stats.mstats as mst
import scipy.stats.stats as st


def _get_column(data, c):
    return list(map(lambda r: r[c], data))


def analyze(granularity, output_name=''):
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

    # erroneous_matrices = {}
    # with open(os.path.join(current_dir, '../output/effort.csv')) as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     for row in reader:
    #         erroneous_matrices.update({row['class']: float(row['erroneous_matrices'])})
    #
    # percentages = {}
    # with open(os.path.join(current_dir, '../output/percentages.csv')) as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     for row in reader:
    #         percentages.update({row['class']: float(row['percentage'])})

    plot_effort_ddu(data, efforts)
    # plot_erroneous_matrices_ddu(data, erroneous_matrices)
    # plot_effort_erroneous_matrices(efforts, erroneous_matrices)
    # plot_effort_density(data, efforts)
    # plot_effort_diversity(data, efforts)
    # plot_effort_uniqueness(data, efforts)
    # plot_effort_num_of_components(data, efforts)
    # plot_error_detection_ddu(output_name, data, percentages)
    # plot_error_detection_density(data, percentages)
    # plot_normalized_density(data)
    # plot_diversity(data)
    # plot_uniqueness(data)
    # plot_ddu(data)
    # plot_uniqueness_vs_num_of_components(data)
    # percentage_couple_components_uniqueness(data)
    # plot_uniqueness_and_tests(data)
    # effort_correlation(data, efforts)
    # plot_effort_density(data, efforts)


def effort_correlation(data, efforts):
    a = []
    for class_name, percentage in efforts.items():
        class_data = list(filter(lambda x: x['parent'] == class_name, data))[0]
        normalized_density = class_data['normalized_density']
        diversity = class_data['diversity']
        uniqueness = class_data['uniqueness']
        if normalized_density and diversity and uniqueness:
            a.append((float(normalized_density), float(diversity), float(uniqueness), percentage))
    nd, d, u, e = zip(*a)
    print("Normal test density:", mst.normaltest(nd))
    print("Normal test diversity:", mst.normaltest(d))
    print("Normal test uniqueness:", mst.normaltest(u))
    print("Normal test effort:", mst.normaltest(e))
    print("[Spearman] density vs. effort", st.spearmanr(nd, e))
    print("[Spearman] diversity vs. effort", st.spearmanr(d, e))
    print("[Spearman] uniqueness vs. effort", st.spearmanr(u, e))
    print("[Pearson] density vs. effort", st.pearsonr(nd, e))
    print("[Pearson] diversity vs. effort", st.pearsonr(d, e))
    print("[Pearson] uniqueness vs. effort", st.pearsonr(u, e))


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
    num_of_components = _get_column(data, 'number_of_tests')
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


def plot_error_detection_ddu(output_name, data, percentages):
    a = []
    for class_name, percentage in percentages.items():
        class_data = list(filter(lambda x: x['parent'] == class_name, data))[0]
        a.append((class_data['parent'], float(class_data['ddu']), float(class_data['density']), percentage))
    # for name, ddu, percentage in sorted(a, key=lambda tup: tup[1], reverse=True):
    for name, ddu, density, percentage in a:
        print('Name: %s, DDU: %f, density: %f, percentage: %f' % (name, ddu, density, percentage))
        # ddu, percentage = zip(*a)
        # plt.scatter(ddu, percentage)
        # plt.xlabel('DDU')
        # plt.ylabel('Failure detection')
        # plt.title('DDU vs. failure detection')
        # plt.grid(True)
        #
        # plt.xlim(0.0, 1.0)
        # plt.ylim(0.0, 1.0)
        # plt.show()
        # z = numpy.polyfit(ddu, percentage, 1)
        # p = numpy.poly1d(z)
        # plt.plot(ddu, p(ddu), "--")

        # plt.savefig(output_name)


def plot_error_detection_density(data, percentages):
    a = []
    for class_name, percentage in percentages.items():
        class_data = list(filter(lambda x: x['parent'] == class_name, data))[0]
        a.append((float(class_data['density']), percentage))
    density, percentage = zip(*a)
    plt.scatter(density, percentage)
    plt.xlabel('Normalized density')
    plt.ylabel('Failure detection')
    plt.title('Normalized density vs. failure detection')
    plt.grid(True)

    plt.xlim(0.0, 1.0)
    plt.ylim(0.0, 1.0)
    plt.show()


def plot_effort_num_of_components(data, efforts):
    a = []
    for class_name, effort in efforts.items():
        class_data = list(filter(lambda x: x['parent'] == class_name, data))[0]
        a.append((float(class_data['number_of_components']), effort))
    x, y = zip(*a)
    print("Normal test number_of_components:", mst.normaltest(x))
    print("Normal test effort:", mst.normaltest(y))
    print("[Pearson]", st.pearsonr(x, y))
    print("[Spearman]", st.spearmanr(x, y))
    plt.scatter(x, y)
    plt.xlabel('number_of_components')
    plt.ylabel('Average wasted effort')
    plt.title('number_of_components vs. average wasted effort')
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
    plt.xlim(0, 1.0)
    plt.ylim(0, 1.0)
    z = numpy.polyfit(x, y, 1)
    p = numpy.poly1d(z)
    plt.plot(x, p(x), "r-")
    plt.show()


def plot_erroneous_matrices_ddu(data, erroneous_matrices):
    a = []
    for class_name, errors in erroneous_matrices.items():
        class_data = list(filter(lambda x: x['parent'] == class_name, data))[0]
        a.append((float(class_data['ddu']), errors))
    x, y = zip(*a)
    plt.scatter(x, y)
    plt.xlabel('DDU')
    plt.ylabel('Erroneous matrices')
    plt.title('DDU vs. erroneous matrices')
    plt.grid(True)
    plt.xlim(0, 1.0)
    plt.ylim(0, 1.0)
    z = numpy.polyfit(x, y, 1)
    p = numpy.poly1d(z)
    plt.plot(x, p(x), "r-")
    plt.show()


def plot_effort_erroneous_matrices(efforts, erroneous_matrices):
    a = []
    for class_name, effort in efforts.items():
        a.append((erroneous_matrices[class_name], effort))
    x, y = zip(*a)
    plt.scatter(x, y)
    plt.xlabel('Erroneous matrices')
    plt.ylabel('Effort')
    plt.title('Erroneous matrices vs. effort')
    plt.grid(True)
    plt.xlim(0, 1.0)
    plt.ylim(0, 1.0)
    z = numpy.polyfit(x, y, 1)
    p = numpy.poly1d(z)
    plt.plot(x, p(x), "r-")
    plt.show()


def plot_effort_density(data, efforts):
    a = []
    for class_name, effort in efforts.items():
        class_data = list(filter(lambda c: c['parent'] == class_name, data))[0]
        a.append((float(class_data['normalized_density']), effort))
    x, y = zip(*a)
    print("Normal test normalized density:", mst.normaltest(x))
    print("Normal test effort:", mst.normaltest(y))
    print("[Pearson]", st.pearsonr(x, y))
    print("[Spearman]", st.spearmanr(x, y))
    plt.scatter(x, y)
    plt.xlabel('Normalized density')
    plt.ylabel('Average wasted effort')
    plt.title('Normalized density vs. average wasted effort')
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
    diversity = _get_column(data, 'diversity')
    uniqueness = _get_column(data, 'uniqueness')
    normalized_density = _get_column(data, 'normalized_density')

    res = [(float(w), float(x), float(y), float(z)) for w, x, y, z in zip(ddu, normalized_density, diversity, uniqueness) if w and x and y and z]
    ddu, diversity, uniqueness, normalized_density = zip(*res)

    zeroes = [0 for ddu, den, div, uni in res if den == 0 or div == 0 or uni == 0]

    bins = [float(x) / 10 for x in range(0, 10)]
    bins.append(1.0)
    plt.hist(ddu, bins=bins)
    plt.xlabel('DDU')
    plt.ylabel('Frequency')
    plt.title('DDU of classes')
    plt.grid(True)

    plt.hist(zeroes, bins=bins, label='Zeroes')
    plt.legend(loc='upper right')

    plt.show()


def plot_diversity(data):
    diversity = _get_column(data, 'diversity')
    number_of_tests = _get_column(data, 'number_of_tests')
    number_of_components = _get_column(data, 'number_of_components')

    res = [(float(x), int(y), int(z)) for x, y, z in zip(diversity, number_of_tests, number_of_components) if x and y and z]
    diversity, number_of_tests, number_of_components = zip(*res)
    print(reduce(lambda x, y: x + y, diversity) / len(diversity))

    test_1 = [(d, nt, nc) for d, nt, nc in res if not d]
    print(len(test_1))
    print(test_1)
    test_1 = [0 for _ in test_1]

    bins = [float(x) / 10 for x in range(0, 10)]
    bins.append(1.0)
    plt.hist(diversity, bins=bins)
    plt.xlabel('Diversity')
    plt.ylabel('Frequency')
    plt.title('Diversity of classes')
    plt.grid(True)

    plt.hist(test_1, bins=bins, label='Zeroes')
    plt.legend(loc='lower right')


    plt.show()


def plot_uniqueness(data):
    uniqueness = _get_column(data, 'uniqueness')
    number_of_components = _get_column(data, 'number_of_components')
    d = [(float(u), int(c)) for u, c in zip(uniqueness, number_of_components) if u and c]
    uniqueness, number_of_components = zip(*d)

    one_component = [1.0 for u, c in d if c == 1]

    print(len(one_component))

    bins = [float(x) / 10 for x in range(0, 10)]
    bins.append(1.0)
    plt.hist(uniqueness, bins=bins)
    plt.xlabel('Uniqueness')
    plt.ylabel('Frequency')
    plt.title('Uniqueness of classes')
    plt.grid(True)

    plt.hist(one_component, bins=bins, label='Only one component')
    plt.legend(loc='lower right')

    plt.show()


def plot_normalized_density(data):
    normalized_density = _get_column(data, 'normalized_density')
    number_of_components = _get_column(data, 'number_of_components')
    names = _get_column(data, 'parent')
    d = [(float(d), int(c), n) for d, c, n in zip(normalized_density, number_of_components, names) if d and c]
    normalized_density, number_of_components, names = zip(*d)
    zeroes, components, _ = zip(*[(x, c, n) for x, c, n in d if not x])
    print(reduce(lambda x, y: x + y, normalized_density) / len(normalized_density))
    zc = [0.0 for x in components if x <= 1]
    between_6_7 = [(nd, c, n) for nd, c, n in d if 0.6 <= nd <= 0.7]
    print(between_6_7)

    bins = [float(x) / 10 for x in range(0, 10)]
    bins.append(1.0)
    plt.hist(normalized_density, bins=bins)
    plt.xlabel('Normalized density')
    plt.ylabel('Frequency')
    plt.title('Normalized density of classes')
    plt.grid(True)

    plt.hist(zeroes, bins=bins, label='Zeroes')

    plt.legend(loc='lower right')
    print(len(zc))

    plt.show()


if __name__ == "__main__":
    analyze('method')
