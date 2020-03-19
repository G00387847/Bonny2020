# Bonny Chimezie Nwosu
# This program reads in text file
# And outputs the number of e's it contains

# Source code - sanfoundry.com

num1 = 'e'
num = 0

with open("c:/Users/chimezie/Desktop/moby10b.txt", "r") as fileName:
    for line in fileNme:
        words = line.split()
        for i in words:
            for e in i:
                if(e==num1):
                    num = num + 1
print()
print(num)
