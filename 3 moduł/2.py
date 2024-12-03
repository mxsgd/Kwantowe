def xtime(a):
    if a & 0b10000000:
        return ((a << 1) ^ 0b11011) & 0b11111111
    else:
        return (a << 1) & 0b11111111


result = xtime(0b11010111)

print(bin(result))
