import pytest
from solutions.lists_dicts import *

def test_generate_numbers():
    assert generate_numbers(5) == [1, 2, 3, 4, 5]

def test_generate_squares():
    assert generate_squares(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

def test_merge_lists():
    assert merge_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

def test_multiply_keys():
    assert multiply_keys({'a': 3, 'b': 2}) == ['a', 'a', 'a', 'b', 'b']

def test_list_to_dict():
    assert list_to_dict(['apple', 'banana', 'cherry']) == {'apple': 5, 'banana': 6, 'cherry': 6}

def test_majority_element():
    assert majority_element([3, 3, 4, 2, 4, 4, 2, 4, 4]) == 4

def test_filter_dictionary():
    assert filter_dictionary({'apple': 5, 'banana': 3, 'cherry': 8}, 6) == {'cherry': 8}
