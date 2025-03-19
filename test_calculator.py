import pytest
from calculator import get_user_input, height_to_meters, pounds_to_kg, bmicalculator, categorycalculator, print_results

def test_user_input(monkeypatch): # monekypatch needed for i/o
    ft = 5
    inches = 3
    lbs = 125.0

    input_values = iter([ft, inches, lbs])
    monkeypatch.setattr('builtins.input', lambda _: next(input_values))
    result = get_user_input()
    assert result == (5, 3, 125.0)

def test_height_to_meters():
    assert height_to_meters() == "test"

def test_pounds_to_kg():
    assert pounds_to_kg() == "test"

def test_bmicalculator():
    assert bmicalculator() == "test"

def test_categorycalculator():
    assert categorycalculator == "tes"

def test_print_results():
    assert print_results == "test"