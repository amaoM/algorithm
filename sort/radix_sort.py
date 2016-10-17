# coding: utf-8

def radix_sort(buff, p, res_buff = []):

    bucket_buff = [[] for _ in range(10)]

    for i in buff:
        if p > len(str(i)):
            res_buff.append(i)
        else:
            bucket_buff[int(str(i)[-p])].append(i)

    temp_buff = []

    for b in bucket_buff:
        temp_buff += b

    if len(temp_buff) == 0:
        return res_buff

    return radix_sort(temp_buff, p + 1, res_buff)
