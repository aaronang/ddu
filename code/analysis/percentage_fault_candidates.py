import csv
import os
from functools import reduce, partial

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


classes = [class_name for class_name in os.listdir(MATRICES_DIR)]
class_dirs = [os.path.join(MATRICES_DIR, class_dir) for class_dir in os.listdir(MATRICES_DIR)]
percentages = list(map(percentage_faults, class_dirs))

with open(OUTPUT_PATH, 'w', newline='') as csvfile:
    fieldnames = [
        'class',
        'percentage'
    ]
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(fieldnames)
    for c, p in zip(classes, percentages):
        writer.writerow([c, p])
