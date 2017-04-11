from src.mhs.spectra_filter import SpectraFilter

import sys


class Spectra:

    def __init__(self):
        self.matrix = []
        self.transactions = 0
        self.components = 0

    def read(self, filename):
        f = open(filename)
        self.matrix = []
        for line in f:
            line = line.rstrip().replace(' ', '') \
                                .replace('x', '1')\
                                .replace('.', '0')\
                                .replace('-', '1')\
                                .replace('+', '0')
            line = list(map(int, line))
            self.matrix.append(line)

        self.transactions = len(self.matrix)
        self.components = len(self.matrix[0]) - 1

    def get_transaction_activity(self, transaction):
        return self.matrix[transaction]

    def get_activity(self, transaction, component):
        return self.matrix[transaction][component]

    def is_error(self, transaction):
        return self.matrix[transaction][-1]

    def print_spectra(self, out=sys.stdout, spectra_filter=None):
        if not spectra_filter:
            spectra_filter = SpectraFilter(self)

        for t in spectra_filter.transactions_filter:

            for c in spectra_filter.components_filter:
                out.write('%d ' % self.get_activity(t, c))

            if self.is_error(t):
                out.write('x\n')
            else:
                out.write('.\n')
