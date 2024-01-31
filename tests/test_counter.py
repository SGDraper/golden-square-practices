from lib.counter import *

def test_counter_positive():
    counter = Counter()
    counter.add(3)
    result = counter.report()
    assert result == "Counted to 3 so far."

def test_counter_negative():
    counter = Counter()
    counter.add(-3)
    result = counter.report()
    assert result == "Counted to -3 so far."

def test_counter_multiple_numbers():
    counter = Counter()
    counter.add(3)
    counter.add(4)
    result = counter.report()
    assert result == "Counted to 7 so far."