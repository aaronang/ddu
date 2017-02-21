import os
import csv

import scipy.stats.stats as st
import scipy.stats as stats
import matplotlib.pyplot as plt

from matrix import to_float

def _get_column(data, c):
    return list(map(lambda r: to_float(r[c]), data))

def analyze():
    dir = os.path.dirname(__file__)
    directory = os.path.normpath(os.path.join(dir, '../output/'))
    data = []
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            print(os.path.join(directory, filename))
            with open(os.path.join(directory, filename)) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    data.append(row)

    number_of_tests = _get_column(data, 'number_of_tests')
    number_of_classes = _get_column(data, 'number_of_classes')
    density = _get_column(data, 'density')
    diversity = _get_column(data, 'diversity')
    uniqueness = _get_column(data, 'uniqueness')
    ddu = _get_column(data, 'ddu')
    unit_vs_integration = _get_column(data, 'unit_vs_integration')

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
