# Problem Sheet

## Programming and Scripting

## Homework Weeekly Task - 2

Write a program that calculates somebody's Body Mass Index (BMI). The inputs are the person's height in centimetres and weight in kilograms. The output is their weight divided by their height in metres squared.

# Solution

Using this [webpage](https://www.tutorialspoint.com/python-program-to-calculate-bmi-body-mass-index-of-your-body), I found the relevant data to write the code on my repository, couple with my GMIT online learning video recorded lecture.

# Bonny Nwosu
# This program  calculate somebody's Body Mass Index (BMI)
# Using height in centimetres and weight in kilograms
  
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))

height_in_meters = height / 100

bmi = round(weight / height_in_meters**2, 2)

print(bmi)
