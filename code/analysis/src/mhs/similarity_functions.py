import math


def ochiai(n):
    res = math.sqrt(n[1][1] + n[0][1]) * math.sqrt(n[1][1] + n[1][0])
    if res == 0.0:
        return 0.0
    else:
        return n[1][1] / res
