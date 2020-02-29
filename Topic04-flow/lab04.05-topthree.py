# This program generates 10 random numbers.
# prints them out, then
# prints out the top 3
# using a list to store and
# manipulate the numbers

import random
# programming the general case
num1 = 10
num2 = 3
sum1 = 0
sum2 = 100
numbers = []
for i in range(0,10):
 numbers.append(random.randint(sum1,sum2))
print ("{} random numbers\t {}".format(num1,numbers))

# Sorts from https://stackoverflow.com/q/32296887
topOnes = numbers.copy()
topOnes.sort(reverse = True)
print("The top {} are \t\t {}".format(num2,topOnes[0:num2]))