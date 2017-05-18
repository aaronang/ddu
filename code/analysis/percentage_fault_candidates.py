import csv
import os
from functools import reduce, partial
import generate
import shutil
from src.analysis import analyze

CURRENT_DIR = os.path.dirname(__file__)
OUTPUT_DIR = os.path.join(CURRENT_DIR, 'output')
MATRICES_DIR = os.path.join(OUTPUT_DIR, 'matrices')
OUTPUT_PATH = os.path.join(OUTPUT_DIR, 'percentages.csv')


def is_fail_transaction(column):
    error_cell = column.strip()[-1]
    return True if error_cell is '-' else False


def has_fail_transaction(component_dir, matrix_file):
    filepath = os.path.join(component_dir, matrix_file)
    with open(filepath, 'r') as f:
        return reduce(lambda x, y: x or is_fail_transaction(y), f, False)


def num_of_files(directory):
    return len([filename for filename in os.listdir(directory) if os.path.isfile(os.path.join(directory, filename))])


def percentage_faults(component_dir):
    num_of_spectra = num_of_files(component_dir)
    failures = map(partial(has_fail_transaction, component_dir), os.listdir(component_dir))
    spectra_with_fail = list(filter(lambda x: x, failures))
    num_of_spectra_with_fail = len(spectra_with_fail)
    return float(num_of_spectra_with_fail) / num_of_spectra

for g in [0]:

    cs = []
    error_detection = []
    num_of_generations = 20
    cardinality = 2

    for r in range(num_of_generations):
        # Next three lines not necessary when matrices are generated.
        if os.path.exists(MATRICES_DIR):
            shutil.rmtree(MATRICES_DIR)
        generate.generate_matrices(20, cardinality, g)
        # 8, 1
        # 20, 2
        # 40, 3
        # 50, 4
        # 40, 5

        classes = [class_name for class_name in os.listdir(MATRICES_DIR)]
        class_dirs = [os.path.join(MATRICES_DIR, class_dir) for class_dir in os.listdir(MATRICES_DIR)]
        percentages = list(map(percentage_faults, class_dirs))

        data = list(zip(classes, percentages))
        data.sort(key=lambda x: x[0])
        cs, detection = zip(*data)
        print(cs)
        print(detection)

        if error_detection:
            error_detection = [x + y for x, y in zip(detection, error_detection)]
        else:
            error_detection = detection

    error_detection = [e / num_of_generations for e in error_detection]
    data = list(zip(cs, error_detection))
    data.sort(key=lambda x: x[1], reverse=True)

    with open(OUTPUT_PATH, 'w', newline='') as csvfile:
        fieldnames = [
            'class',
            'percentage'
        ]
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(fieldnames)
        for c, p in data:
            print(c, p)
            writer.writerow([c, p])

    # analyze('method', 'failure_detection_ddu_cardinality_%d_goodness_%f_rounds_20.png' % (cardinality, g))
