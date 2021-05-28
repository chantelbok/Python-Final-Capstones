"""Enter a number and have the program generate e up to "n" many decimal places. Keep a limit to how far the
program will go. """

# math module allows easy use of mathematical expressions
import math


def e_dec(n=2):
    """Very simple function to return e with 'n' decimal places"""
    if n > 10:
        return "Please supply value equal to or less than 10"
    else:
        return round(math.e, n)


print(e_dec(6))


# can make the program a bit more interesting

def input_dec():
    a = 1
    while a == 1:

        result = int(input("How many decimals for pi? Max number of decimals is 10 "))
        print(e_dec(result))
        yn = input("Do you want to try again? Please enter y or n ")
        if yn.lower() == "y":
            continue
        elif yn.lower() == "n":
            print("Goodbye")
            break
        else:
            print("Please only supply y or n ")
            continue


input_dec()
