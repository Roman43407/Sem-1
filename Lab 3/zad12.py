import random

orel = 0
resh = 0
count = 0
while count != 50:
    mon = random.randint(1, 2)
    count += 1
    if mon == 1:
        orel += 1

    elif mon == 2:
        resh += 1

print("Orzeł upadł", orel)
print("Reshka upadła", resh)