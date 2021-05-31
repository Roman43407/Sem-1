a = float(input("Podaj liczbę: "))
b = float(input("Podaj liczbę: "))
c = float(input("Podaj liczbę: "))

while True:
    a = float(input("Podaj liczbę: "))
    b = float(input("Podaj liczbę: "))
    if a < 0 or b < 0:
        continue
    else:
        print("Średnia to: ", (a+b)/2)