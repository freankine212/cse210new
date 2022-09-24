'''
tic-tac-toe
Author: Mike Helm
Class: CSE210
Purpose: to make a game of tic tac toe
'''

def main():
    gamer = next_person("")
    board = create_board()
    while not (is_winner(board) or is_a_tie(board)):
        display_board(board)
        play_already(gamer,board)
        gamer = next_person(gamer)
    display_board(board)
    print("GG, thanks for playing!")


def create_board():
    board = []
    for box in range(9):
        board.append(box+1)
    return board

def display_board(board):
    print()
    print(f'{board[0]}|{board[1]}|{board[2]}')
    print('-+-+-')
    print(f'{board[3]}|{board[4]}|{board[5]}')
    print('-+-+-')
    print(f'{board[6]}|{board[7]}|{board[8]}')
    print()

def is_a_tie(board):
    for box in range(9):
        if board[box] != "x" and board[box] != "o":
            return False
    return True

def is_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def play_already(gamer, board):
    square = int(input(f"{gamer}'s turn to choose a square (1-9): "))
    board[square - 1] = gamer

def next_person(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()