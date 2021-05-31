from random import randint
from time import sleep

c  = open("nationality", "r")
n = open("f_name" , "r") 

nations = c.readlines() # nations with \n
names = n.readlines()

#print(nations[randint(0,8)][0:-1]) # random nation
#print(names[randint(0,104)][0:-1]) # random name




class Passport: # This is virtually the whole game
    def __init__(self, nationality, gender, name, day, month, year, discrepant, permitted):
        self.nationality = nationality
        self.gender = gender    
        self.name = name
        self.day = day # Expiry dates
        self.month = month
        self.year = year
        self.discrepant = discrepant
        #self.permitted = permitted
    
#    def check(self):
#        if self.discrepant == True and self.permitted == True:
#            self.mistake += 1
#        elif self.discrepant == False and self.permitted == False:
#           self.mistake += 1
#       else:
#            pass

print("WELCOME TO TEKKEN BORDER CUSTOMS, OTHERWISE KNOWN AS PLAPERS PEASE.\nYOUR JOB IS SIMPLE: PERMIT THOSE WHOSE PASSPORTS AREN'T EXPIRED IN AND REJECT THE ONES WHOSE ARE\nFOR THE BENEFIT OF TEKKUO!")

while True:
    
    gender = ""
    if randint(0,1) == 0 : 
        gender = "F" 
    else: 
        gender = "M"

    f_name = names[randint(0,104)][0:-1] + " " + names[randint(0,104)][0:-1]

    expired_by = randint(0,11)
    day = 10
    month = 11
    year = 1980
    if expired_by == 0:
        day -= randint(1,11)
    elif expired_by == 1:
        month -= randint(1,5)
    elif expired_by == 2:
        year -= randint(1,2)
    elif expired_by == 3:
        day += randint(1,11)
    elif expired_by == 4:
        month += randint(1,5)
    elif expired_by == 5:
        year += randint(1,2)

    discrepant = False

    if expired_by == 0 or expired_by == 1 or expired_by == 2:
        discrepant = True
    elif expired_by == 3 or expired_by == 4 or expired_by == 5:
        discrepant = False
    else:
        discrepant = False

    person = Passport(nations[randint(0,8)][0:-1] , gender , f_name, day, month, year, discrepant, " ")

    print(person.nationality + "\n" + person.gender + "\n" + person.name + "\n" + str(person.year) + "." + str(person.month) + "." + str(person.day))

    allow = input("ALLOW? Y/N ")

    if allow == "Y":
        if person.discrepant == True:
            print("---\nWRONG\n---")
        elif person.discrepant == False:
            print("---\nCORRECT\n---")
    elif allow == "N":
        if person.discrepant == True:
            print("---\nCORRECT\n---")
        elif person.discrepant == False:
            print("---\nWRONG\n---")


c.close()
n.close()