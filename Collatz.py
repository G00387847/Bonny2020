# Bonny Chimezie Nwosu

# Writing a program that asked user to input any positive integer
# and outputs the sucessive values of  the following calculation.
# At each step of calculation, the next value will take current value
# If it is even, divide by two and if it is odd 
# Multiply it by three and add one
# The program will end if the current value is one. 

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