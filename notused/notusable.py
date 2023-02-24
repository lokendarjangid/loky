# Python3 program to demonstrate Morse code

# function to encode a alphabet as
# Morse code
def morseEncode(x):
    # refer to the Morse table
    # image attached in the article
    if x == 'a':
        return ".-"
    elif x == 'b':
        return "-..."
    elif x == 'c':
        return "-.-."
    elif x == 'd':
        return "-.."
    elif x == 'e':
        return "."
    elif x == 'f':
        return "..-."
    elif x == 'g':
        return "--."
    elif x == 'h':
        return "...."
    elif x == 'i':
        return ".."
    elif x == 'j':
        return ".---"
    elif x == 'k':
        return "-.-"
    elif x == 'l':
        return ".-.."
    elif x == 'm':
        return "--"
    elif x == 'n':
        return "-."
    elif x == 'o':
        return "---"
    elif x == 'p':
        return ".--."
    elif x == 'q':
        return "--.-"
    elif x == 'r':
        return ".-."
    elif x == 's':
        return "..."
    elif x == 't':
        return "-"
    elif x == 'u':
        return "..-"
    elif x == 'v':
        return "...-"
    elif x == 'w':
        return ".--"
    elif x == 'x':
        return "-..-"
    elif x == 'y':
        return "-.--"
    elif x == 'z':
        return "--.."
    elif x == '1':
        return ".----"
    elif x == '2':
        return "..---"
    elif x == '3':
        return "...--"
    elif x == '4':
        return "....-"
    elif x == '5':
        return "....."
    elif x == '6':
        return "-...."
    elif x == '7':
        return "--..."
    elif x == '8':
        return "---.."
    elif x == '9':
        return "----."
    elif x == '0':
        return "-----"


# character by character print
# Morse code
def morseCode(s):
    for character in s:
        print(morseEncode(character), end="")

def calculator():
    """This is calculator which calculate digits and give answer to you."""  # need to modify

    for mm in range(1, 5):  # I use FOR because there are many people who recur more time calculator.
        # you can (break) this command if you don't want to continue this .
        # BREAK command in line 23.
        x = int(input("Enter first digit :"))
        z = str(input("Choose from these(+,-,/,*,%) or you can stop here(stop) :"))
        if z == "bye" or z == "good bye" or z == "exit" or z == "stop":
            break
        y = int(input("Enter second digit :"))
        if z == "+":
            print("sum is", x + y)
        elif z == "-":
            print("answer is", x - y)
        elif z == "/":
            print("answer  is", x / y)
        elif z == "*":
            print("multiplication is", x * y)
        elif z == "%":
            print("answer is ", x % y)
        else:
            print("This option is not available in this list")

def roots_of_quadratic_equation():
    """This function will find roots of quadratic equation and useful for school
    students."""

    a = int(input("Enter a :"))
    b = int(input("Enter b :"))
    c = int(input("Enter c :"))

    if a == 0:
        print("value of", a, 'should not be zero')
        print("\n Aborting !!!!!")
    else:
        delta = b * b - 4 * a * c
        if delta > 0:
            root1 = (-b + math.sqrt(delta)) / (2 * a)
            root2 = (-b - math.sqrt(delta)) / (2 * a)
            print("Roots are REAL and UNEQUAL")
            print("Root1=", root1, ",Root2=", root2)
        elif delta == 0:
            root1 = -b / (2 * a)
            print("Roots are REAL and EQUAL")
            print("Root1=", root1, ",Root2=", root1)
        else:
            print("Roots are COMPLEX and IMAGINARY")




def sum_of_n_terms():
    """This is normal function of maths . For class 10 and upper stander it is usable .
    It will help you to find out sum of terms which are in continuous oder"""

    nthterm = int(input("enter n :"))
    firstterm = int(input("enter a :"))
    difference = int(input("enter d :"))

    if nthterm == 0:
        print("value of 'a' should not be", firstterm)
    else:
        sumitionofnthterm = nthterm / 2 * ((2 * firstterm) + (nthterm - 1) * difference)
        print("sum of nth terms is", sumitionofnthterm)


def table():
    """This function will help you to find out table of any number in maths ."""

    num = int(input("Enter number for table : "))
    # using for loop to iterate multiplication 10 times
    for i in range(1, 11):
        print(num, 'x', i, '=', num * i)
    print("Thanks for using this program ")


# txt_file

def createtxt():
    """This is normal text file crater. which can create txt file easy .
    you can easy add text or numbers into text file which you created ."""

    # Entering file name
    file_name = input("Enter file name :")
    # opening txt file
    f = open(file_name + ".txt", 'w')
    # asking to add text into file
    option = input("Would you like to print anything into text file(y/n):")
    if option in "Yy" or "yes" in option:
        print("What do you want to enter into file")
        print("1.Text\n2.Numbers\n3.exit")
        # asking to what do you want to add into txt
        ch = int(input("Enter your choice :"))
        # giving loop to add break command
        for i in range(1, 2):
            if ch == 1:
                # adding words here
                print("Enter your words below :")
                while True:
                    words = input()
                    if words == "exit":
                        break
                    f.write(str(words) + "\n")
            elif ch == 2:
                # asking from where to where add number
                fromwhere = int(input("From :"))
                towhere = int(input("To :"))
                steps = input("Steps :")
                if steps in "":
                    steps = 1
                steps = int(steps)
                for j in range(fromwhere, towhere + 1, steps):
                    f.write(str(j) + "\n")
            elif ch == 3:
                break
            else:
                print("Please type correct number!!!")
            print("completed...")
    else:
        print("Thanks for using this program...")


# game file

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

def passchanger():  # Use when you want to change password

    """password changer for loky program."""

    while True:
        f = open("password.dat", "wb")
        username = input("USERNAME :")
        password = input("PASSWORD :")
        rec = pickle.load(f)
        if rec[0] == username and rec[1] == password:
            print("This Username already existent..\nChoose another Username/Password.")
            passchanger()
        rec = [username, password]
        pickle.dump(rec, f)
        f.close()
        break


def passwordlogin():  # Password login function

    """password logger in loky"""

    print("Hello sir...")
    print("Enter you Username/Password.")
    f = open("password.dat", "rb")
    rec = pickle.load(f)
    username = input("USERNAME :")
    password = input("PASSWORD :")
    if rec[0] == username and rec[1] == password:
        print("you are logged in....")
        f.close()
        main()
    else:
        print("Username/Password is wrong.")
        print("Try again!!!")
        passwordlogin()
