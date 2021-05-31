import math

def Main():
    namesOfDef = list(input("Wybierz jednostke wejściową oraz wyjściową: C - Celsjusz, K - Kelwin, F - Fahrenheit"))
    value = int(input("podaj wartość temperatury"))
    if namesOfDef[0] == "K":
        Kelwin(value, namesOfDef)
    elif namesOfDef[0] == "F":
        Fahrenheit(value, namesOfDef)
    else:
        Celsjusz(value, namesOfDef)



def Kelwin(value, namesOfDef):
    if namesOfDef[1] == "C":
        print(value + 273)
    else:
        print(value - 255)


def Fahrenheit(value, namesOfDef):
    if namesOfDef[1] == "C":
        print(value - 32)
    else:
        print(value + 255)


def Celsjusz(value, namesOfDef):
    if namesOfDef[1] == "K":
        print(value - 273)
    else:
        print(value + 32)

Main()