from src.parser import parse_numbers
from src.calculator import calculate_sum


def test_simple_addition():
    numbers = parse_numbers("1+2+3")
    result = calculate_sum(numbers)
    assert result == 6


def test_float_numbers():
    numbers = parse_numbers("1.5+2.5")
    result = calculate_sum(numbers)
    assert result == 4.0
