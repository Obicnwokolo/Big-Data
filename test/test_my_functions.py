import pytest

# Functions to be tested
def add(number_one, number_two):
    return number_one + number_two

def divide(number_one, number_two):
    if number_two == 0:
        raise ValueError("Cannot divide by zero")
    return number_one / number_two


# Test cases using pytest
def test_add():
    # Test adding two positive numbers
    assert add(2, 3) == 5
    
    # Test adding a positive and a negative number
    assert add(5, -3) == 2
    
    # Test adding two negative numbers
    assert add(-2, -3) == -5
    
    # Test adding zero to a number
    assert add(0, 4) == 4
    
    # Test adding two zeros
    assert add(0, 0) == 0


def test_divide():
    # Test dividing two positive numbers
    assert divide(10, 2) == 5
    
    # Test dividing a positive number by a negative number
    assert divide(10, -2) == -5
    
    # Test dividing two negative numbers
    assert divide(-10, -2) == 5
    
    # Test dividing by 1 (should return the number itself)
    assert divide(7, 1) == 7
    
    # Test dividing by a number greater than the dividend (should return less than 1)
    assert divide(5, 10) == 0.5
    
    # Test dividing by 0 (should raise ValueError)
    with pytest.raises(ValueError):
        divide(10, 0)
