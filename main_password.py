import pickle
from time import sleep


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

    from main import main
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
