#   +   suma
#   —   różnica
#   *   mnożenie
#   /   dzieleni
#   **  pierwiastkowanie
def Main():
    print("Zero jako znak operacji"
      "\nzakończy działanie programu")
while True:
    c = input("Co robimy? (+,-,*,/,**): ")
    if c == '0':
        break
    if c in ('+', '-', '*', '/', '**',):
        a = float(input("a = "))
        b = float(input("b = "))
        if c == '+':
            c = a + b
            print(str(c))
        elif c == '-':
            c = a - b
            print(str(c))
        elif c == '*':
            c = a * b
            print(str(c))
        elif c == '/':
            if a != 0 and b != 0:
                print(str (a / b))
            else:
                print("Dzielenie przez zero!")
        elif c == '**':
            c = a ** b
            print(str(c))
    else:
        print("Nieprawidłowy znak operacji!")
Main()