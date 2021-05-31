sumaS = 0
liczby = 0
for i in range(0,101):
    sumaS += i**3
    if sumaS > 10**6:
        liczby = i
    else:
        continue
print("Potrzebna ilość liczb naturalnych: ", liczby)
print("Suma szeescianow ", sumaS)