# Bonny Chimezie Nwosu

#  Writing a program that output 
# Whether or not today is a weekday

import datetime

now = datetime.datetime.now()
day = now.weekday
weekend = 7

 #assigning to detect the weekday attribute
if day == weekend:
    print (" It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday.")
