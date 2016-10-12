# coding: utf-8

'''
node: n
parent node: (n + 1) / 2
left child node: 2n + 1
right child node: 2n + 2
'''

def make_heap(buff, end):

    while True:
        maked = True

        for i in range(end):
            n = buff[i]
            c = 2*i + 1

            if c >= end: break

            lcn = buff[c]

            if end > c + 1 and buff[c + 1] >= buff[c] and buff[c + 1] > n:
                c += 1

            if buff[c] > buff[i]:
                t = buff[i]
                buff[i] = buff[c]
                buff[c] = t
                maked = False

        if maked: break

    return buff

def heap_sort(buff):
    buff = make_heap(buff, len(buff))

    begin = 0
    end = len(buff) - 1

    while end >= 0:

        if buff[begin] > buff[end]:
            t = buff[begin]
            buff[begin] = buff[end]
            buff[end] = t

        end -= 1

        buff = make_heap(buff, end)

    return buff
