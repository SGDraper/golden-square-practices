import pytest
from lib.password_checker import *

def test_under_8():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check('four')
    message = str(e.value)
    assert message == "Invalid password, must be 8+ characters."

def test_8_or_over():
    password = PasswordChecker()
    result = password.check('overeight')
    assert result == True