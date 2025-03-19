def get_user_input():
    feet = input("What's the height in feet? ")
    inches = input("And inches? ")
    pounds = input("What's the weight in pounds? ")
    return int(feet), int(inches), float(pounds)

def height_to_meters(feet: int, inches: int):
    return
    # return ((feet*12) + inches) * 0.025 # metric covnersion factor for meters

def pounds_to_kg(pounds):
    return
    # return pounds *0.45 # metric conversion factor for kilograms

def bmicalculator(height, weight: float):
    height = height * height # square height in meters
    bmi = weight / height #BMI Formula: kg div by squared height
    # decimal precision
    bmi_decimal = float("{:.2f}".format(bmi))
    return #bmi_decimal 

def categorycalculator(bmi):
    # match bmi:
    #     case _ if bmi < 18.5:
    
    #     case _ if bmi < 18.5:
        
    #     case _ if bmi < 18.5:

    #     case _ if bmi < 18.5:
    return

def print_results(bmi, category):
    print("BMI: " + bmi)


# Gather data and calculate using that data

feet, inches, pounds = get_user_input()
kg = pounds_to_kg(pounds)
height = height_to_meters(feet, inches) # in meters
bmi = bmicalculator(height, kg)
category = categorycalculator(bmi)

# Print results
print_results(bmi, category)


