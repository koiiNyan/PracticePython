#TODO
#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year 
#that they will turn 100 years old.

name = input("Enter your name, please: ")
age = int(input("Enter your age, please: "))
cur_year = int(input("Current year: "))
year = (cur_year - age) + 100 

print("Hi {}! You will be 100 y.o. in {}".format(name, year))

#Extras:
#
#Add on to the previous program by asking the user for another number 
#and printing out that many copies of the previous message. 
lines = int(input("How many times do you want the reply message to be written?"))
#
#Print out that many copies of the previous message on separate lines. 

print(("Hi " + name + "!" + " You will be 100 y.o. in " + str(year) + '\n')* lines)