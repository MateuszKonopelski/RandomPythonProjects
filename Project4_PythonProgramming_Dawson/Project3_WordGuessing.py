print('''
Computer has a word in "mind".
Would you like to guess it?

You can ask 10 times if your letter is included.
After which you need to guess it.

Good Luck!!!

''')

import random

word = random.choice(('book', 'table', 'window', 'linux', 'spam', 'eggs', 'python', 'cobra'))

print("Computer's word has", len(word), "letters.")
for i in range(10):
    guess = input(str(i+1) + "letter: ")
    if guess in word:
        print("This letter included. Position:", word.find(guess)+1)
    else:
        print("This letter is not included.")

if input('Your guess:') == word:
    print('Congrats!!')
else:
    print("Unfortunately the word is wrong. The correct is:", word)