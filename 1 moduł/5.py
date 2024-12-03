import gmpy2


def mod_sqrt(b, p):

    if not gmpy2.is_prime(p):
        raise ValueError("p musi być liczbą pierwszą")
    if p % 4 != 3:
        raise ValueError("p musi spełniać p ≡ 3 (mod 4)")
    b = b % p
    e = (p + 1) // 4
    root = gmpy2.powmod(b, e, p)
    return int(root)


p = gmpy2.mpz(7)
b = gmpy2.mpz(2)

root = mod_sqrt(b, p)
print(f"Pierwiastek kwadratowy {b} w Z{p} to {root}")
print(f"{root}^2 mod {p} = {root ** 2 % p}")
