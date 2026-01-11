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

import pytest
from src.parser import ParseError


def test_empty_input_error():
    try:
        parse_numbers("")
        assert False, "空输入应该抛出错误"
    except ParseError:
        assert True


def test_invalid_token_error():
    try:
        parse_numbers("abc+1")
        assert False, "非法字符应该抛出错误"
    except ParseError:
        assert True
