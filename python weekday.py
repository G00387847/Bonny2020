# Bonny Chimezie Nwosu
#  Writing a program on Datetime

import datetime

now = datetime.datetime.now()
day = now.weekday
weekend = (5, 7)

# assigning to only detect the weekday attribute
if day == weekend:
    print (" It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday.")