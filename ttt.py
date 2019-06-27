import sys
import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

choice = 0
win = False

#Prints out full board
def printBoard():
    print("\n" +
    board[0] + " " + board[1] + " " + board[2] + "\n" +
    board[3] + " " + board[4] + " " + board[5] + "\n" +
    board[6] + " " + board[7] + " " + board[8] + "\n"
    )

#Opponent makes a move (COMPLEX AI, DO NOT TOUCH)
def opponent_move():
    noMove = True

    while noMove:
        r = random.randint(0,8)
        if board[r] == "-":
            board[r] = "O"
            noMove = False

#Checks if board is full and exits if True
def isFull():
    ctr = 0

    for i in range(len(board)):
        if board[i] != "-":
            ctr += 1
    if ctr == 9:
        printBoard()
        print("The board is full. Game Over! Play again?")
        sys.exit(0)

#Checks if someone has won
def victory():
    #Checks if you have won
    if (board[0] == "X" and board[1] == "X" and board[2] == "X"): youWin()
    if (board[3] == "X" and board[4] == "X" and board[5] == "X"): youWin()
    if (board[6] == "X" and board[7] == "X" and board[8] == "X"): youWin()
    if (board[0] == "X" and board[3] == "X" and board[6] == "X"): youWin()
    if (board[1] == "X" and board[4] == "X" and board[7] == "X"): youWin()
    if (board[2] == "X" and board[5] == "X" and board[8] == "X"): youWin()
    if (board[0] == "X" and board[4] == "X" and board[8] == "X"): youWin()
    if (board[2] == "X" and board[4] == "X" and board[6] == "X"): youWin()

    #Checks if opponent has won
    if (board[0] == "O" and board[1] == "O" and board[2] == "O"): youLose()
    if (board[3] == "O" and board[4] == "O" and board[5] == "O"): youLose()
    if (board[6] == "O" and board[7] == "O" and board[8] == "O"): youLose()
    if (board[0] == "O" and board[3] == "O" and board[6] == "O"): youLose()
    if (board[1] == "O" and board[4] == "O" and board[7] == "O"): youLose()
    if (board[2] == "O" and board[5] == "O" and board[8] == "O"): youLose()
    if (board[0] == "O" and board[4] == "O" and board[8] == "O"): youLose()
    if (board[2] == "O" and board[4] == "O" and board[6] == "O"): youLose()

#Victory message
def youWin():
    printBoard()
    print("Congratulations! You Win!\n")
    sys.exit(0)

#Defeat message
def youLose():
    printBoard()
    print("Sorry, you lose.\n")
    sys.exit(0)

#Checks if input is an integer and is between 1 and 9
def validateChoice():
    bool = True
    x = 0
    while bool:
        try:
            x = int(input())
        except ValueError:
            print("")
        if x >= 1 and x <= 9:
            return x
        else:
            print("That entry is not valid. Please enter a number, 1-9.\n")



if __name__ == "__main__":
    while win != True:
        print("\nPlease choose a tile! 1-9")
        printBoard()
        choice = validateChoice()
        #Checks if spot is already taken
        while board[choice-1] != "-":
            print("That spot is already taken, please choose another one:\n")
            choice = input()
        board[choice-1] = 'X'
        isFull()
        victory()
        opponent_move()
        isFull()
        victory()