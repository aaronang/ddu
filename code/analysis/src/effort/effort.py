from collections import OrderedDict
from operator import itemgetter


def worst_effort(fault_set, candidates):
    for i in reversed(range(len(candidates))):
        for x in fault_set:
            if x in candidates[i]:
                return i
    return -1


def best_effort(fault_set, candidates):
    for i in range(len(candidates)):
        for x in fault_set:
            if x in candidates[i]:
                return i
    return -1


def average_effort(fault_set, candidates, num_of_components):
    indexes = []
    for i in range(len(candidates)):
        for x in fault_set:
            if x in candidates[i]:
                indexes.append(i)
    if len(indexes) == 0:
        return num_of_components / 2.0
    return float(sum(indexes)) / len(indexes)


def normalized_average_effort(fault_set, candidates, num_of_components):
    effort = average_effort(fault_set, candidates, num_of_components)
    print('Non-normalized effort:', effort)
    return effort / num_of_components


def normalized_average_effort_flatten(fault_set, candidates, num_of_components, probabilities):
    probs = {}
    for index, candidate in enumerate(candidates):
        for component in candidate:
            if component not in probs:
                probs[component] = 0
            probs[component] += probabilities[index]

    ordered = OrderedDict(sorted(probs.items(), key=itemgetter(1), reverse=True))

    cands = [[k] for k, v in ordered.items()]
    # print('Flattened diagnosis:', [[k, v] for k, v in ordered.items()])
    return normalized_average_effort(fault_set, cands, num_of_components)


def average_effort_flatten(fault_set, candidates, num_of_components, probabilities):
    probs = {}
    for index, candidate in enumerate(candidates):
        for component in candidate:
            if component not in probs:
                probs[component] = 0
            probs[component] += probabilities[index]

    ordered = OrderedDict(sorted(probs.items(), key=itemgetter(1), reverse=True))

    cands = [[k] for k, v in ordered.items()]
    # print('Flattened diagnosis:', [[k, v] for k, v in ordered.items()])
    return average_effort(fault_set, cands, num_of_components)


def compute_effort(fault_set, candidates):
    print('Candidates:', candidates)
    print('Fault set:', fault_set)
    print('Best:', best_effort(fault_set, candidates))
    print('Worst:', worst_effort(fault_set, candidates))
    print('Average:', average_effort(fault_set, candidates))
    print()

    return
