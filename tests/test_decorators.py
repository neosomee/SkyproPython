import pytest
from src.decorators import log

@log()
def add(a, b):
    return a + b

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

def test_add_non_numeric():
    with pytest.raises(TypeError):
        add("a", 2)

def test_add_large_numbers():
    assert add(1000000, 2000000) == 3000000

def test_add_negative_numbers():
    assert add(-1, -2) == -3

def test_log_to_file_error(tmp_path):
    filename = tmp_path / "log.txt"

    @log(filename=str(filename))
    def add(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        add(10, 0)

    with open(filename, 'r') as f:
        log_content = f.read()
        assert "Function 'add' started with args: (10, 0), kwargs: {}" in log_content
        assert "Function 'add' raised an exception: ZeroDivisionError with args: (10, 0), kwargs: {}" in log_content
