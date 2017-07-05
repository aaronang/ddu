import itertools
import random
import sys


class ActivityGenerator:
    def __init__(self, spectra, cardinality):
        self.spectra = spectra
        self.unique_rows = self._unique_rows(spectra.matrix)
        self.cardinality = cardinality
        self.candidates_with_error = self._candidates_with_error()

    def _candidates_with_error(self):
        erroneous_components_per_row = [[i for i, c in enumerate(row) if c == 1] for row in self.unique_rows]
        s = {candidate for row in erroneous_components_per_row for candidate in itertools.combinations(row, self.cardinality)}
        return [list(x) for x in s]

    def _unique_rows(self, matrix):
        return [list(x) for x in set(tuple(x) for x in matrix)]

    def _generate_faulty_set(self, errors_only):
        if self.cardinality > self.spectra.num_of_components:
            sys.exit('Cardinality cannot be lower than number of components.')

        if errors_only:
            return random.choice(self.candidates_with_error)
        else:
            return random.sample(range(self.spectra.num_of_components), self.cardinality)

    def _generate_error_vector(self, faulty_set, goodness):
        def is_error_with_goodness(transaction):
            is_error = all([transaction[i] == 1 for i in faulty_set])
            error_chance = random.random() >= goodness
            # print(error_chance)
            if is_error and error_chance:
                return True
            else:
                return False

        return list(map(is_error_with_goodness, self.spectra.matrix))

    def _transform_error(self, error):
        return '-' if error else '+'

    def generate(self, goodness=0, errors_only=False):
        faulty_set = self._generate_faulty_set(errors_only)
        error_vector = self._generate_error_vector(faulty_set, goodness)
        error_vector = list(map(self._transform_error, error_vector))

        activity_matrix = zip(self.spectra.matrix, error_vector)
        activity_matrix = [x + [y] for x, y in activity_matrix]

        return activity_matrix, faulty_set

    def generate_given_fault(self, faulty_set, goodness=0, errors_only=False):
        error_vector = self._generate_error_vector(faulty_set, goodness)
        error_vector = list(map(self._transform_error, error_vector))

        activity_matrix = zip(self.spectra.matrix, error_vector)
        activity_matrix = [x + [y] for x, y in activity_matrix]

        return activity_matrix