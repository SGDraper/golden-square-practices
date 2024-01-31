from lib.high_value import *

def tests_highest_value_first():
    tests_high_value_one = HighValue(2,1)
    assert tests_high_value_one.get_highest() == "First value is higher"
    tests_high_value_one = HighValue(1,-2)
    assert tests_high_value_one.get_highest() == "First value is higher"

def tests_highest_value_second():
    tests_high_value_two = HighValue(1, 2)
    assert tests_high_value_two.get_highest() == "Second value is higher"
    tests_high_value_two = HighValue(-2, 1)
    assert tests_high_value_two.get_highest() == "Second value is higher"

def tests_equal_values():
    tests_high_value_equal = HighValue(1, 1)
    assert tests_high_value_equal.get_highest() == "Values are equal"
    tests_high_value_equal = HighValue(-1, -1)
    assert tests_high_value_equal.get_highest() == "Values are equal"

def tests_add_function_first():
    tests_add_first = HighValue(1, 1)
    tests_add_first.add(1, "first")
    assert tests_add_first.value_first == 2
    tests_add_first = HighValue(1, 1)
    tests_add_first.add(-2, "first")
    assert f"The value is {tests_add_first.value_first}" == "The value is -1"

def tests_add_function_second():
    tests_add_second = HighValue(1, 1)
    tests_add_second.add(1, "second")
    assert tests_add_second.value_second == 2
    tests_add_second = HighValue(1, 1)
    tests_add_second.add(-1, "second")
    assert f"The value is {tests_add_second.value_second}" == "The value is 0"