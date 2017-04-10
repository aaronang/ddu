import sys
import random


class ActivityGenerator:
    def __init__(self, spectra):
        self.spectra = spectra

    def _generate_faulty_set(self, cardinality):
        if cardinality > self.spectra.num_of_components:
            sys.exit('Cardinality cannot be lower than number of components.')

        return random.sample(range(self.spectra.num_of_components), cardinality)

    def _generate_error_vector(self, faulty_set):
        def is_error(transaction):
            return all([transaction[i] == 1 for i in faulty_set])

        return list(map(is_error, self.spectra.matrix))

    def _transform_error(self, error):
        return '-' if error else '+'

    def generate(self, cardinality):

        faulty_set = self._generate_faulty_set(cardinality)
        error_vector = self._generate_error_vector(faulty_set)
        error_vector = list(map(self._transform_error, error_vector))

        activity_matrix = zip(self.spectra.matrix, error_vector)
        activity_matrix = [x + [y] for x, y in activity_matrix]

        return activity_matrix, faulty_set



