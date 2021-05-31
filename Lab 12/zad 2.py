def Main():
    print("'koniec' konczy operacje")
while True:
    x = input("Co policzymy (kula ,stozek, szescian): ")
    if x == 'koniec':
        break
    if x in ('kula' ,'stozek', 'szescian'):
        if x == 'kula':
            r = float(input("r = "))
            P = 4 * r * r * 3.14
            V = (4/3)*3.14 * r * r * r
            print(str(P))
            print(str(V))
        elif x == 'stozek':
            r = float(input("r = "))
            l = float(input("l = "))
            h = float(input("h = "))
            P = (3.14 * r * r) + (3.14 * r * l)
            V = (1/3) * 3.14 * r * r * h
            print(str(P))
            print(str(V))
        elif x == 'szescian':
            a = float(input("a = "))
            P = 6 * a * a
            V = a * a * a
            print(str(P))
            print(str(V))
    else:
        print("Nieprawidłowy znak operacji!")
Main()