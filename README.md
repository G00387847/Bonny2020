# Problem Sheet

## Programming and Scripting

## Homework Weeekly Task - 2

Write a program that calculates somebody's Body Mass Index (BMI). The inputs are the person's height in centimetres and weight in kilograms. The output is their weight divided by their height in metres squared.

## Solution

Using python programming from this [webpage](https://www.tutorialspoint.com/python-program-to-calculate-bmi-body-mass-index-of-your-body), I found the relevant data to write the code on my repository, couple with my GMIT online learning video recorded lecture.

  
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))

height_in_meters = height / 100

bmi = round(weight / height_in_meters**2, 2)

print(bmi)

## Homework Weekly Task - 3 (SecondString)

Write a program that takes asks a user to input a string and outputs every second letter in reverse order.


## Solution

Using python programming,I used some relevant information from stackflow to write the code in my repo.


num1 = input("Please enter a sentence")

def reverse(num1): 
  str = "" 
  for i in num1: 
    str = i + str
  return str
print(end="")
print(num1[::-2])

## Homework Weekly Task 4 - (Collatz)

Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

## Solution

I used python programming in writing the code to my repository and I got my relavant data from my GMIT online learning recorded lecture and optional lab sheet work


num1 = int(input("Enter any positive integer number: "))
num2 = 2

print (num1)

while num1 > 1:

    if num1 % num2 == 0:
        num1 /= 2
        print (num1)
    
    else:
        num1 = (num1 * 3) + 1
        print (num1)



