import gmpy2


def jest_reszta(b, p):

    b = b % p
    exp = (p - 1) // 2
    result = gmpy2.powmod(b, exp, p)

    return result == 1


p = gmpy2.mpz(7)
b = gmpy2.mpz(2)

is_residue = jest_reszta(b, p)
print(is_residue)
