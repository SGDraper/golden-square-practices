from lib.report_length import *

def test_report_length_one():
    result = report_length("a")
    assert result == "This string was 1 characters long."

def test_report_length_two():
    result = report_length("as")
    assert result == "This string was 2 characters long."

def test_report_length_three():
    result = report_length("ass")
    assert result == "This string was 3 characters long."

def test_report_length_four():
    result = report_length("four")
    assert result == "This string was 4 characters long."

def test_report_length_five():
    result = report_length("coder")
    assert result == "This string was 5 characters long."