import random

def DOB(whatToDraw):
    k = 0
    index = -1
    while(k<=6):
        if(k%2 == 0):
            i = 1
            while(i<=3):
                print(" --- ", end="")
                i = i+1
            print(" ", end="\n")
        else:
            j = 1
            while(j<=4):
                if(j <= 3):
                    index = index + 1
                    print("| " + whatToDraw[index] + " ", end=" ")
                else:
                    print("|")
                j = j+1
        k = k+1

def checkIfSomeoneWon():
    for i in winningPositions:
        j = i[0]
        k = i[1]
        l = i[2]
        if(board[j] == board[k] == board[l]) and (board[j] != ' '):
            if board[j] == 'X':
                return 'X'
            else:
                return 'O'


def checkIfItsADraw():
    for i in board:
        if i == ' ':
            return False
    return True

def findingAppropriatePositionForX():
    position = int(input("At which position do you want to insert 'X'?"))
    if (position > 8):
        print("Out of range of board")
    elif (board[position] == ' '):
        board[position] = 'X'
    else:
        print("O already exists try another position")
        findingAppropriatePositionForX()

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
winningPositions = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                    [0, 3, 6], [1, 4, 7], [2, 5, 8],
                    [0, 4, 8], [2, 4, 6]]
gameActive = True
won = False
i = 0
j = 1

while (gameActive):
    position = int(input("At which position do you want to insert 'X'?"))
    if position > 8:
        print("Out of range of board")
    elif board[position] == ' ':
        board[position] = 'X'
    else:
        print("X or O already exists try another position")
        findingAppropriatePositionForX()
    if j != 5:
        compPosition = random.randint(0, 8)
        while board[compPosition] is not(' '):
            compPosition = random.randint(0, 8)
        board[compPosition] = 'O'
    DOB(board)
    X_or_Y = checkIfSomeoneWon()
    if(X_or_Y == 'X' or X_or_Y == 'O'):
        won = True
    draw = checkIfItsADraw()
    if(won or draw):
        gameActive = False
        if(won):
            print(X_or_Y + " Won")
        else:
            print("Draw")
    j = j+1



