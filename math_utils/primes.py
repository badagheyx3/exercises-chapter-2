def isprime(n):
    """function that takes an integer and identifies whether it is prime or otherwise"""

    # define a variable
    badaghey = False

    # special case
    if n == 1:
        badaghey = True

    # checking for divisors
    if abs(n) > 1:
        for i in range(2,n):
            if (n % i) == 0:
                badaghey = True
                break

    # check if variable is true
    if badaghey:
        return False
    else:
        return True

