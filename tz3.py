def search_minn(file_name):
    try:
        minn = 0
        file = open(file_name, "r")
        for line in file:
            parts = line.split()
            for i in parts:
                if float(i) <= minn:
                    minn = float(i)
        return minn
    except OSError:
        print("File is too long")
    except OverflowError:
        print("File is too long")
    except SystemError:
        print("There is a system error")


def search_maxn(file_name):
    try:
        maxn = 0
        file = open(file_name, "r")
        for line in file:
            parts = line.split()
            for i in parts:
                if float(i) >= maxn:
                    maxn = float(i)
        return maxn
    except OSError:
        print("File is too long")
    except OverflowError:
        print("File is too long")
    except SystemError:
        print("There is a system error")


def find_sum_of_n(file_name):
    try:
        sum_of_n = 0
        file = open(file_name, "r")
        for line in file:
            parts = line.split()
            print(parts)
            for i in parts:
                sum_of_n += float(i)
        return sum_of_n
    except OSError:
        print("File is too long")
    except OverflowError:
        print("File is too long")
    except SystemError:
        print("There is a system error")


def find_multi(file_name):
    try:
        multi = 1
        file = open(file_name, "r")
        for line in file:
            parts = line.split()
            for i in parts:
                multi *= float(i)
        return multi
    except OSError:
        print("File is too long")
    except OverflowError:
        print("File is too long")
    except SystemError:
        print("There is a system error")
