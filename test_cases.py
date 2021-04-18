# pytest will run all files of the form test_*.py or *_test.py
# in the current directory and its subdirectories

import pytest


# checking function returns an expected value
def value_func(val=1):
    return val


def test_answer():
    assert value_func() == 1, "The answer is not as expected"


# checking whether correct exception is raised
def except_func():
    x = 1 / 0  # this would raise ZeroDivisionError


def test_except_func():
    with pytest.raises(ZeroDivisionError):
        except_func()


# checking whether value returned is within some limit
def add_func(n1=0.1, n2=0.2):
    return n1 + n2
    # Executing (0.1+0.2) == 0.3 would return False
    # please check by yourself too.
    # this is due to floating point arithmetic on computers


# @pytest.mark.skip("Skipping the test case")
def test_add_func():
    assert add_func() == 0.3, "this would fail always."


def test_add_func_approx():
    assert add_func() == pytest.approx(
        0.3
    ), "this would succeed as error is within tolerance."


# when test cases need to be evaluated on multiple values,
# you can use mark.parametrize as below.
# The tuples within the list would be passed to the test function one by one.


@pytest.mark.parametrize(
    "inp1, inp2, result",
    [
        (3, 5, 8),
        (5, 5, 10),
        (0.4, 0.3, 0.7),
    ],
)
def test_multiple(inp1, inp2, result):
    assert add_func(inp1, inp2) == result
