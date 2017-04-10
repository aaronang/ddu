import os

from src.effort.activity_generator import ActivityGenerator
from src.effort.spectra import Spectra
from src.effort.util import to_str

current_dir = os.path.dirname(__file__)
directory = os.path.normpath(os.path.join(current_dir, 'output/spectra'))

for filename in os.listdir(directory):
    spectra = Spectra('output/spectra/%s' % filename)
    activity_generator = ActivityGenerator(spectra)

    output = 'output/matrices/%s' % filename
    if not os.path.exists(output):
        os.makedirs(output)

    fault_sets = []

    while len(fault_sets) < 20:
        activity_matrix, faulty_set = activity_generator.generate(2)
        faulty_set.sort()
        h = hash(frozenset(faulty_set))
        if h not in fault_sets:
            fault_sets.append(h)
            name = '_'.join(to_str(faulty_set))
            with open('output/matrices/%s/%s.txt' % (filename, name), 'w') as f:
                for column in activity_matrix:
                    f.write(' '.join(to_str(column)))
                    f.write('\n')
