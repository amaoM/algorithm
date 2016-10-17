# coding: utf-8

def binary_search(target, buff, left, right):
    while True:
        c = (left + right) // 2
        if target == buff[c]:
            return c

        if target > buff[c]:
            r = binary_search(target, buff, c + 1, right)
        else:
            r = binary_search(target, buff, left, c)

        return r
