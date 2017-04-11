from src.mhs.trie import Trie
from src.mhs.spectra_filter import SpectraFilter
from src.mhs.similarity_ranker import SimilarityRanker
from src.mhs.similarity_functions import ochiai


class MHS:

    def __init__(self, l=6):
        self.ranker = SimilarityRanker(ochiai)
        self.cutoff = l
        self.epsilon = 0.0001

    def __call__(self, spectra, spectra_filter=None):
        self.spectra = spectra

        if not spectra_filter:
            spectra_filter = SpectraFilter(self.spectra)

        spectra_filter.filter_passing_transactions(self.spectra)
        self.candidates = Trie()
        self.calculate_mhs(spectra_filter, [])
        return self.candidates

    def calculate_mhs(self, spectra_filter, d):
        if spectra_filter.has_failing_transactions(self.spectra):
            if (len(d) + 1 >= self.cutoff or
                    not spectra_filter.components_filter):
                return

            r = self.ranker(self.spectra, spectra_filter=spectra_filter)

            removed_components = 0
            for component, coefficient in reversed(r):
                if coefficient < self.epsilon:
                    spectra_filter.filter_component(component)
                    removed_components += 1
                else:
                    break

            if removed_components:
                r = r[:-removed_components]

            for component, coefficient in r:
                new_spectra_filter = spectra_filter.copy()
                new_spectra_filter.strip_component(self.spectra, component)
                spectra_filter.filter_component(component)
                self.calculate_mhs(new_spectra_filter, d + [component])

        elif d:
            self.candidates.add_candidate(sorted(d))
