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
   
#Write a program that asks the user how many Fibonnaci numbers to generate and then
#generates them. Take this opportunity to think about how you can use functions.
#Make sure to ask the user to enter the number of numbers in the sequence to generate.
#(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the
#sequence is the sum of the previous two numbers in the sequence. The sequence looks like
#this: 1, 1, 2, 3, 5, 8, 13, …)

count = int(input('How many numbers should i generate?'))

lista = [1]
p_number = 1
p_p_number = 0

for i in range(count - 1):
    new_number = p_number + p_p_number
    lista.append(new_number)
    p_p_number = p_number
    p_number = new_number
print(lista)

lista = [1, 1]
for i in range(count - 2):
    lista.append(lista[-1] + lista[-2])
print(lista)

#Write a program (function!) that takes a list and returns a new list
#that contains all the elements of the first list minus all the duplicates.
#Extras:
#Write two different functions to do this - one using a loop and constructing a list,
#and another using sets. Go back and do Exercise 5 using sets, and write the solution
#for that in a different function.

def list_without_duplicates1(lista):
    return list(set(lista))

def list_without_duplicates2(lista):
    newlist = []
    for element in lista:
        if element not in newlist:
            newlist.append(element)
    return newlist

E = [1, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9, 9]

print(list_without_duplicates1(E))
print(list_without_duplicates2(E))

#Write a program (using functions!) that asks the user for a long string containing
#multiple words. Print back to the user the same string, except with the words in
#backwards order. For example, say I type the string:
#  My name is Michele
#Then I would see the string:
#  Michele is name My
#shown back to me.

def reverse_order(string):
    return ' '.join(string.split()[::-1])

string = input('String to reverse: ')

print(reverse_order(string))

#Write a password generator in Python. Be creative with how you generate passwords -
#strong passwords have a mix of lowercase letters, uppercase letters, numbers, and
#symbols. The passwords should be random, generating a new password every time the
#user asks for a new password. Include your run-time code in a main method.
#Extra:
#Ask the user how strong they want their password to be. For weak passwords,
#pick a word or two from a list.

import random
import string

def Password_generator():
    answer = input('How strong do you want to have password?')

    try:
        if answer == 'weak':
            return random.choice(['pass1', 'pass2', 'pass3', 'pass4'])
        elif answer == 'medium':
            return ''.join([random.choice(string.ascii_letters.lower()) for x in range(10)])
        elif answer == 'hard':
            letters = string.ascii_letters
            signs = '!@#$%^&*()_+=-{}][:";<>?,./'
            return ''.join([random.choice(letters + signs) for x in range(20)])
        else:
            raise IndexError()
    except:
        return 'You answer is out of possible range'

print(Password_generator())

#Create a program that will play the “cows and bulls” game with the user. The game
#works like this: Randomly generate a 4-digit number. Ask the user to guess a 4-digit
#number. For every digit that the user guessed correctly in the correct place, they
#have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.”
#Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
#Once the user guesses the correct number, the game is over. Keep track of the number
#of guesses the user makes throughout teh game and tell the user at the end.
#Say the number generated by the computer is 1038. An example interaction could look
#like this:

#  Welcome to the Cows and Bulls Game! 
#  Enter a number: 
#  >>> 1234
#  2 cows, 0 bulls
#  >>> 1256
#  1 cow, 1 bull
#  ...

#Until the user guesses the number.

import random

def guessnumber(guess, target):
    #if not len(guess) == 4 or guess.isdigit() == False:
    #    return 'Error'
    cows = 0
    bulls = 0
    for i in range(4):
        if guess[i] == target[i]:
            cows += 1
        if guess[i] in target:
            bulls += 1
    return cows, bulls

def o_o_m(arg):
    if arg == 1:
        return ''
    else:
        return 's'

def print_result(cows, bulls):
    try:
        print(str(cows) + ' cow{}, '.format(o_o_m(cows)) + str(bulls) + ' bull{}'.format(o_o_m(bulls))) 
    except:
        print('Incorrect Entry')

print('''
This is a cow and bull game.
Guess my 4-digit number.
''')

TARGET = str(random.randrange(1000, 9999))
print(TARGET)
count = 0

while True:
    guess = input('')
    cows, bulls = guessnumber(guess, TARGET)
    if cows == 4:
        print('You guess the numer in {} tries'.format(count))
        break
    print_result(cows, bulls)
    count += 1
    
# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) 
# and another number. The function decides whether or not the given number is inside the list and returns (then prints) 
# an appropriate boolean.
# find is a function that takes an ordered list of numbers and another number,
# returning true or false whether the element appears in the list
# l is a list ordered from smallest to largest
# element is the number to find in the original list   

def find_element(element, lista):
    if element in lista:
        return True
 
if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0]
    print(find_element(4, lista))
    print(find_element(6, lista))
    print(find_element(7, lista))
    

        
    


