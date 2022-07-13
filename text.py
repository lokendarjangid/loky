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


if __name__ == "__main__":
    createtxt()