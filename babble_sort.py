# coding: utf-8

def babble_sort(buff):

    while True:
        changed_count = 0

        for i in range(len(buff) - 1):
            if buff[i] > buff[i+1]:
                t = buff[i]
                buff[i] = buff[i+1]
                buff[i+1] = t
                changed_count += 1

        if changed_count == 0:
            return buff

def main():
    buff = list(map(int, input().split()))
    print(babble_sort(buff))

if __name__ == '__main__':
    main()
