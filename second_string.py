# Bonny Nwosu
# This program takes asks a user to input a string
# And output every second letter in reverse order.
# Using Loop

num1 = input("Please enter a sentence")

def reverse(num1): 
  str = "" 
  for i in num1: 
    str = i + str
  return str
print(end="")
print(num1[::-2])
