# This will manage game developed in this folder

def manage_game():
    """This is to manage game . when you type game you will get game sequence
    from this function."""

    print("Which game you want to play.\n1.Tik tak toe\n2.Number game")
    ch = int(input("\nEnter number :"))
    if ch == 1:
        tik_tak_toe()
    elif ch == 2:
        number_game()
    else:
        print("Game not founded!!!")


# This number game developed.

def number_game():
    """Game which is makeup of number. In this game you choose number b/w 1 to 10
    if number match correct number you win this game."""

    import random as r
    for g in range(1, 4):
        number = r.randint(1, 11)
        print("you will get three chance to play")
        a = str(input("Enter a number between 1 to 10 :"))
        if a == number:
            print("YOU WIN")
            break
        else:
            print("YOU LOSE")


# This tik-tak-toe game developed.

def tik_tak_toe():
    """Game which is Tik-Tak-Toe everyone can play this game easily .
    everyone know how to play this game."""

    # Implementation of Two Player Tic-Tac-Toe game in Python.

    ''' We will make the board using dictionary
        in which keys will be the location(i.e : top-left,mid-right,etc.)
        and initially it's values will be empty space and then after every move
        we will change the value according to player's choice of move. '''

    theboard = {'7': ' ', '8': ' ', '9': ' ',
                '4': ' ', '5': ' ', '6': ' ',
                '1': ' ', '2': ' ', '3': ' '}

    board_keys = []

    for key in theboard:
        board_keys.append(key)

    ''' We will have to print the updated board after every move in the game and 
        thus we will make a function in which we'll define the printBoard function
        so that we can easily print the board everytime by calling this function. '''

    def printboard(board):
        print(board['7'] + '|' + board['8'] + '|' + board['9'])
        print('-+-+-')
        print(board['4'] + '|' + board['5'] + '|' + board['6'])
        print('-+-+-')
        print(board['1'] + '|' + board['2'] + '|' + board['3'])

    # Now we'll write the main function which has all the gameplay functionality.
    def game():
        turn = 'X'
        count = 0

        for i in range(10):
            printboard(theboard)
            print("It's your turn," + turn + ".Move to which place?")

            move = input()

            if theboard[move] == ' ':
                theboard[move] = turn
                count += 1
            else:
                print("That place is already filled.\nMove to which place?")
                continue

            # Now we will check if player X or O has won,for every move after 5 moves.
            if count >= 5:
                if theboard['7'] == theboard['8'] == theboard['9'] != ' ':  # across the top
                    printboard(theboard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break
                elif theboard['4'] == theboard['5'] == theboard['6'] != ' ':  # across the middle
                    printboard(theboard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break
                elif theboard['1'] == theboard['2'] == theboard['3'] != ' ':  # across the bottom
                    printboard(theboard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break
                elif theboard['1'] == theboard['4'] == theboard['7'] != ' ':  # down the left side
                    printboard(theboard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break
                elif theboard['2'] == theboard['5'] == theboard['8'] != ' ':  # down the middle
                    printboard(theboard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break
                elif theboard['3'] == theboard['6'] == theboard['9'] != ' ':  # down the right side
                    printboard(theboard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break
                elif theboard['7'] == theboard['5'] == theboard['3'] != ' ':  # diagonal
                    printboard(theboard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break
                elif theboard['1'] == theboard['5'] == theboard['9'] != ' ':  # diagonal
                    printboard(theboard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break

                    # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
            if count == 9:
                print("\nGame Over.\n")
                print("It's a Tie!!")

            # Now we have to change the player after every move.
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'

                # Now we will ask if player wants to restart the game or not.
        restart = input("Do want to play Again?(y/n)")
        if restart == "y" or restart == "Y":
            for key in board_keys:
                theboard[key] = " "

            game()

    game()
