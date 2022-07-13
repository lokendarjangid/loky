from game import *
from mathfunction import *
from passmanager import *
from text import *
from morseCode import *

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
        elif "morse code" in d:
            morseEncode()
        # bye program
        elif "bye" in d or d == "exit":
            print("bye sir")
            break
        else:
            print("I don't know. what is this. \n I am a steal learning robot.")
    print("Thanks for using this program")


if __name__ == "__main__":
    passwordlogin()
