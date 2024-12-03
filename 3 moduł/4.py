

def iloczyn(a, b):

    result = 0
    for i in range(8):
        if b & 1:
            result ^= a
        buff = a & 0b10000000
        a = (a << 1) & 0b11111111
        if buff:
            a ^= 0b00011011
        b >>= 1
    return result


def odwrotnosc(a):

    if a == 0:
        raise ValueError("Brak elementu odwrotnego dla 0 w F_2^8")
    t, new_t = 0, 1
    r, new_r = 0b100011101, a
    while new_r != 0:
        iloraz = r // new_r
        t, new_t = new_t, t ^ iloczyn(iloraz, new_t)
        r, new_r = new_r, r ^ iloczyn(iloraz, new_r)
    if r > 1:
        raise ValueError(f"{a} nie jest odwracalne w F_2^8")
    return t


print(bin(odwrotnosc(0b01010111)))