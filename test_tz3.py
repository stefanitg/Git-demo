import pytest
import random

from tz3 import search_maxn, search_minn, find_sum_of_n, find_multi


def random_list():
    file = []
    k = random.randint(0, 1025)
    for i in range(0, k - 1):
        n = random.uniform(-1048567, 1048576)
        file.append(n)
    return file


def test_over_flow_error():
    with pytest.raises(OverflowError) as err:
        print("OverFlowError")


def test_search_maxn():
    file_test = random_list()
    maxi = max(file_test)
    assert search_maxn(file_test) == maxi


def test_search_minn():
    file_test = random_list()
    mini = max(file_test)
    assert search_minn(file_test) == mini


def test_find_sum_of_n():
    file_test = random_list()
    sumi = sum(file_test)
    assert find_sum_of_n(file_test) == sumi


def test_find_multi():
    multi = 1
    file_test = random_list()
    for i in file_test:
        multi *= float(i)
    assert find_multi(file_test) == multi

