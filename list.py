#TODO:
#
#write a program that prints out all the elements of the list 
#that are less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
    if i < 5:
        print (i)




#Extras:
#
#1. make a new list that has all the elements less than 5 from this list 
#in it and print out this new list.
b = []
#2. Write this in one line of Python.
for i in a:
    if i <5:
        b.append(i)

print(b)
#3. Ask the user for a number and return a list that contains 
#only elements from the original list a that are smaller than 
#that number given by the user.
x = int(input('Enter a number: '))
for c in a:
    if c < x:
        print(c)