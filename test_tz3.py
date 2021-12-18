import pytest

from tz3 import search_maxn, search_minn, find_sum_of_n, find_multi


def test_over_flow_error():
    with pytest.raises(OverflowError) as err:
        print("OverFlowError")


def test_search_maxn(file_name):
    with open(file_name, "r") as f:
        data = []
        full_f = f.read()
        for i in full_f.split():
            data.append(float(i))
    maxi = max(data)
    assert search_maxn(file_name) == maxi


def test_search_minn(file_name):
    with open(file_name, "r") as f:
        data = []
        full_f = f.read()
        for i in full_f.split():
            data.append(float(i))
    mini = max(data)
    assert search_minn(file_name) == mini


def test_find_sum_of_n(file_name):
    with open(file_name, "r") as f:
        data = []
        full_f = f.read()
        for i in full_f.split():
            data.append(float(i))
    sumi = sum(data)
    assert find_sum_of_n(file_name) == sumi


def test_find_multi(file_name):
    multi = 1
    file = open(file_name, "r")
    for line in file:
        parts = line.split()
        for i in parts:
            multi *= float(i)
    assert find_multi(file_name) == multi
