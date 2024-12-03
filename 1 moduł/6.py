import gmpy2
import time


def is_prime(n):
    if n < 2:
        return False

    sqrt_n = gmpy2.isqrt(n)

    if gmpy2.is_prime(n):
        return True
    return False


num = gmpy2.mpz(987643212340000000000000000000013)

start_time = time.time()
is_prime_result = is_prime(num)
is_prime_time = time.time() - start_time
print(f"{num} {is_prime(num)}, time: {is_prime_time} seconds")

def miller_rabin_test(n, k=5):
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    rand_state = gmpy2.random_state()

    for _ in range(k):
        a = gmpy2.mpz_random(rand_state, n)
        while a < 2:
            a = gmpy2.mpz_random(rand_state, n)

        x = gmpy2.powmod(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = gmpy2.powmod(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

start_time = time.time()
miller_rabin_result = miller_rabin_test(num)
miller_rabin_time = time.time() - start_time
print(f"{num} {miller_rabin_test(num)}, time: {miller_rabin_time} seconds")

