a=input("Wpisz długość pomieszczenia = ")
b=input("Wprowadź szerokość pomieszczenia = ")
c=input("Podaj wysokość pomieszczenia = ")
m1= float(a)*float(b)*2
m2= (float(a)*float(c)*2)+(float(b)*float(c)*2)
m3= float(m1)+float(m2)

wynik = float(a)*float(c)*float(b)

wynik2= str(wynik)
m4= str(m3)

print ("Objętość wynosi: "+wynik2)
print("Pole całkowite wynosi: "+m4)
