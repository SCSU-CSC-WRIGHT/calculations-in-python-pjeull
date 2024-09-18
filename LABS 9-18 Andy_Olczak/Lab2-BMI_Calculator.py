import math

min_bmi = 18.5
max_bmi = 24.9
weight = input("Please insert your weight in kilograms: ")
height = input("Please insert your height in meters: ")

bmi = (int(weight)/(float(height)**2))

print(f"Your BMI is {bmi:.2f}")

if bmi < min_bmi:
    print("Your BMI is below the healthy range of 18.5 - 24.9.")
elif bmi > max_bmi:
    print("Your BMI is above the healthy range of 18.5 - 24.9.")
else:
    print("Your BMI is in the healthy range of 18.5 - 24.9.")