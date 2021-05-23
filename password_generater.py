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


if __name__ == "__main__":
    passwordgenerator()
