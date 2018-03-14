#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

import datetime

name = input('What is your name?')
age = input('What is your age?')
now = datetime.datetime.now()
year = now.year + (100 - int(age))

print(name + ', you will have 100 birtday in', year)

#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate 
#message to the user. Hint: how does an even / odd number react differently when divided by 2?
#Extras:
#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
#If check divides evenly into num, tell that to the user. If not, print a different appropriate message

number = int(input('What is your number?'))
check = int(input('What is your second number?'))

if number % 4 == 0:
    print('Multiple of 4')
    print('Odd number')
elif number % 2 == 0:
    print('Odd number')
else:
    print('Even number')

if number % check ==0:
    print(number, 'can be divided by:',check, 'wihtout')

#Take a list, say for example this one:
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.
#Instead of printing the elements one by one, make a new list that has all the elements less than 
#5 from this list in it and print out this new list.
#Write this in one line of Python.
#Ask the user for a number and return a list that contains only elements from the original list a 
#that are smaller than that number given by the user.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newlist = []
for element in a:
    if element <5:
        print(element)
        newlist.append(element)
print(newlist)
number = int(input('What number should I compare the list to?'))
newlist = []
for element in a:
    if element < number:
        newlist.append(element)
print(newlist)

#Create a program that asks the user for a number and then prints out a list of all the divisors of 
#that number. (If you don’t know what a divisor is, it is a number that divides evenly into another 
#number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

number = int(input('What is the number for which I will find devisors?'))

def devisors(a, b):
    if a % b == 0:
        return b

newlist = []
for i in range(1, number + 1):
    newlist.append(devisors(number, i))
    
print(list(filter(None, newlist)))

#Take two lists, say for example these two:
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements that are common between the lists 
#(without duplicates). Make sure your program works on two lists of different sizes.
#Extras:
#Randomly generate two lists to test this
#Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

