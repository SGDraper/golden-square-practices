import pytest
from lib.present import *


def test_wrap_then_unwrap():
    present = Present()
    present.wrap(57)
    assert present.unwrap() == 57

def test_unwrap_before_wrap():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    message = str(e.value)
    assert message == 'No contents have been wrapped.'

def test_wrap_wrapped():
    present = Present()
    present.wrap(4)
    with pytest.raises(Exception) as e:
        present.wrap(3)
    message = str(e.value)
    assert message == 'A contents has already been wrapped.'