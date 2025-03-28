def get_user_input():
    feet = input("What's the height in feet? ")
    inches = input("And inches? ")
    pounds = input("What's the weight in pounds? ")
    return float(feet), float(inches), float(pounds)

def height_to_meters(feet: float, inches: float):
    return ((feet*12) + inches) * 0.025 # metric covnersion factor for meters

def pounds_to_kg(pounds):
    return pounds *0.45 # metric conversion factor for kilograms

def bmicalculator(height, weight: float):
    height = height * height # square height in METERS
    bmi = weight / height #BMI Formula: KILOGRAMS div by squared height
    # decimal precision
    bmi_decimal = float("{:.1f}".format(bmi))
    return bmi_decimal 

def categorycalculator(bmi):
    category = ""
    match bmi:
        case _ if bmi < 18.5:
            category = "Underweight"
    
        case _ if bmi >= 18.5 and bmi <= 24.9:
            category = "Normal weight"
        
        case _ if bmi > 25 and bmi < 29.9:
            category = "Overweight"

        case _ if bmi >= 30:
            category = "Obese"
    return category

def print_results(bmi, category):
    print("BMI: " + str(bmi) + " Category: "+ category)


# Gather data and calculate using that data

feet, inches, pounds = get_user_input()
kg = pounds_to_kg(pounds)
height = height_to_meters(feet, inches) # in meters
bmi = bmicalculator(height, kg)
category = categorycalculator(bmi)

# Print results
print_results(bmi, category)


