print('''
This is an IT slang dictionary.

Use the menu to select one of the options.
''')

MSG = '''
'1' for finding IT slang definition
'2' for adding new definition
'3' correcting definition
'4' deleting term
'5' show all it slang terms in dictionary
'0' exit the program
'''

geek = {'404': 'Ignorant. Used from 404 error in html',
        'googling': 'Using internet to find information about particular person.',
        'keyboard plaque': 'Food and other rodents hidden in keyboard spaces.',
        'link rot': 'Dead link in internet.',
        'percussive maintenace': 'Solving a problem using a fist',
        'uninstalled': 'Being fired from the your work',
        'noob': 'Someone with little experience'}

choice = None

while choice != '0':
    print(MSG)
    choice = input('Choose one option: ')

    if choice == '1':
        word = input('What term you look for: ')
        print(geek.get(word.lower(), "Error: Dictionary doesn't include this term."))
    elif choice == '2':
        word = input('What term would you like to add: ').lower()
        geek[word] = input('Fill here the definition: ')
        print('New Term:', word, '\nNew definition:', geek[word])
    elif choice == '3':
        word = input('What term would you like to correct: ')
        if word in geek:
            geek[word] = input('What is the correct definition: ')
        else:
            print('This term is not included in dictionary')
    elif choice == '4':
        word = input('Which term would you like to delete?').lower()
        if word in geek:
            print(word, 'has been deleted.')
            del geek[word]
        else:
            print('This term is not in dictionary')
    elif choice == '5':
        for item in geek:
            print(item)
    else:
        if not choice == '0': print('Incorrect Entry. Please choose form 0-5.')

input('In order to close the program. Press "Enter".')
