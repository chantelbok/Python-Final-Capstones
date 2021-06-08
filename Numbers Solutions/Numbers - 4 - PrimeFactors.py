"""Have the user enter a number and find all Prime Factors (if there are any) and display them."""


# prime factors: any of the prime numbers that can be multiplied to give the original number
# if the number the user entered is a prime number, then this will be irrelevant - can print "{n} is a prime nr"
# if the user entered something other than a prime number, then all the prime numbers must be generated up to n
# then check multiplication of those prime numbers to equal n

def prime_factors(n):
    ls1 = []
    n = int(n)
    for number in range(1, n + 1):
        if len(ls1) < 2:
            ls1.append(number)
        else:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                ls1.append(number)
    factors = [x for x in range(1, n + 1) if n % x == 0]
    primefacs = [num for num in factors if num in ls1 and num > 1]
    if len(primefacs) > 1:
        return primefacs
    else:
        return f'{n} is a prime number'


if __name__ == '__main__':
    print("Enter a number in the prompt for which you would like to calculate prime factors or type 'quit' to exit")
    numInput = 0

    while True:
        if numInput:
            print(prime_factors(numInput))
        print(">>>", end='')
        numInput = input()
        if numInput == "quit":
            print("Goodbye")
            break

# I can manage to print out the prime factors but not how they are multiplied to give n
