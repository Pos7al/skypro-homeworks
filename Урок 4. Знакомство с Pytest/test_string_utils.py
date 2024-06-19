import pytest
from string_utils import StringUtils

utils = StringUtils()

def test_capitilize():
    assert utils.capitilize("skypro") == "Skypro"
    assert utils.capitilize("Skypro") == "Skypro"
    assert utils.capitilize("") == ""
    assert utils.capitilize("1skypro") == "1skypro"
    assert utils.capitilize(" skypro") == " skypro"

def test_trim():
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("skypro") == "skypro"
    assert utils.trim("   sky pro  ") == "sky pro  "
    assert utils.trim("") == ""
    assert utils.trim("    ") == ""

def test_to_list():
    assert utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert utils.to_list("1:2:3", ":") == ["1", "2", "3"]
    assert utils.to_list("") == []
    assert utils.to_list("a b c d", " ") == ["a", "b", "c", "d"]
    assert utils.to_list(None) == []

def test_contains():
    assert utils.contains("SkyPro", "S") == True
    assert utils.contains("SkyPro", "U") == False
    assert utils.contains("", "a") == False
    assert utils.contains("12345", "3") == True
    assert utils.contains("SkyPro", "") == False

def test_delete_symbol():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"
    assert utils.delete_symbol("SkyPro", "Z") == "SkyPro"
    assert utils.delete_symbol("", "a") == ""
    assert utils.delete_symbol("aaaaa", "a") == ""

def test_starts_with():
    assert utils.starts_with("SkyPro", "S") == True
    assert utils.starts_with("SkyPro", "P") == False
    assert utils.starts_with("", "a") == False
    assert utils.starts_with("12345", "1") == True
    assert utils.starts_with("SkyPro", "") == True

def test_end_with():
    assert utils.end_with("SkyPro", "o") == True
    assert utils.end_with("SkyPro", "y") == False
    assert utils.end_with("", "a") == False
    assert utils.end_with("12345", "5") == True
    assert utils.end_with("SkyPro", "") == True

def test_is_empty():
    assert utils.is_empty("") == True
    assert utils.is_empty(" ") == True
    assert utils.is_empty("SkyPro") == False
    assert utils.is_empty("   ") == True
    assert utils.is_empty("Sky Pro") == False

def test_list_to_string():
    assert utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
    assert utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
    assert utils.list_to_string([]) == ""
    assert utils.list_to_string([1]) == "1"
