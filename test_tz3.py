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
    file_test = random_list()
    maxi = max(file_test)
    maxp = search_maxn(file_test)
    assert maxp == maxi


def test_search_minn():
    file_test = random_list()
    mini = max(file_test)
    minp = search_minn(file_test)
    assert minp == mini


def test_find_sum_of_n():
    file_test = random_list()
    file_test_fsum = file_test.split()
    sumi = 0
    for i in file_test_fsum:
        i = float(i)
        sumi += i
    sump = find_sum_of_n(file_test)
    assert sump == sumi


def test_find_multi():
    multi = 1
    file_test = random_list()
    file_for_multi = file_test.split()
    for i in file_for_multi:
        multi *= float(i)
    sump = find_multi(file_test)
    assert sump == multi


def test_is_digits():
    rand_file = random_list()
    digit = search_maxn(rand_file)
    assert type(digit) == float or type(digit) == int
      
