import math as m


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
