#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

import datetime

name = input('What is your name?')
age = input('What is your age?')
now = datetime.datetime.now()
year = now.year + (100 - int(age))

print(name + ', you will have 100 birtday in', year)

