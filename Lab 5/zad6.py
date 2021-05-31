import time
import random
start_time = time.time()
print("zgadnij liczbę z zakresu od 0 do 100, masz 3 szansy")
c = 0
liczba = random.randint(0, 100)

while c != 3:
    a = int(input("Podaj swoją liczbę: "))
    if a > liczba:
        print("Za duża: ")
        c += 1
        continue

    elif a < liczba:
        print("Za mała: ")
        c += 1
        continue

    else:
        print("Gratuluję, wygrałeś!")
        break

else:

    print("przegrałeś")
elapsed_time = time.time() - start_time
print("program wykonał się w :")
print(elapsed_time)