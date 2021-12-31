# -----------------------------
# Imports
# -----------------------------
import pytest

# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4

# -----------------------------
# A test function that verifies an exception
# -----------------------------
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0 

    assert 'division by zero' in str(e.value)

     