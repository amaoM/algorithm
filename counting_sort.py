# coding: utf-8

def counting_sort(buff):
    cl = [0 for _ in range(max(buff) + 1)]

    for i in buff:
        cl[i] += 1

    res = []

    for k, i in enumerate(cl):
        res += [k] * i

    return res
