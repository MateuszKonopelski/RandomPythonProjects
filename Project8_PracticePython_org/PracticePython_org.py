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

