#!/usr/bin/python3


def rand(m, b, c, a=0):
    """
    Prints 20 random numbers with the PRNG used by gcc
    """
    i = 0
    while i <= 19:
        a = (b * a + c) % (m)
        i += 1
        print(a)

m = 2 ** 32
b = 1103515245
c = 12345
a = 0  # seed
rand(m, b, c, a)
