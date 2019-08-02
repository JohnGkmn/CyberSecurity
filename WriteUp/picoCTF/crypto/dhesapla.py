def egcd(a, b):
    """
    Euclid's Extended GCD algorithm.
    https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    """

    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)

    return g, x - (b // a) * y, y



def modinv(a, m):
    """
    Modular inverse using the e-GCD algorithm.
    https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Computing_multiplicative_inverses_in_modular_structures
    """

    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m
