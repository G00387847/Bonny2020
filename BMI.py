# Bonny Nwosu
# This program  calculate somebody's Body Mass Index (BMI)
# Using height in centimetres and weight in kilograms
  
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))

height_in_meters = height / 100

bmi = round(weight / height_in_meters**2, 2)

print(bmi)

