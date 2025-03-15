import pytest
from calculator import calculator, height_to_inches

def test_normal_bmi():
    assert calculator(63, 125) == "BMI: 22.7 Category: Normal"

def test_underweight_bmi():

def test_overweight_bmi():

def test_obese_bmi():
