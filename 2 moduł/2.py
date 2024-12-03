from gmpy2 import mpz, mpz_random, powmod, is_prime, random_state
import random

def random_point_on_curve(A, B, p):

    if not is_prime(p):
        raise ValueError("p nie jest liczba pierwsza")
    if (p % 4) != 3:
        raise ValueError("nie spelnia p ≡ 3 (mod 4)")


    while True:
        x = mpz(random.randint(0, p-1))
        reszta_kw = (pow(x, 3) + A * x + B) % p

        if powmod(reszta_kw, (p - 1) // 2, p) == 1:
            y = powmod(reszta_kw, (p + 1) // 4, p)
            return int(x), int(y)


p = mpz(1018517988167243043134222844204689080525734196832968125318070224677190649881668353091699131)
A = mpz(519180478281835417500898517204494480791323919506089796732320469884632348030745189618253931)
B = mpz(1005835284264579218587573711093312574434924483405368871084485155206464286609183742251755578)

point = random_point_on_curve(A, B, p)
print(f"Losowy punkt na krzywej P = {point}")
