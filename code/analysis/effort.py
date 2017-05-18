import csv
import os
import re
import subprocess

import src.utils as utils
import src.effort.effort as eff
from src.mhs.spectra import Spectra
from src.mhs.mhs import MHS
from collections import OrderedDict
from operator import itemgetter

CWD = os.path.dirname(__file__)
STACCATO = os.path.join(CWD, 'lib/Staccato.macosx.x86_64')
BARINEL = os.path.join(CWD, 'lib/Barinel.macosx.x86_64')
OUT_DIR = os.path.join(CWD, 'output')
MATRICES_DIR = os.path.join(OUT_DIR, 'matrices')
STACCATO_OUT = 'out.staccato'
BARINEL_DIR = os.path.join(OUT_DIR, 'barinel')
EFFORT_OUT = os.path.join(OUT_DIR, 'effort.csv')

effort_dict = {}

for class_name in os.listdir(MATRICES_DIR):
    class_dir = os.path.join(MATRICES_DIR, class_name)
    barinel_out = os.path.join(BARINEL_DIR, class_name)
    print(class_dir)
    if not os.path.exists(barinel_out):
        os.makedirs(barinel_out)

    for filename in os.listdir(class_dir):
        filepath = os.path.join(class_dir, filename)
        print(filepath)

        with open(filepath, 'r') as f:
            columns = len(f.readline().split(' ')[:-1])
            columns = str(columns)

        print('Running Staccato')
        spectra = Spectra()
        spectra.read(filepath)

        mhs = MHS()
        candidates = mhs(spectra).get_candidates()
        utils.write_candidates(STACCATO_OUT, candidates)

        print('Running Barinel')
        barinel_output = os.path.join(barinel_out, filename)
        barinel = subprocess.Popen([BARINEL, columns, filepath, STACCATO_OUT, barinel_output],
                                   stdout=open(os.devnull, 'w'),
                                   stderr=subprocess.STDOUT)
        barinel.wait()

        os.remove(STACCATO_OUT)


    def _get_fault_set(filename):
        base = os.path.basename(filename)
        fault_set = os.path.splitext(base)[0].split('_')
        return list(map(int, fault_set))


    def _get_num_of_components(cdir):
        filepath = os.path.join(cdir, os.listdir(cdir)[0])
        with open(filepath, 'r') as f:
            row = f.readline().strip().split(' ')
            return len(row) - 1


    num_of_components = _get_num_of_components(class_dir)
    average_efforts = []
    for filename in os.listdir(barinel_out):
        filepath = os.path.join(barinel_out, filename)
        fault_set = _get_fault_set(filename)
        candidates = []
        probabilities = []
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                probability = float(re.findall('  .*', line)[0].strip())
                probabilities.append(probability)
                candidate = re.sub('  .*', '', line)
                candidate = re.sub('[{,}]', '', candidate)
                candidate = candidate.split(' ')
                candidate = list(map(lambda x: int(x) - 1, candidate))
                candidates.append(candidate)
        if candidates:
            # To compute the effort without activity matrices that do not have any errors, comment out the this if statement.
            print(candidates)
            print('Number of candidates:', len(candidates))
            # average_efforts.append(eff.average_effort(fault_set, candidates, num_of_components))
            # average_efforts.append(eff.normalized_average_effort(fault_set, candidates, num_of_components))
            average_efforts.append(eff.normalized_average_effort_flatten(fault_set, candidates, num_of_components, probabilities))
            # Reindent until this part. "Best code ever."
    if average_efforts:
        average_wasted_effort = sum(average_efforts) / len(average_efforts)
        effort_dict[class_name] = average_wasted_effort
        print(average_wasted_effort)

ordered = OrderedDict(sorted(effort_dict.items(), key=itemgetter(1), reverse=True))

with open(EFFORT_OUT, 'w', newline='') as csvfile:
    fieldnames = [
        'class',
        'average_wasted_effort'
    ]
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(fieldnames)
    for k, v in ordered.items():
        writer.writerow([k, v])
