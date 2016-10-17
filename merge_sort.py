# coding: utf-8

def merge_sort(buff):
    c = len(buff)

    if c == 1: return buff

    if c == 2:
        if buff[1] >= buff[0]:
            return [buff[0], buff[1]]
        else:
            return [buff[1], buff[0]]

    hc = c // 2

    alst = merge_sort(buff[:hc])
    blst = merge_sort(buff[hc:])

    reslst = []

    ai = 0
    bi = 0

    while True:
        if alst[ai] > blst[bi]:
            reslst.append(blst[bi])
            bi += 1
        else:
            reslst.append(alst[ai])
            ai += 1

        if ai > len(alst) - 1 and len(blst) - 1 >= bi:
            reslst += blst[bi:]
            break
        elif bi > len(blst) - 1 and len(alst) - 1 >= ai:
            reslst += alst[ai:]
            break

    return reslst
