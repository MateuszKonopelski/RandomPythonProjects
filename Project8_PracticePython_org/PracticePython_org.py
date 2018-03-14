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


import random

a = [random.randrange(1, 1000) for x in range(100)]
b = [random.randrange(1, 1000) for x in range(100)]
newlist = list(set([x for x in a if x in b]))
print(newlist)

#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string 
#that reads the same forwards and backwards.)

string = input('String to test')

if string.lower() == string[::-1].lower():
    print('It is palindrome')
else:
    print('It is not palindrome')

#Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
#Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([element for element in a if element % 2 == 0])

#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a 
#message of congratulations to the winner, and ask if the players want to start a new game)
#Remember the rules:
#Rock beats scissors
#Scissors beats paper
#Paper beats rock

import random

def game(player1, player2):
    if player1 == player2 == ('R' or 'S' or 'P'): return '\nDraw\n'
    elif player1 == 'R' and player2 == 'S': return '\nWinner is you\n'
    elif player1 == 'S' and player2 == 'P': return '\nWinner is you\n'
    elif player1 == 'P' and player2 == 'R': return '\nWinner is you\n'
    else: return '\nI won!\n'

print('''
This is a two-player Rock-Paper-Scissors game.
Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock

''')

while True:
    user = input('Rock (R), Scissors (S), Paper (P) or Exit(E)?')
    if user == 'E' or user == 'e': break
    comp = random.choice(['R', 'S', 'P'])

    print(game(user, comp))
   
#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then 
#tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user 
#input lessons from the very first exercise)
#Extras:
#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken, and when the game ends, print this out.

'I did it in other project'



#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and
#makes a new list of only the first and last elements of the given list. For practice,
#write this code inside a function.

def firstlast(lista):
    return [lista[0], lista[-1]]
A = [5, 10, 15, 20, 25]
print(firstlast(A))
   
    
