import sys


class SpectraFilter:
    def __init__(self, spectra):
        if spectra:
            self.transactions_filter = \
                [x for x in range(spectra.transactions)]
            self.components_filter = \
                [x for x in range(spectra.components)]

    def copy(self):
        sf = SpectraFilter(None)
        sf.transactions_filter = self.transactions_filter[:]
        sf.components_filter = self.components_filter[:]
        return sf

    def strip_component(self, spectra, component):
        self.transactions_filter = [t for t in self.transactions_filter
                                    if not spectra.get_activity(t, component)]
        self.components_filter.remove(component)

    def filter_component(self, component):
        self.components_filter.remove(component)

    def filter_transaction(self, transaction):
        self.transactions_filter.remove(transaction)

    def filter_passing_transactions(self, spectra):
        self.transactions_filter = [t for t in self.transactions_filter
                                    if spectra.is_error(t)]

    def has_failing_transactions(self, spectra):
        for t in self.transactions_filter:
            if spectra.is_error(t):
                return True
        return False

    def print_filter(self, out=sys.stdout):
        out.write('Transactions:\t%s\n' % self.transactions_filter)
        out.write('Components:\t%s\n' % self.components_filter)
