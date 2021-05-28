"""Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number
Two separate functions, one where n specifies the list length and second where n specifies the max value
in the fibonacci sequence"""


def fibonacci(n):
    """ Function that takes in a number "n" and generates a fibonacci sequence of length "n" """
    ls1 = []
    for number in range(n):
        if len(ls1) < 2:
            ls1.append(number)
        else:
            ls1.append(sum(ls1[-2:]))
    return ls1


print(fibonacci(10))


def fibonacci2(n):
    """ Function that takes in a number "n" and generates a fibonacci sequence of length "n" """
    ls1 = []
    for number in range(n):
        if len(ls1) < 2:
            ls1.append(number)
        else:
            if max(ls1) < n:
                ls1.append(sum(ls1[-2:]))
    for fibo in ls1:
        if fibo > n:  # there will be more efficient ways to do this
            ls1.pop()
    return ls1


print(fibonacci2(10))
