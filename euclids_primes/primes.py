#!/usr/bin/python3


def is_prime(n):
    """Tells if a given number n is a prime using brute force."""
    c = 0
    for i in range(2, n):
        if n % i == 0:
            c += 1
    if c == 0:
        return True
    else:
        return False


def get_primes(n):
    """Finds the first n primes."""
    primes = [1]
    i = 1
    c = 2
    while i < n:
        prime = is_prime(c)
        if prime:
            primes.append(c)
            i += 1
        c += 1
    return primes


def euclid(n):
    """Tests the "Euclid's Proof of the Infinitude of Primes (c. 300 BC)"."""
    m = None
    primes = get_primes(n)
    print(primes)
    for n in primes:
        if m is None:
            m = n
        else:
            m = m * n
    p = m + 1
    return is_prime(p)


if __name__ == '__main__':
    # As you'll see the proof fails with the 7th prime number. It is false!
    for i in range(1, 8):
        proof = euclid(i)
        if proof is False:
            print(proof)
            break
        else:
            print(proof)
