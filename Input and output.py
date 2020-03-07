# Bonny Chimezie Nwosu
# This program reads in text file
# And outputs the number of e's it contains

# Source code - sanfoundry.com
#fname = input("Enter file name:")
I = 'e'  #input("Enter letter to be searched:")
num = 0

with open("c:/Users/chimezie/Desktop/moby10b.txt", "r") as f:
    for line in f:
        words = line.split()
        for i in words:
            for e in i:
                if(e==I):
                    num = num + 1
print()
print(num)
