import sys
import random

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]


def drawboard():
    print("  " + board[0] + " |  " + board[1] + "  |  " + board[2])
    print("---------------")
    print("  " + board[3] + " |  " + board[4] + "  |  " + board[5])
    print("---------------")
    print("  " + board[6] + " |  " + board[7] + "  |  " + board[8])
    print("                   ")


c1 = 0
player_decisionv1 = input("What will you choose? X or O? ")
if player_decisionv1 in "X":
    c1 = str(player_decisionv1)
elif player_decisionv1 in "O":
    c1 = str(player_decisionv1)
else:
    while True:
        if player_decisionv1 in "X" or player_decisionv1 in "O":
            c1 = str(player_decisionv1)
            break
        else:
            player_decisionv1 = input("Please enter X or O(not zero)!!! ")
            continue

t = 1
x1 = 0


def win(c):
    if board[0] == board[1] == board[2] and board[0] in "X" or \
        board[3] == board[4] == board[5] and board[3] in "X" or \
        board[6] == board[7] == board[8] and board[6] in "X" or \
        board[0] == board[3] == board[6] and board[0] in "X" or \
        board[1] == board[4] == board[7] and board[1] in "X" or \
        board[2] == board[5] == board[8] and board[2] in "X" or \
        board[0] == board[4] == board[8] and board[0] in "X" or \
        board[2] == board[4] == board[6] and board[2] in "X":
        if findenemyc(c) in "X":
            print("The Enemy won!")
            sys.exit()
        elif findenemyc(c) in "O":
            print("The Player won!")
            sys.exit()
    elif board[0] == board[1] == board[2] and board[0] in "O" or \
        board[3] == board[4] == board[5] and board[3] in "O" or \
        board[6] == board[7] == board[8] and board[6] in "O" or \
        board[0] == board[3] == board[6] and board[0] in "O" or \
        board[1] == board[4] == board[7] and board[1] in "O" or \
        board[2] == board[5] == board[8] and board[2] in "O" or \
        board[0] == board[4] == board[8] and board[0] in "O" or \
        board[2] == board[4] == board[6] and board[2] in "O":
        if findenemyc(c) in "O":
            print("The Enemy won!")
            sys.exit()
        elif findenemyc(c) in "X":
            print("The Player won!")
            sys.exit()
    else:
        return False


def boardfull():
    if board[0] == board[1] == board[2] == board[3] == board[4] == board[5] == board[6] == board[7] == board[8] != " ":
        return True
    else:
        return False


while win(c1) is False and boardfull() is False:
    boardfull()
    def boxisempty(x):
        if board[x - 1] in " ":
            return True
        else:
            return False


    def findenemyc(c):
        if c in "X":
            return "O"
        elif c in "O":
            return "X"


    def playermove(x, c):
        if boxisempty(x) is True:
            board[x - 1] = c
        elif boxisempty(x) is False:
            while boxisempty(x) is False:
                pd = input("Please enter the number of a box that is not occupied: ")
                if boxisempty(int(pd)) is True:
                    board[int(pd) - 1] = c
                    break
                elif boxisempty(int(pd)) is False:
                    print("Please make sure the number is between 0 and 10 too!")
                    continue


    player_decision2v1 = input("Where will you put your " + player_decisionv1 + '? ')
    if player_decision2v1.isdigit() is False:
        while player_decision2v1.isdigit() is False:
            player_decision2v1 = input("Please enter a digit between 0 and 10: ")
            if player_decision2v1.isdigit() is False:
                continue
            elif player_decision2v1.isdigit() is True:
                x1 = int(player_decision2v1)
                break
    if player_decision2v1 not in range(0, 10):
        x1 = int(player_decision2v1)
        while not 0 < x1 < 10:
            decision = input("Please enter a digit between 0 and 10: ")
            x1 = int(decision)
            continue
    else:
        x1 = int(player_decision2v1)


    def enemyalgorithm1():
        if findenemyc(c1) in "X":
            while True:
                x = random.randrange(1, 10)
                if boxisempty(x) is True:
                    print("The Enemy did something!")
                    print("                       ")
                    board[x - 1] = "X"
                    break
        elif findenemyc(c1) in "O":
            while True:
                x = random.randrange(1, 10)
                if boxisempty(x) is True:
                    print("The Enemy did something!")
                    print("                       ")
                    board[x - 1] = "O"
                    break

    playermove(x1, c1)
    drawboard()
    win(c1)
    enemyalgorithm1()
    drawboard()
    win(c1)
print("It's a tie!")
