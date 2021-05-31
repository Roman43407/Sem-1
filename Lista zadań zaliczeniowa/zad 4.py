def Main():
    Roz = float(input("Rozmiar dysku twardego: "))
    Gb = 1024 # Megabajtów
    Mb = 1024 # Kilobajtów
    Kb = 1024 # Bajtów
    result = Roz * Gb
    result1 = Roz * Mb * Mb * Mb
    result2 = Roz * Kb * Kb * Kb * Kb
    print(round(result), "- Megabajtów")
    print(round(result1), "- Kilobajtów")
    print(round(result2), "- Bajtów")
Main()