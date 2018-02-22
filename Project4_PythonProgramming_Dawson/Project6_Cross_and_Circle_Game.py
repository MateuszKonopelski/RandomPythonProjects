'''
This is a Cross and Circle Game where user is in battle with computer
over the victory on fencing floor.


'''

# Import modules

# Global constants
X = 'X'
O = 'O'
EMPTY = ''
TIE = 'TIE'
NUM_SQUARES = 9

# Functions


def display_instruct():
    '''Display instructions of the Game'''
    print('''
     Welcome to the biggest mind challenge of all times.
     This is a Cross and Circle Game.
     This will be the last battle of your human brain
     and my computer algorithms.

     Your moves you will indicate by choosing number in
     range 1 - 9. Those numbers are associated with position
     on floor just as on below scheme:

                1 | 2 | 3
                _________
                4 | 5 | 6
                _________
                7 | 8 | 9

     Prepare Human! The last battle will start soon!\n
    ''')


def ask_yes_no(question):
    '''Ask for user input. Possible answers: Y or N.'''
    response = None
    while response not in('y', 'n'):
        response = input(question).lower()
    return response


def ask_number(question):
    '''Ask for User Number on Grid. It must be between 1 - 9'''
    response = None
    while response not in range(1, 9):
        response = input(question)
    return response


def pieces():
    '''Use user answer to question "who starts?" to appoint chips.'''
    go_first = ask_yes_no('Do you want to have first move? <y/n>:')
    if go_first == 'y':
        print('\nThe First move is yours. You will need it.')
        computer = O
        human = X
    else:
        print('\nYour courage will kill you... I start.')
        computer = X
        human = O
    return computer, human





# Procedure

display_instruct()

