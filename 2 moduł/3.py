from gmpy2 import mpz


def negate_point(P, p):

    x, y = P
    if y == 0:
        return (x, 0)
    neg_y = (-y) % p
    return (x, neg_y)


p = mpz(17)
P = (mpz(5), mpz(7))

neg_P = negate_point(P, p)
print(f"Punkt P {P}")
print(f"Punkt przeciwny -P {neg_P}")
