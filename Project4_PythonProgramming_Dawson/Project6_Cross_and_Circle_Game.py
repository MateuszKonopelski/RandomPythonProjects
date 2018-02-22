'''
This is a Cross and Circle Game where user is in battle with computer
over the victory on the board.


'''

# Import modules
import random

# Global constants
X = 'X'
O = 'O'
EMPTY = ' '
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
    '''Ask for User Number on board. It must be between 1 - 9'''
    response = None
    while response not in range(0, 8):
        response = int(input(question)) - 1
    return response


def pieces():
    '''Use user answer to question "who starts?" to appoint chips.'''
    global computer, human
    go_first = ask_yes_no('Do you want to have first move? <y/n>: ')
    if go_first == 'y':
        print('\nThe First move is yours. You will need it.\nYou have X\n')
        computer = O
        human = X
    else:
        print('\nYour courage will kill you... I start.\nYou have O\n')
        computer = X
        human = O
    return computer, human


def new_board():
    '''Create empty board.'''
    board = [EMPTY for i in range(NUM_SQUARES)]
    return board


def display_board(board):
    '''Display actual board'''
    scheme = '''
                1 | 2 | 3
                _________
                4 | 5 | 6
                _________
                7 | 8 | 9
    '''
    for i in range(NUM_SQUARES):
        scheme = scheme.replace(str(i+1), str(board[i]))
    print(scheme)


def legal_move(board):
    '''Return positions on board which are empty'''
    lmove = []
    for pos in range(NUM_SQUARES):
        if board[pos] == EMPTY:
            lmove.append(pos)
    return lmove


def winner(board):
    global result
    possible_conf = [(0, 1, 2),
                     (3, 4, 5),
                     (6, 7, 8),
                     (0, 3, 6),
                     (1, 4, 7),
                     (2, 5, 8),
                     (0, 4, 6),
                     (2, 4, 6)]
    tie = 0
    for conf in possible_conf:
        if board[conf[0]] == X and board[conf[1]] == X and board[conf[2]] == X:
            if computer == X:
                result = 'Winner is Me!'
            else:
                result = 'Oh No. You Won! :('
            return X
        elif board[conf[0]] == O and board[conf[1]] == O and board[conf[2]] == O:
            if computer == O:
                result = 'Winner is Me!'
            else:
                result = 'Oh No. You Won! :('
            return O
        else:
            if [1 for i in board if i == ' '] == 1:
                pass
            tie += 1
            #if tie == 8: print('No winner! Tie')


def human_move(board):
    '''Indicate your position on board'''
    choice = ask_number('What is your move? <1-9>')
    if choice in legal_move(board):
        board[choice] = human
        display_board(board)
    else:
        print('This field is already used or outside <1-9> range.')
        human_move(board)


def comp_move(board):
    '''Algorithm to set computer move'''
    board[random.choice(legal_move(board))] = computer
    print('My move:')
    display_board(board)

# Procedure
display_instruct()
pieces()
board = new_board()

while True:
    if human == X:
        human_move(board)
        if winner(board) == X or winner(board) == O: break
        comp_move(board)
        if winner(board) == X or winner(board) == O: break
    else:
        comp_move(board)
        if winner(board) == X or winner(board) == O: break
        human_move(board)
        if winner(board) == X or winner(board) == O: break

print('\nEND OF GAME\n', result)

