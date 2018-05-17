#TODO:
#
#Ask the user for a number. Depending on whether the number is even or odd, 
#print out an appropriate message to the user.
#
#Extras:
#
#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) 
#and one number to divide by (check). 
#If check divides evenly into num, tell that to the user. 
#If not, print a different appropriate message.


num = int(input("Enter the number: "))
check = int(input("Enter the 2nd number: "))

if num % 4 == 0:
    print("{} is a multiple of 4".format(num))

elif num % 2 == 0:
    print("{} is even!".format(num))

else:
    print("{} is odd!".format(num))


if num % check == 0:
    print("{} divides by {} without a remainder!".format(num, check))

else:
    print("{} can't be divided by {} without a remainder!".format(num, check))

