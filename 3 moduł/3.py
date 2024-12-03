
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


print(bin(iloczyn(0b01010111, 0b10000011)))
