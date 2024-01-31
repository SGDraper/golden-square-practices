from lib.gratitudes import *

def test_gratitudes_empty():
    gratitudes = Gratitudes()
    gratitudes.add("")
    result = gratitudes.format()
    assert result == "Be grateful for: "

def test_gratitudes_add_string():
    gratitudes = Gratitudes()
    gratitudes.add('Samuel')
    assert gratitudes.format() == 'Be grateful for: Samuel'