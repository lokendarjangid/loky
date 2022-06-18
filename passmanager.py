import pickle
from time import sleep
from main import main
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
    else:
        print("Username/Password is wrong.")
        print("Try again!!!")
        passwordlogin()


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

