# A Program that reads students
# until the user enters a blank
# and then prints them out 
students = []
firstname = input("enter firstname (blank to quit): ").strip()
while firstname != "":
 student = {}
 student["firstname"] = firstname
 lastname = input("enter lastname: ").strip()
 student["lastname"] = lastname
 students.append(student)
 # next student firstname and lastname
 firstname = input("enter firstname of next (blank to quit): ").strip()
print ("here are the students you entered:")
for currentStudent in students:
 print ("{} {}".format(currentStudent["firstname"],
currentStudent["lastname"]))