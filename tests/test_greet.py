from lib.greet import *

def test_greet_samuel():
    result = greet("Samuel")
    assert result == "Hello, Samuel!"
