from gmpy2 import mpz, invert

def point_add(P, Q, A, p):
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and y1 == -y2 % p:
        return None
    if P == Q:
        lam = (3 * x1**2 + A) * invert(2 * y1, p) % p
    else:
        lam = (y2 - y1) * invert(x2 - x1, p) % p

    x3 = (lam**2 - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p

    return x3, y3


def scalar_multiply(n, P, A, p):

    result = None
    add = P
    while n > 0:
        if n & 1:
            result = point_add(result, add, A, p)
        add = point_add(add, add, A, p)
        n >>= 1

    return result


p = mpz(17)
A = mpz(2)
B = mpz(3)
P = (mpz(5), mpz(1))
n = mpz(7)

result = scalar_multiply(n, P, A, p)
print(f"{n} * {P} = {result}")
