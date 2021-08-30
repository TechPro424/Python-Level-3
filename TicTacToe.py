theBoard = {'1': '  ', '2': '  ', '3': '  ',
            '4': '  ', '5': '  ', '6': '  ',
            '7': '  ', '8': '  ', '9': '  '}

boardkeys = []

for key in theBoard:
  boardkeys.append(key)

def printBoard(board):
  print(board['1'] + '|' + board['2'] + '|' + board['3'])
  print('--------')
  print(board['4'] + '|' + board['5'] + '|' + board['6'])
  print('--------')
  print(board['7'] + '|' + board['8'] + '|' + board['9'])

def game():
    turn = 'x'
    count = 0

    for i in range(10):
        printBoard(theBoard)

        move = input("It's your turn, " + turn + ". Move to which place?")

        if theBoard[move] == '  ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled. Move to which place?")
            continue
        # Now we check if a player has won, for every move after 5 moves.

        if count >= 5:
            if theBoard['1'] == theBoard['2'] == theBoard['3'] != '  ':

                printBoard(theBoard)
                print("Game over.")
                print('**** '+turn+ 'won! ****')
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != '  ':

                printBoard(theBoard)
                print("Game over.")
                print('**** '+turn+ 'won! ****')
                break
            elif theBoard['7'] == theBoard['8'] == theBoard['9'] != '  ':

                printBoard(theBoard)
                print("Game over.")
                print('**** '+turn+ 'won! ****')
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != '  ':

                printBoard(theBoard)
                print("Game over.")
                print('**** '+turn+ 'won! ****')
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != '  ':

                printBoard(theBoard)
                print("Game over.")
                print('**** '+turn+ 'won! ****')
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != '  ':

                printBoard(theBoard)
                print("Game over.")
                print('**** '+turn+ 'won! ****')
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != '  ':

                printBoard(theBoard)
                print("Game over.")
                print('**** '+turn+ 'won! ****')
                break
            elif theBoard['3'] == theBoard['5'] == theBoard['7'] != '  ':

                printBoard(theBoard)
                print("Game over.")
                print('**** '+turn+ 'won! ****')
                break
        if count == 9:
            printBoard(theBoard)
            print("Game over.")
            print("**** It's a tie! ****")
            break

        if turn == 'x':
            turn = 'o'
        else:
            turn = 'x'
    
    restart = input("Do you want to restart the game? (y/n)")
    if restart.lower() == 'y':
        for key in boardkeys:
            theBoard[key] = '  '
        game()

if __name__ == '__main__':
    game()