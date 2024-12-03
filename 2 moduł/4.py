from gmpy2 import mpz, invert


def add_points(P, Q, A, p):
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 + y2) % p == 0:
        return None
    if P != Q:
        lam = ((y2 - y1) * invert(x2 - x1, p)) % p
    else:
        if y1 == 0:
            return None
        lam = ((3 * x1 ** 2 + A) * invert(2 * y1, p)) % p

    x3 = (lam ** 2 - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p

    return (int(x3), int(y3))


p = mpz(17)
A = mpz(2)
B = mpz(3)

P = (mpz(5), mpz(1))
Q = (mpz(6), mpz(3))

result = add_points(P, Q, A, p)
print(f"Punkt P {P}")
print(f"Punkt Q {Q}")
print(f"Suma P (+) Q {result}")
