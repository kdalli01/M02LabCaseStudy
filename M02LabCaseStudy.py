#Kayla Allinger

#M02LabCaseStudy

#This app will accept the input of student first and last names and compare
#against variables for the Dean's List and Honor Roll to see if the student
#qualifies

 

HonorRoll = 3.25

DeansList = 3.5

while True:

    StLastName = input("Please enter student last name: ")

    if StLastName == 'zzz':

        break

    StFirstName = input("Please enter student first name: ")

    GPA = float(input("Please enter GPA: "))

    if HonorRoll <= GPA < DeansList:

        print(StFirstName + " " + StLastName + " has made the Honor Roll.")

    elif GPA >= DeansList:

        print(StFirstName + " " + StLastName + " has made the Deans List.")