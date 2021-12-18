def search_minn(file_name):
    minn = 0
    file = open(file_name, "r")
    for line in file:
        parts = line.split()
        for i in parts:
            if float(i) <= minn:
                minn = float(i)
    return minn


def search_maxn(file_name):
    maxn = 0
    file = open(file_name, "r")
    for line in file:
        parts = line.split()
        for i in parts:
            if float(i) >= maxn:
                maxn = float(i)
    return maxn


def find_sum_of_n(file_name):
    sum_of_n = 0
    file = open(file_name, "r")
    for line in file:
        parts = line.split()
        print(parts)
        for i in parts:
            sum_of_n += float(i)
    return sum_of_n


def find_multi(file_name):
    multi = 1
    file = open(file_name, "r")
    for line in file:
        parts = line.split()
        for i in parts:
            multi *= float(i)
    return multi
