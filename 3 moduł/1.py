def suma(x, y):

    return (x | y) & ~(x & y)


xy = 0b11001010
uw = 0b10110101

wynik = suma(xy, uw)
print(f"Suma {bin(xy)} + {bin(uw)} = {bin(wynik)}")
