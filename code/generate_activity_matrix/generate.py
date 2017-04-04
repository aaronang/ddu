import os

from src.activity_generator import ActivityGenerator
from src.spectra import Spectra
from src.util import to_str

spectra = Spectra()
filename = 'com.google.inject.TypeLiteral'
spectra.read('resources/spectra/%s' % filename)
activity_generator = ActivityGenerator(spectra)

output = 'out/guice/%s' % filename
if not os.path.exists(output):
    os.makedirs(output)

faulties = []

while len(faulties) < 10:
    activity_matrix, faulty_set = activity_generator.generate(2)
    faulty_set.sort()
    h = hash(frozenset(faulty_set))
    if h not in faulties:
        faulties.append(h)
        name = '_'.join(to_str(faulty_set))
        with open('out/guice/%s/%s.txt' % (filename, name), 'w') as f:
            for column in activity_matrix:
                f.write(' '.join(to_str(column)))
                f.write('\n')
