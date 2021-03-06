from os import system, name
from time import sleep

board = [' ' for _ in range(10)]


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '


def printBoard():
    print("     +     +   ")
    print(f"  {board[1]}  +  {board[2]}  +  {board[3]}")
    print("     +     +   ")
    print("+++++++++++++++++")
    print("     +     +   ")
    print(f"  {board[4]}  +  {board[5]}  +  {board[6]}")
    print("     +     +   ")
    print("+++++++++++++++++")
    print("     +     +   ")
    print(f"  {board[7]}  +  {board[8]}  +  {board[9]}")
    print("     +     +   ")


def isWinner(bo, letter):
    return (bo[1] == letter and bo[2] == letter and bo[3] == letter) or (
                bo[4] == letter and bo[5] == letter and bo[6] == letter) or (
                   bo[7] == letter and bo[8] == letter and bo[9] == letter) or (
                   bo[1] == letter and bo[4] == letter and bo[7] == letter) or (
                   bo[2] == letter and bo[5] == letter and bo[8] == letter) or (
                   bo[3] == letter and bo[6] == letter and bo[9] == letter) or (
                   bo[1] == letter and bo[5] == letter and bo[9] == letter) or (
                   bo[3] == letter and bo[5] == letter and bo[7] == letter)


def playerMove():
    run = True
    while run:
        move = input("Enter a position to place an 'X' (1-9): ")
        try:
            move = int(move)
            if 0 < move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry! That place is occupied')
            else:
                print('Please enter a number within range!')
        except:
            print('Please type a number!')


def compMove():
    move = 0
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]

    for lt in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = lt
            if isWinner(boardCopy, lt):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

    return move


def selectRandom(ls):
    import random
    ln = len(ls)
    r = random.randrange(0, ln)
    return ls[r]


def isBoardFull(bo):
    return not board.count(' ') > 1


def main():
    print("Welcome to Tic-Tac-Toe by Bhargav Andhe!")
    printBoard()

    while not (isBoardFull(board)):
        if not (isWinner(board, 'O')):
            playerMove()
            clear()
            printBoard()
        else:
            print("Sorry, You Lose!")
            break

        if not (isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                clear()
                print("Computer is thinking...")
                sleep(1)
                clear()
                print(f"Computer placed an 'O' in position {move}:")
                printBoard()

        else:
            print("Hurrah! You Win.")
            break

    if isBoardFull(board):
        print("Tie Game!")


if __name__ == '__main__':
    main()
