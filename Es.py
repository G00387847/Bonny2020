# Bonny Chimezie Nwosu
# This program reads in text file
# And outputs the number of e's it contains

# Reference - www.sanfoundry.com

num1 = 'e'
num = 0

# filename from an argument on the command line
with open("c:/Users/chimezie/Desktop/moby10b.txt", "r") as fileName:
    for line in fileName:
        words = line.split()
        for i in words:
            for e in i:
                if(e==num1):
                    num = num + 1
print()
print(num)
