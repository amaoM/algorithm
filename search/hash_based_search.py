# coding: utf-8

def hash_based_search(t, s, input_data):
    kv_list = [None for _ in range(s)]

    for d in input_data:
        h = d % s

        if kv_list[h] is None:
            kv_list[h] = []
        kv_list[h].append(d)

    th = t % s

    for i in kv_list[th]:
        if i == t:
            return True

    return False
