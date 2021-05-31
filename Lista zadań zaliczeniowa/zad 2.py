def main():
    cena = float(input("Twoja wypłata: "))
    procent = 0.058     # Zaliczka na podatek - 5,8%
    procent1 = 0.078    # Ubezpieczenie zdrowotne - 7,8%
    procent2 = 0.024    # Ubezpieczenie chorobowe - 2,4%
    procent3 = 0.015    # Ubezpieczenie rentowe - 1,5%
    procent4 = 0.098    # Ubezpieczenie emerytalne - 9,8%
    procent5 = 0.02     # Fundusz Pracy - 2%
    procent6 = 0.001    # FGŚP - 0,10%
    result = (cena * procent) + (cena * procent1) + (cena * procent2) + (cena * procent3) + (cena * procent4) + (cena * procent5) + (cena * procent6)
    result2 = cena + result
    print("Zaliczka na podatek:", round(cena * procent))
    print("Ubezpieczenie zdrowotne:", round(cena * procent1))
    print("Ubezpieczenie chorobowe:", round(cena * procent2))
    print("Ubezpieczenie rentowe:", round(cena * procent3))
    print("Ubezpieczenie emerytalne:", round(cena * procent4))
    print("Fundusz Pracy:", round(cena * procent5))
    print("FGŚP:", round(cena * procent6))
    print("Kwota za wszystkie usługi:", round(result))
    print("Twoja wypłata (kwota netto):", round(result2))
main()