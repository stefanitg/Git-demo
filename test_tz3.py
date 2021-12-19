import random

from tz3 import search_maxn, search_minn, find_sum_of_n, find_multi


def random_list():
    file = []
    k = random.randint(0, 1025)
    for i in range(0, k - 1):
        n = random.uniform(-1048567, 1048576)
        file.append(n)
    file_1 = " ".join(map(str, file))
    return file_1


def test_search_maxn():
    file_name = random_list()
    maxi = max(file_name)
    assert search_maxn(file_name) == maxi


def test_search_minn():
    file_name = random_list()
    mini = max(file_name)
    assert search_minn(file_name) == mini


def test_find_sum_of_n():
    file_name = random_list()
    sumi = sum(file_name)
    assert find_sum_of_n(file_name) == sumi


def test_find_multi():
    multi = 1
    file_name = random_list()
    for i in file_name:
        multi *= float(i)
    assert find_multi(file_name) == multi
