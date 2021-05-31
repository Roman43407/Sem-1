m = float (input("Wpisz swoją wagę w kg: "))
h = float (input("Wpisz swój wzrost w cm: "))
h = h/100
index_mass = float(m / (h*h))
def Main():
    if float(index_mass) >= 18.5 and float(index_mass) <= 24.99:
        print ("BMI :", "%.2f" % index_mass, "Masz niedowagę")
    elif float(index_mass) >= 24.99 and float(index_mass) <= 25:
        print ("BMI :", "%.2f" % index_mass, "Twoja waga jest prawidłowa")
    elif float(index_mass) >= 25:
        print ("BMI :", "%.2f" % index_mass, "Masz nadwagę!!!")
Main()