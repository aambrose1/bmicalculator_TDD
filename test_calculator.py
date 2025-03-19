import pytest
from calculator import get_user_input, height_to_meters#, pounds_to_kg, bmicalculator, categorycalculator, print_results

def test_user_input(monkeypatch): # monekypatch needed for i/o
    ft = 5.0
    inches = 3.0
    lbs = 125.0

    input_values = iter([ft, inches, lbs])
    monkeypatch.setattr('builtins.input', lambda _: next(input_values))
    result = get_user_input()
    assert result == (5.0, 3.0, 125.0)

def test_height_to_meters():
    result = height_to_meters(5.0,3.0)
    assert result == 1.5750000000000002

# def test_pounds_to_kg():
#     assert pounds_to_kg() == "test"

# def test_bmicalculator():
#     assert bmicalculator() == "test"

# def test_categorycalculator():
#     assert categorycalculator == "tes"

# def test_print_results():
#     assert print_results == "test"