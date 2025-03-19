import pytest
from calculator import get_user_input, height_to_meters, pounds_to_kg, bmicalculator, categorycalculator#, print_results

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

def test_pounds_to_kg():
    test_val = 125
    assert pounds_to_kg(test_val) == 56.25

def test_bmicalculator():
    meters = 1.5750000000000002
    kg = 56.25
    assert bmicalculator(meters, kg) == 22.7

def test_NORMAL_categorycalculator():
    assert categorycalculator(22.7) == "Normal weight"

def test_UNDER_categorycalculator():
    assert categorycalculator(18.4) == "Underweight"

def test_OVER_categorycalculator():
    assert categorycalculator(28) == "Overweight"

def test_OBESE_categorycalculator():
    assert categorycalculator(50) == "Obese"

#BOUNDARY TESTS
def test_bounds_LOW_categorycalculator():
    assert categorycalculator(18.5) == "Normal weight"

def test_bounds_MID_categorycalculator():
    assert categorycalculator(24.9) == "Normal weight"

def test_bounds_HIGH_categorycalculator():
    assert categorycalculator(30) == "Obese"


# def test_print_results():
#     assert print_results == "test"