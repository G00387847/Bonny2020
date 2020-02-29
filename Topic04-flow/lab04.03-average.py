#Bonny Chimezie Nwosu
# This program reads numbers until
# the user enters 0
# it will then print back out again
# the average
numbers = []
# we check if it is 0 in the while loop
number = int(input("enter number (0 to quit): "))
while number != 0:
 numbers.append(number)
 # we read the next number and check if 0
 number = int(input("enter another (0 to quit): "))
for value in numbers:
 print (value)
# The average to be a float
average = float(sum(numbers)) / len(numbers)
print ("The average is {}".format(average))