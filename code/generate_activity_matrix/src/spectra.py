import re


class Spectra:
    def __init__(self, filename):
        self.matrix = []
        self.num_of_components = 0
        self.num_of_transactions = 0
        self._read(filename)

    def _read(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                line = re.sub('].*', '', line)
                line = re.sub('[^01]', '', line)
                line = list(map(int, line))
                self.matrix.append(line)

        self.num_of_transactions = len(self.matrix)
        self.num_of_components = len(self.matrix[0])
