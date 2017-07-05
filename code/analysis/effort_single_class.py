import os
import re
import subprocess
import csv

import generate as gen
import src.effort.effort as eff
import src.utils as utils
from src.mhs.mhs import MHS
from src.mhs.spectra import Spectra
import src.effort.spectra as s

CWD = os.path.dirname(__file__)
STACCATO = os.path.join(CWD, 'lib/Staccato.macosx.x86_64')
BARINEL = os.path.join(CWD, 'lib/Barinel.macosx.x86_64')
OUT_DIR = os.path.join(CWD, 'output')
MATRICES_DIR = os.path.join(OUT_DIR, 'matrices')
STACCATO_OUT = 'out.staccato'
BARINEL_DIR = os.path.join(OUT_DIR, 'barinel')
EFFORT_OUT = os.path.join(OUT_DIR, 'effort.csv')
SPECTRA_OUT = os.path.join(OUT_DIR, 'spectra')
REPLICATION_OUT = os.path.join(OUT_DIR, 'replication.csv')

with open(REPLICATION_OUT, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['class_name', 'num_of_transactions', 'normalized_density', 'diversity', 'uniqueness', 'ddu', 'average_effort'])

    for class_name in os.listdir(SPECTRA_OUT):
        spec = s.Spectra('output/spectra/%s' % class_name, class_name)
        faults = []
        for i in range(2, spec.num_of_transactions + 1):
            spec.use_first_n_tests(i)

            efforts = []
            effort_dict = {}
            erroneous_matrices_dict = {}

            if not faults:
                faults = gen.generate_class_matrices(class_name, 20, 2, 0, True, spec)
            else:
                gen.generate_class_matrices_given_faults(class_name, faults, 2, 0, True, spec)

            if faults:
                class_dir = os.path.join(MATRICES_DIR, class_name)
                barinel_out = os.path.join(BARINEL_DIR, class_name)
                # print(class_dir)
                if not os.path.exists(barinel_out):
                    os.makedirs(barinel_out)

                for filename in os.listdir(class_dir):
                    filepath = os.path.join(class_dir, filename)
                    # print(filepath)
                    with open(filepath, 'r') as f:
                        columns = len(f.readline().split(' ')[:-1])
                        columns = str(columns)

                    # print('Running Staccato')
                    spectra = Spectra()
                    spectra.read(filepath)

                    mhs = MHS()
                    candidates = mhs(spectra).get_candidates()
                    utils.write_candidates(STACCATO_OUT, candidates)

                    # print('Running Barinel')
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
                erroneous_matrices = []
                include_non_erroneous_matrices = True

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
                    if candidates or include_non_erroneous_matrices:
                        # print('Number of candidates:', len(candidates))
                        # print('Filename:', filename)
                        # print(candidates)
                        erroneous_matrices.append(1 if candidates else 0)
                        # effort = eff.average_effort(fault_set, candidates, num_of_components)
                        # effort = eff.normalized_average_effort(fault_set, candidates, num_of_components)
                        # effort = eff.normalized_average_effort_flatten(fault_set, candidates, num_of_components, probabilities)
                        effort = eff.average_effort_flatten(fault_set, candidates, num_of_components, probabilities)
                        # print('Effort:', effort)
                        average_efforts.append(effort)
                if average_efforts:
                    average_wasted_effort = sum(average_efforts) / len(average_efforts)
                    average_erroneous_matrices = sum(erroneous_matrices) / len(erroneous_matrices)
                    effort_dict[class_name] = average_wasted_effort
                    erroneous_matrices_dict[class_name] = average_erroneous_matrices
                    # print('Effort: %f, erroneous matrices: %f' % (average_wasted_effort, average_erroneous_matrices))
                    efforts.append(average_wasted_effort)
                den = spec.normalized_density()
                div = spec.diversity()
                uni = spec.uniqueness()
                ddu = spec.ddu()
                avg_effort = sum(efforts) / len(efforts)
                writer.writerow([class_name, spec.num_of_transactions, den, div, uni, ddu, avg_effort])
                print('%s,%d,%f,%f,%f,%f,%f' % (class_name, spec.num_of_transactions, den, div, uni, ddu, avg_effort))