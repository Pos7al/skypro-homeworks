import pytest
from string_utils import StringUtils

utils = StringUtils()

"""CAPITALIZE"""
@pytest.mark.parametrize('input_string, expected', [
    ("skypro", "Skypro"),
    ("Skypro", "Skypro"),
    ("", ""),
    ("1skypro", "1skypro"),
    (" skypro", " skypro")
])
def test_capitilize(input_string, expected):
    assert utils.capitilize(input_string) == expected

"""TEST_TRIM"""
@pytest.mark.parametrize('input_string, expected', [
    ("   skypro", "skypro"),
    ("skypro", "skypro"),
    ("   sky pro  ", "sky pro  "),
    ("", ""),
    ("    ", "")
])
def test_trim(input_string, expected):
    assert utils.trim(input_string) == expected

"""TEST_TO_LIST"""
@pytest.mark.parametrize('input_string, delimiter, expected', [
    ("a,b,c,d", ",", ["a", "b", "c", "d"]),
    ("1:2:3", ":", ["1", "2", "3"]),
    ("", ",", []),
    ("a b c d", " ", ["a", "b", "c", "d"]),
    pytest.param(None, ",", [], marks=pytest.mark.xfail(strict=True))
])
def test_to_list(input_string, delimiter, expected):
    assert utils.to_list(input_string, delimiter) == expected

"""TEST_CONTAINS"""
@pytest.mark.parametrize('string, symbol, expected', [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("", "a", False),
    ("12345", "3", True),
    ("SkyPro", "", False)
])
def test_contains(string, symbol, expected):
    assert utils.contains(string, symbol) == expected

"""DELETE_SYMBOL"""
@pytest.mark.parametrize('string, symbol, expected', [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("SkyPro", "Z", "SkyPro"),
    ("", "a", ""),
    ("aaaaa", "a", "")
])
def test_delete_symbol(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected

"""STARTS_WITH"""
@pytest.mark.parametrize('string, symbol, expected', [
    ("SkyPro", "S", True),
    ("SkyPro", "P", False),
    ("", "a", False),
    ("12345", "1", True),
    ("SkyPro", "", True)
])
def test_starts_with(string, symbol, expected):
    assert utils.starts_with(string, symbol) == expected

"""END_WITH"""
@pytest.mark.parametrize('string, symbol, expected', [
    ("SkyPro", "o", True),
    ("SkyPro", "y", False),
    ("", "a", False),
    ("12345", "5", True),
    ("SkyPro", "", True)
])
def test_end_with(string, symbol, expected):
    assert utils.end_with(string, symbol) == expected

"""IS_EMPTY"""
@pytest.mark.parametrize('string, expected', [
    ("", True),
    (" ", True),
    ("SkyPro", False),
    ("   ", True),
    ("Sky Pro", False)
])
def test_is_empty(string, expected):
    assert utils.is_empty(string) == expected

"""LIST_TO_STRING"""
@pytest.mark.parametrize('lst, joiner, expected', [
    ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),
    (["Sky", "Pro"], ", ", "Sky, Pro"),
    (["Sky", "Pro"], "-", "Sky-Pro"),
    ([], ", ", ""),
    ([1], ", ", "1")
])
def test_list_to_string(lst, joiner, expected):
    assert utils.list_to_string(lst, joiner) == expected