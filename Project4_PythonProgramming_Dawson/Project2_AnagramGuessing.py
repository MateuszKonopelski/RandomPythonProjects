print('''
Computer has chosen a word and mixed letters inside.
Try to guess it.

If you need hint, press "0", but every hint will be subtracted from final score.
''')

import random

WORDS = ('eggs', 'spam', 'cobra', 'rambo', 'puppy', 'pussy')

correct = random.choice(WORDS)
word = correct
anagram = ''

while word != '':
    position = random.randrange(0, len(word))
    anagram += word[position:position + 1]
    word = word[:position] + word[position + 1:]

guess = input("What is this word " + anagram + '?')
tip = 0

while guess != '' and guess.lower() != correct:
    if guess == '0':
        print(tip + 1, 'letter is', correct[tip])
        tip += 1
        guess = input("Your answer: ")
    else:
        print("Unfortunately wrong, try again.")
        guess = input("Your answer: ")

print("\nCongrats! You guessed it correctly!")
print("Your score is:", len(correct)-tip, '/', len(correct))
input("To finish the game, press 'Enter'.")
