from src.mhs.similarity_functions import ochiai
from src.mhs.spectra_filter import SpectraFilter

import operator


class SimilarityRanker:

    def __init__(self, heuristic=ochiai):
        self.heuristic = heuristic

    def __call__(self, spectra, spectra_filter=None):
        if not spectra_filter:
            spectra_filter = SpectraFilter(spectra)

        ranking = []
        error = {}
        for t in spectra_filter.transactions_filter:
            error[t] = spectra.is_error(t)

        for c in spectra_filter.components_filter:
            n = [[0, 0], [0, 0]]

            for t in spectra_filter.transactions_filter:
                activity = spectra.get_activity(t, c)
                n[1 if activity else 0][1 if error[t] else 0] += 1

            ranking.append((c, self.heuristic(n)))

        return sorted(ranking, key=operator.itemgetter(1), reverse=True)
