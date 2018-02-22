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
    while response not in range(0, 9):
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
    print('\n\t', board[0], '|', board[1], '|', board[2])
    print('\t', '-' * 10)
    print('\t', board[3], '|', board[4], '|', board[5])
    print('\t', '-' * 10)
    print('\t', board[6], '|', board[7], '|', board[8])


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
    for conf in possible_conf:
        if board[conf[0]] == board[conf[1]] == board[conf[2]] != EMPTY:
            return board[conf[0]]
        elif EMPTY not in board:
            return TIE
        else:
            return None


def human_move(board, human):
    '''Indicate your position on board'''
    legal = legal_move(board)
    move = None
    while move not in legal:
        move = ask_number('What is your move? <1-9>')
        if move not in legal:
            print('This field is already used or outside <1-9> range.')
    return move

def comp_move(board, computer, human):
    '''Algorithm to set computer move'''
    # Copy of the existing list in order to make tests
    board = board[:]

    # Best positions to have on board (middle, corners, rest)
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    # If I can win the game by setting last place:
    for move in legal_move(board):
        board[move] == computer
        if winner(board) == computer:
            print(move)
            return(move)
        # this move was checked, undo it
        board[move] = EMPTY

    # If user can win, block it
    for move in legal_move(board):
        board[move] = human
        if winner(board) == human:
            return(move)
        # this move was checked, undo it
        board[move] = EMPTY

    # If noone can win, choose the best field
    for move in BEST_MOVES:
        if move in legal_move(board):
            return(move)


def next_turn(turn):
    '''Change the turn maker'''
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, computer, human):
    '''Print the winner or tie with a comment'''
    if the_winner != TIE:
        print(the_winner, 'is the winner!')
    else:
        print("It's a tie!")

    if the_winner == human:
        print('Oh No! How is it possible? You tricked me little human!',
                'But it will not happend again! I promise that.')

    elif the_winner == computer:
        print('This is what I anticipated. You have no chance with me human!',
              'This is a proof that computers are better than humans')

    elif the_winner == TIE:
        print('You were lucky this time. It"s a tie. Would you like to play again?')


# Main function
def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = comp_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

# Procedure
main()
input('\n\nPress Enter to finish the game.\n\n')
