import math as m
import pickle
from time import sleep


def helpfor():  # Help function to give help data    #Not completed

    """This for help who don't how to use this program .
    Here is all information added this function .This function give all information
    about use function in this program or you can open that function form here
    directly by typing help and function name. If you type help then you will get all information
    about function and function will directly run from here."""

    if d == "help":
        print('''you can ask me about my self or my information   
                    menu for my commands :
                    (FOR)                             TYPE(COMMAND)\n
                    calculator                        open calculator
                    calculate sum of n term           calculate sum of n terms
                    factorial                         calculate factorial
                    area of circle                    calculate area of circle
                    perimeter of circle               calculate perimeter of circle
                    tik tak toe                       open tik tak toe
                    game                              open game
                    roots of quadratic equation       find roots of quadratic equation
                    table                             find table , table
                    square root                       find square root
                    quiz master                       play quiz
                    EXIT                              bye,exit,good bye
                    ''')  # Menu of commands
    elif "game" in d:
        print(
            "Here is two types of game which you can play.\nThese game are only for entertainment which you can play.")
        print("Anybody can play these games.\nNo restriction for kids")
        print("1.Tik tak toe\n2.Number game")
        wanttoplay = input("\nDo you want to play game :")
        if wanttoplay in "Yy" or wanttoplay == "yes":
            manage_game()
    elif "calculator" in d:
        print("This is normal calculator. which you can use.\n")
        wanttouse = input("Do you want to use it :")
        if wanttouse in "Yy" or wanttouse == "yes":
            calculator()
    else:
        input("This command is not in this program")
        main()


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


# main_password


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
    sleep(1)
    print("Enter you Username/Password.")
    sleep(1)
    f = open("password.dat", "rb")
    rec = pickle.load(f)
    username = input("USERNAME :")
    password = input("PASSWORD :")
    if rec[0] == username and rec[1] == password:
        print("loading.....")
        sleep(2)
        main()
    f.close()


# normal maths


def area_of_circle():
    """This function will calculate area of circle . when you enter radius .
    This function will calculate automatically area of circle and give you answer."""

    radius = float(input("Enter radius of circle :"))
    area = 3.14159 * radius * radius
    print("area of circle is", area)


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


def factorialanotherway():
    """This function is used to calculate factorial for you. In class 11 and 12 this operation used .
    This function is very useful for students. symbol used in maths for this function is !."""

    n = int(input("Enter value for factorial : "))
    a = 1
    b = 1
    while a <= n:
        b *= n
        n -= 1
    print(b)


def perimeter_of_circle():
    """This function will calculate perimeter of circle . when you enter radius .
    This function will calculate automatically perimeter of circle and give you answer."""

    radius = float(input("Enter radius of circle :"))
    perimeter = 2 * 3.14159 * radius
    print("Perimeter of circle is", perimeter)


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
            root1 = (-b + m.sqrt(delta)) / (2 * a)
            root2 = (-b - m.sqrt(delta)) / (2 * a)
            print("Roots are REAL and UNEQUAL")
            print("Root1=", root1, ",Root2=", root2)
        elif delta == 0:
            root1 = -b / (2 * a)
            print("Roots are REAL and EQUAL")
            print("Root1=", root1, ",Root2=", root1)
        else:
            print("Roots are COMPLEX and IMAGINARY")


def square_root():
    """This is normal maths function. which will help to do square roots."""

    y = int(input("Enter number for square root :"))
    v = m.sqrt(y)
    print(v)


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


# password_generator

def passwordgenerator():
    """This is normal password generator which help to generate password.
    Digits, special letters, uppercase, lowercase letters are use to generate
    password."""

    import string
    import random
    from time import sleep

    s1 = string.ascii_letters
    s2 = string.digits
    s3 = string.punctuation

    passlen = int(input("\nEnter password length :"))
    # print(s3)
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))

    # print(s)
    print("Creating password....")
    sleep(1)
    print("Here is your password :")
    print("".join(random.sample(s, passlen)))


# txt_file

def createtxt():
    """This is normal text file crater. which can create txt file easy .
    you can easy add text or numbers into text file which you created ."""

    from time import sleep
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
            sleep(1)
            print("completed...")
    else:
        print("Thanks for using this program...")


def main():  # This is main function which have all programs

    """This is function which have all function
    All functions are running from this function .
    If this function is not here program will not run. """

    while True:
        global d  # Defined d as a global variable to use in help function
        d = str(input("\nwhat i can do for you sir :"))
        print("loading...")
        sleep(1)
        if d == "right answer":
            print("THANKS")
        # help programme to give help to user
        elif "help" in d:
            helpfor()
        # Game management programme
        elif "game" in d:
            manage_game()
        # Two game
        elif "tik tak toe" in d:
            tik_tak_toe()
        elif "number game" in d:
            number_game()
        # Normal maths function defined
        elif "calculator" in d:
            calculator()
        elif "sum of n terms" in d:
            sum_of_n_terms()
        elif "factorial" in d:
            factorialanotherway()
        elif "table" in d:
            table()
        elif "area of circle" in d:
            area_of_circle()
        elif "perimeter of circle" in d:
            perimeter_of_circle()
        elif "roots of quadratic equation" in d:
            roots_of_quadratic_equation()
        elif "square root" in d:
            square_root()
        # password generator to generate password
        elif "password generator" in d or "generate password" in d:
            passwordgenerator()
        # change password of this program
        elif "change password" in d or "password change" in d or "pswd change" in d:
            passchanger()
        elif "create txt" in d or "create text" in d or "create text file" in d:
            createtxt()
        # bye program
        elif "bye" in d or d == "exit":
            print("bye sir")
            break
        else:
            print("I don't know. what is this. \n I am a steal learning robot.")
    print("Thanks for using this program")


if __name__ == "__main__":
    passwordlogin()
