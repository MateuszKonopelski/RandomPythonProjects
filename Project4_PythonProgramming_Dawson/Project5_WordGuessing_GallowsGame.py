# Import

import random

# Constants

NAMES = ('CHRISTIE', 'SHAKESPEARE', 'CARTLAND', 'STEEL', 'ROBBINS', 'SIMENON', 'SHELDON', 'BLYTON', 'ROWLING')

HANGMAN = (
'''
 _______
|/      |
|
|
|
|
|
|\\
|_\\_________
''',
'''
 _______
|/      |
|       0
|
|
|
|
|\\
|_\\_________
''',
'''
 _______
|/      |
|       0
|       +
|
|
|
|\\
|_\\_________
''',
'''
 _______
|/      |
|       0
|    \- +
|
|
|
|\\
|_\\_________
''',
'''
 _______
|/      |
|       0
|    \- + -/
|
|
|
|\\
|_\\_________
''',
'''
 _______
|/      |
|       0
|    \- + -/
|       |
|
|
|\\
|_\\_________
''',
'''
 _______
|/      |
|       0
|    \- + -/
|       |
|       |
|
|\\
|_\\_________
''',
'''
 _______
|/      |
|       0
|    \- + -/
|       |
|       |
|      /
|\\
|_\\_________
''',
'''
 _______
|/      |
|       0
|    \- + -/
|       |
|       |
|      / \\
|\\
|_\\_________
'''
)

# Print Rules
print('''
This is a HANGMAN game.
From list of best-selling fiction authors,
you have 8 tries to guess the one I have in mind.
before hangman hangs.
''', HANGMAN[0])

# variables
name = random.choice(NAMES)
guess = '-' * len(name)
tries = 0
used = []

# procedure
while not name == guess:
    print('Correct letters:', guess)
    print('\n\nUsed letter:', used)
    letter = input('Guess a letter: ')
    letter = letter.upper()
    if not len(letter) == 1 or letter.isalpha == False:
        print('You can only fill one letter.')
    elif letter in used:
        print('You already used this letter')
    elif letter in name:
        if not letter in guess:
            pos = name.index(letter)
        else:
            pos = name.index(letter, 2)
        guess = list(guess)
        guess[pos] = letter
        guess = ''.join(guess)
        print('Congrats!', letter, 'is part of the name: ', guess)
    else:
        tries += 1
        print(HANGMAN[tries])
        used.append(letter)
        if tries == 8:
            break

if tries < 8:
    print('You have correctly guessed the name of writer: ', name)
else:
    print('Unfortunately. You reached your maximum tries.')



