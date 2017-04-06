import os
import re
import subprocess

import src.effort as eff

CLASSNAME = 'com.google.inject.PrivateModule'

CWD = os.path.dirname(__file__)
STACCATO = os.path.join(CWD, 'lib/Staccato.macosx.x86_64')
BARINEL = os.path.join(CWD, 'lib/Barinel.macosx.x86_64')
OUT_DIR = os.path.join(CWD, 'out')
MATRICES_DIR = os.path.join(OUT_DIR, 'matrices')
CLASS_DIR = os.path.join(MATRICES_DIR, CLASSNAME)
STACCATO_OUT = 'out.staccato'
BARINEL_DIR = os.path.join(OUT_DIR, 'barinel')
BARINEL_OUT = os.path.join(BARINEL_DIR, CLASSNAME)

if not os.path.exists(BARINEL_OUT):
    os.makedirs(BARINEL_OUT)

for filename in os.listdir(CLASS_DIR):
    filepath = os.path.join(CLASS_DIR, filename)

    with open(filepath, 'r') as f:
        columns = len(f.readline().split(' ')[:-1])
        columns = str(columns)

    staccato = subprocess.Popen([STACCATO, columns, filepath, STACCATO_OUT])
    staccato.wait()

    barinel_output = os.path.join(BARINEL_OUT, filename)
    barinel = subprocess.Popen([BARINEL, columns, filepath, STACCATO_OUT, barinel_output])
    barinel.wait()

    os.remove(STACCATO_OUT)


def _get_fault_set(filename):
    base = os.path.basename(filename)
    fault_set = os.path.splitext(base)[0].split('_')
    return list(map(int, fault_set))

average_efforts = []
for filename in os.listdir(BARINEL_OUT):
    filepath = os.path.join(BARINEL_OUT, filename)
    fault_set = _get_fault_set(filename)
    candidates = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            candidate = re.sub('  .*', '', line)
            candidate = re.sub('[{,}]', '', candidate)
            candidate = candidate.split(' ')
            candidate = list(map(lambda x: int(x) - 1, candidate))
            candidates.append(candidate)
    eff.compute_effort(fault_set, candidates)
    average_efforts.append(eff.average_effort(fault_set, candidates))

print('Average wasted effort:', sum(average_efforts) / len(average_efforts))
