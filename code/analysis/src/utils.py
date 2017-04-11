import json


def pp(data):
    print(json.dumps(data, indent=4))


def write_candidates(out, candidates):
    with open(out, 'w') as f:
        for c in candidates:
            f.write(c + '\n')