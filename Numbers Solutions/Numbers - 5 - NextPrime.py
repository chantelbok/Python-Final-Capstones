"""Have the program find prime numbers until the user chooses to stop asking for the next one."""


def is_prime(x):
    """
    Function that checks whether a value is a prime number or not
    """

    if x == 2:  # 2 is a prime number
        return True

    if x % 2 == 0:  # all even number should return False
        return False

    # since a composite number must have a factor less than the square root of that number
    for i in range(2, int(x//2)):
        if x % i == 0:
            return False

    return True


def next_prime(cp):
    """
    Returns the next prime
    after the currentPrime
    """
    # next number is current prime + 1
    nn = cp + 1

    while True:

        if not is_prime(nn):
            # if is_prime = False, add 1 to the next number (nn)
            nn += 1
        else:
            # break out of the loop is is_prime = True
            break
    # return the next number where is_prime evaluated to True
    return nn


def main():  # Wrapper function

    cp = 2

    while True:

        answer = input('Would you like to see the next prime? (Y/N) ')

        if answer.lower().startswith('y'):
            print(f'{cp} is the next prime number')
            cp = next_prime(cp)

        else:
            break


if __name__ == '__main__':
    main()
