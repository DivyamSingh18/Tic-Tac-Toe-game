# importing libraries


theBoard = {'1': " ", '2': " ", '3': " ", '4': " ", '5': " ", '6': " ", '7': " ", '8': " ", '9': " "}

# user defined functions
def printBoard(board):
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    print('- + - + -')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('- + - + -')
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])

def playGame():
    player1 = input("\nEnter First PLayer's Name: ")
    player2 = input("Enter Second player's Name: ")

    print(player1 + ": X, " + player2 + " : O ")

    turn = "X"
    count = 0
    player = player1

    while True:
        printBoard(theBoard)

        if count == 9:
            print("The game ends in a Draw!")
            break
        if player == player1:
            move = input("Enter your move {}: " .format(player1))
        else:
            move = input("Enter your move {}: " .format(player2))

        if move not in theBoard.keys():
            print("Invalid move")
            continue

        if theBoard[move] == " ":
            theBoard[move] = turn

            # checking for winner
            winner = checkWin(turn)
            if winner != '':
                printBoard(theBoard)
                print("Congratulations!!! The winner is ", player)
                break
            else:
                count += 1
                if turn == "X":
                    turn = "O"
                    player = player2
                else:
                    turn = "X"
                    player = player1
        else:
            print("Sorry!, this place is already filled")


def checkWin(turn):
    winner = ''
    # checking for rows
    if (theBoard['7'] == theBoard['8'] == theBoard['9'] == turn) or (
            theBoard['4'] == theBoard['5'] == theBoard['6'] == turn) or (
            theBoard['1'] == theBoard['2'] == theBoard['3'] == turn):
        winner = turn
    # checking for columns
    if (theBoard['1'] == theBoard['4'] == theBoard['7'] == turn) or (
            theBoard['2'] == theBoard['5'] == theBoard['8'] == turn) or (
            theBoard['3'] == theBoard['6'] == theBoard['9'] == turn):
        winner = turn
    # checking for diagonals
    if (theBoard['1'] == theBoard['5'] == theBoard['9'] == turn) or (
            theBoard['3'] == theBoard['5'] == theBoard['7'] == turn):
        winner = turn

    return winner


def ask():
    x = input("Do you want to play again? (y/n)")
    if x == "y":
        global theBoard
        for key, val in  theBoard.items():
            theBoard[key] = " "
        main()

    elif x == "n":
        exit()

    else:
        ask()


def main():
    playGame()
    ask()

# Main

if __name__ == "__main__":
    print("############# TIC TAC TOE ############# ")
    main()
    ask()