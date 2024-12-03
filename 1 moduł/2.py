import gmpy2


def rozszerzony_algorytm_euklidesa(a, b):

    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = rozszerzony_algorytm_euklidesa(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


def oblicz_odwrotnosc(n, b):

    b = gmpy2.mpz(b)
    mod = gmpy2.mpz(n)
    gcd, x, y = rozszerzony_algorytm_euklidesa(b, mod)
    print(f"{gcd}, {x}, {y}")
    if gcd != 1:
        raise ValueError(f"({b}, {n}) != 1")

    return x % mod


n = 17
b = 3

odwrotnosc = oblicz_odwrotnosc(n, b)
print(f"Odwrotność {b} w grupie ({n}): {odwrotnosc}")