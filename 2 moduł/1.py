from gmpy2 import is_prime, mpz_random, next_prime, powmod, mpz, random_state
import random
def generate_random_elliptic_curve(p):

    if not is_prime(p):
        raise ValueError("p nie jest liczba pierwsza")
    if (p % 4) != 3:
        raise ValueError("nie spelnia p ≡ 3 (mod 4)")


    while True:
        A = mpz(random.randint(0, p))
        B = mpz(random.randint(0, p))

        discriminant = (4 * powmod(A, 3, p) + 27 * powmod(B, 2, p)) % p
        if discriminant != 0:
            return A, B


p = next_prime(1018517988167243043134222844204689080525734196832968125318070224677190649881668353091699131)
A, B = generate_random_elliptic_curve(p)
print(f"Wspolczynniki krzywej A = {A}, B = {B}")
print(f"Liczba pierwsza p = {p}")
