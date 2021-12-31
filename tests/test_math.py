# -----------------------------
# Imports
# -----------------------------
import pytest

# content of test_sample.py


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5

# -----------------------------
# A test function that verifies an exception
# -----------------------------


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)

# -----------------------------
# Parameterized test cases
# -----------------------------

# 1 tupple per
    # Equivalence class


products = [
    (2, 4, 8),            # positive interger
    (1, 44, 44),          # entity
    (0, 44, 0),           # zero
    (4, -4, -16),         # positive by negative
    (-4, -4, 16),         # negative by negavite
    (2.5, 6.7, 16.75)      # floats
]

# python decoration
@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a,b, product):
    assert a * b == product 