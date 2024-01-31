from lib.string_builder import StringBuilder

def test_string_builder_empty():
    string_builder = StringBuilder()
    assert string_builder.output() == ""


def test_string_builder_return_size():
    string_builder = StringBuilder()
    string_builder.add("party")
    result = string_builder.size()
    assert result == 5


def test_string_builder_return_string():
    string_builder = StringBuilder()
    string_builder.add("partytime")
    result = string_builder.output()
    assert result == "partytime"