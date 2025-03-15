def height_to_meters(feet: int, inches: int):
    return ((feet*12) + inches) * 0.025 # metric covnersion factor for meters

def pounds_to_kg(pounds):
    return pounds *0.45 # metric conversion factor for kilograms


def bmicalculator(height, weight: float):
    height = height * height # square height in meters
    return weight / height

    
def get_user_input():
    feet = input("What's the height in feet?")
    inches = input("And inches?")
    pounds = input("What's the weight in pounds?")
    return int(feet), int(inches), float(pounds)

def calculator():
    feet, inches, pounds = get_user_input()
    kg = pounds_to_kg(pounds)
    height = height_to_meters(feet, inches) # in meters

