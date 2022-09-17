"""
This is the first hands-on session of our workshop. The goal is to get your development
setup up to speed, so that you can participate in the workshop. You'll also write your first
property-based test.
"""
from typing import TypeVar

import pytest
from hypothesis import given, strategies as st

# Exercise 1: Run the following test
@given(
  st.one_of(
      st.lists(st.integers(), min_size=1),
      st.lists(st.floats(allow_nan=False), min_size=1),
    )
)
def test_max_returns_max(values):
    assert max(values) == sorted(values)[-1]



# Exercise 2: Open a Python shell. Inspect the values generated by st.lists(st.integers()) by using the .example() method of strategies. Invoke .example() several times.
# >>> import hypothesis.strategies as st
# >>> lists_of_int = st.lists(st.integers())
# >>> lists_of_int.example()
# []
# >>> lists_of_int.example()
# [0]
# ...



# Exercise 3: Replace the tests of the "square" function with one or more Hypothesis tests.
# Use the "integers" strategy to ask Hypothesis for random integer values.
# See https://hypothesis.readthedocs.io/en/latest/data.html#hypothesis.strategies.integers
def square(i: int) -> int:
    return i*i


@pytest.mark.skip
def test_square_positive_number():
    number = 42
    result = square(number)
    assert result == 1764


@pytest.mark.skip
def test_square_negative_number():
    number = -5
    result = square(number)
    assert result == 25


@pytest.mark.skip
def test_square_zero():
    number = 0
    result = square(number)
    assert result == 0


def test_square():
    pytest.skip()  # Remove this
    # Your code goes here



# Bonus exercise 1: The square function supports floating point numbers in addition to integers. Extend the Hypothesis tests accordingly-
# Hint: Use the "one_of" strategy to combine strategies
# See https://hypothesis.readthedocs.io/en/latest/data.html#hypothesis.strategies.one_of
T = TypeVar("T", int, float)

def square2(i: T) -> T:
    return i*i

def test_square2():
    pytest.skip()  # Remove this
    # Your code goes here



# Bonus exercise 2: Extend square to support fractions in addition to integers and floats. Extend the Hypothesis tests accordingly.
# Hint: Use the "fractions" strategy to ask Hypothesis for random fractions.
# see https://hypothesis.readthedocs.io/en/latest/data.html#hypothesis.strategies.fractions
