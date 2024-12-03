import gmpy2


def modular_exp(b, k, n):

    result = gmpy2.mpz(1)
    podst = b
    exp = k

    while exp > 0:
        if exp % 2 == 1:
            result = (result * podst) % n
        podst = (podst * podst) % n
        exp //= 2

    return int(result)


n = gmpy2.mpz(17)
b = gmpy2.mpz(7)
k = gmpy2.mpz(13)

result = modular_exp(b, k, n)
print(f"{b}^{k} mod {n} = {result}")
