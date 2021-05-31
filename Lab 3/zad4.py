z3 = []
z4 = []
for i in range(100, 200):
    if (i % 2 != 0) & (i % 3 != 0):
        z3.append(i)
    if (i % 2 == 0) & (i % 3 != 5) & (i % 6 != 0) & (i % 11 != 0):
        z4.append(i)
print("Wynik zadania 3: " + str(z3))
print("Wynik zadania 4: " + str(z4))