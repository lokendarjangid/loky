from game import *
from mathfunction import *
from passmanager import *


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
