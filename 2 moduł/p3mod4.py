from gmpy2 import is_prime, mpz_random, next_prime, powmod, mpz, random_state

warunek = False
p = mpz(pow(2,299))
p = next_prime(p)

while not warunek:
    if p % 4 == 3:
        warunek = True
    else:
        p = (next_prime(p))

print(p)