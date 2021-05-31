w_m = int(input("Na jakiej wysokości lecimy? [W metrach]: "))
w_km = w_m / 1000
def Main():
        if w_km < 5:
            print(f"{w_km} km to za nisko!")
        else:
            print(f"Na tej wysokości ({w_km} km) jesteś już bezpieczny")
Main()