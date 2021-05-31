inp = int(input("Podaj górną granicę: "))
for x in range(0, inp):
    if x % 6 == 0 or x % 9 == 0:
        print(x)