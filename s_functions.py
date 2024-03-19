
import random


# normal maths
import string


def addition(a, b):
    c = a + b
    return c


def subtract(a, b):
    c = a - b
    return c


def area_of_circle(radius):
    """This function will calculate area of circle . when you enter radius .
    This function will calculate automatically area of circle and give you answer."""

    area = 3.14159 * radius * radius
    return area


def perimeter_of_circle(radius):
    """This function will calculate perimeter of circle . when you enter radius .
    This function will calculate automatically perimeter of circle and give you answer."""

    perimeter = 2 * 3.14159 * radius
    return perimeter


def factorial(n):
    """This function is used to calculate factorial for you. In class 11 and 12 this operation used .
    This function is very useful for students. symbol used in maths for this function is !."""

    a = 1
    b = 1
    while a <= n:
        b *= n
        n -= 1
    return b

# password_generator

def passwordgenerator(passlen=8):
    """This is normal password generator which help to generate password.
    Digits, special letters, uppercase, lowercase letters are use to generate
    password."""

    s1 = string.ascii_letters
    s2 = string.digits
    s3 = string.punctuation
    # print(s3)
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    return ("".join(random.sample(s, passlen)))

def intotxtfile(question ,text):
    with open("output.txt", 'a') as f:
        f.write("\n\nQuestion: "+question+"\n")
        f.write("Answer: ")
        for i in text:
            f.write(i)