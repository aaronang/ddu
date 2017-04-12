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


def compute_effort(fault_set, candidates):
    print('Candidates:', candidates)
    print('Fault set:', fault_set)
    print('Best:', best_effort(fault_set, candidates))
    print('Worst:', worst_effort(fault_set, candidates))
    print('Average:', average_effort(fault_set, candidates))
    print()

    return
