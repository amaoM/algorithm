# coding: utf-8

def quick_sort(buff, left, right):
    e = buff[(left + right) // 2]
    l = left
    r = right

    while r >= l:
        while e > buff[l]: l += 1
        while buff[r] > e: r -= 1

        if l >= r: break

        t = buff[r]
        buff[r] = buff[l]
        buff[l] = t

        l += 1
        r -= 1

    if left < l - 1:
        buff = quick_sort(buff, left, l - 1)
    if right > r + 1:
        buff = quick_sort(buff, r + 1, right)

    return buff

def main():
    buff = list(map(int, input().split()))
    quick_sort(buff)

if __name__ == '__main__':
    main()
