import os

from src.effort.activity_generator import ActivityGenerator
from src.effort.spectra import Spectra
from src.effort.util import to_str

dir = os.path.dirname(__file__)
directory = os.path.normpath(os.path.join(dir, 'output/spectra'))

for filename in filenames:
    print(filename)
    spectra = Spectra('resources/spectra/%s' % filename)
    activity_generator = ActivityGenerator(spectra)

    output = 'out/matrices/%s' % filename
    if not os.path.exists(output):
        os.makedirs(output)

    faulties = []

    while len(faulties) < 5:
        activity_matrix, faulty_set = activity_generator.generate(2)
        faulty_set.sort()
        h = hash(frozenset(faulty_set))
        if h not in faulties:
            faulties.append(h)
            name = '_'.join(to_str(faulty_set))
            with open('out/matrices/%s/%s.txt' % (filename, name), 'w') as f:
                for column in activity_matrix:
                    f.write(' '.join(to_str(column)))
                    f.write('\n')
