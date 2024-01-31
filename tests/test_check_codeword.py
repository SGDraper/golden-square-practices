from lib.check_codeword import *

def test_check_codeword_correct():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_codeword_close():
    result = check_codeword("hose")
    assert result == "Close, but nope."
    result = check_codeword("house")
    assert result == "Close, but nope."
    result = check_codeword("hole")
    assert result == "Close, but nope."
    result = check_codeword("house")
    assert result == "Close, but nope."
#
def test_check_codeword_incorrect():
    result = check_codeword("duck")
    assert result == "WRONG!"
    result = check_codeword("goose")
    assert result == "WRONG!"
    result = check_codeword("Horse")
    assert result == "WRONG!"
    result = check_codeword("Hose")
    assert result == "WRONG!"