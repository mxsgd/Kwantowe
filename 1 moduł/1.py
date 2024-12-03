from gmpy2 import mpz, random_state, mpz_random



def losowy_element_zn(k):

    n = mpz(2) ** k
    rand_state = random_state()
    b = mpz_random(rand_state, n)

    return mpz(b)


k = mpz(2000000)
random_number = losowy_element_zn(k)
print(random_number)