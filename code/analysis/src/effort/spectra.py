import functools
import math
import re
import metrics

import matrix


class Spectra:
    def __init__(self, filename, class_name=''):
        self.matrix = []
        self.original_matrix = []
        self.num_of_components = 0
        self.num_of_transactions = 0
        self.class_name = class_name
        self._read(filename)

    def _read(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not self.class_name or self.class_name + 'Test' in line:
                    line = re.sub('].*', '', line)
                    line = re.sub('[^01]', '', line)
                    line = list(map(int, line))
                    self.matrix.append(line)

        self.num_of_transactions = len(self.matrix)
        self.num_of_components = len(self.matrix[0]) if self.matrix else 0
        self.original_matrix = self.matrix[:]

    def use_first_n_tests(self, n):
        self.matrix = self.original_matrix[:n]
        self.num_of_transactions = len(self.matrix)
        self.num_of_components = len(self.matrix[0])

    def density(self):
        ones = sum([sum(row) for row in self.matrix])
        return float(ones) / (self.num_of_components * self.num_of_transactions)

    def normalized_density(self):
        component_activity = matrix.transpose(self.matrix)
        return metrics.normalized_density(component_activity)

    def diversity(self):
        component_activity = matrix.transpose(self.matrix)
        return metrics.diversity(component_activity)

    def uniqueness(self):
        component_activity = matrix.transpose(self.matrix)
        return metrics.uniqueness(component_activity)

    def ddu(self):
        return self.normalized_density() * self.diversity() * self.uniqueness()
