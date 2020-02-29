# Bonny Chimezie Nwosu
#This program reads 
# a students percentage
# and prints out the
# corresponding grade

import random


percentage = float(input("Enter the percentage: "))
#print (percentage)
if percentage < 0 or percentage > 100:

 print ("Please enter a number between 0 and 100")
elif percentage < 40: # we know it is greater than 0
 print ("Fail")
elif percentage < 50: # between 40 and 49
 print ("Pass")
elif percentage < 60: # between 50 and 59 n
 print ("Merit1")
elif percentage < 69.5: # between 60 and 69
 print ("Merit2")
else: # only option left is over 70 and 100
 print("Distinction")