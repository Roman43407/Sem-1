from datetime import date
from datetime import timedelta
from datetime import datetime

def main():
        # Uzyskaj dzisiejszą datę z klasy datetime
    today = datetime.now()
        # Otrzymujemy aktualny czas
        # dzień tygodnia 0 (poniedziałek) do 6 (niedziela)
    yesterday = date.today() + timedelta(days=1)
    tomorrow = date.today() - timedelta(days=1)
    wd = date.weekday(today)
        # Dni zaczynają się od 0 w poniedziałek
    days = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]
    print("Dzisiaj jest numer dnia: %d" % wd)
    print("Który jest: " + days[wd])
    print("\nWczorajsza data to:", tomorrow)
    print("Bieżąca data i godzina to:", today)
    print("Jutrzejsza data to:", yesterday)

if __name__ == "__main__":
    main()

import datetime
now = datetime.datetime.today()
NY = datetime.datetime(2021,4,3)
d = NY-now
mm, ss = divmod(d.seconds, 60)
hh, mm = divmod(mm, 60)
print('\nDo Wielkanocy zostało: {} dni {} godzin {} min {} sek.'.format(d.days, hh, mm, ss))

def get_user_birthday():
    year = int(input('\nKiedy są twoje urodziny? [Rok] '))
    month = int(input('Kiedy są twoje urodziny? [Miesiąc] '))
    day = int(input('Kiedy są twoje urodziny? [Dzień] '))

    birthday = datetime(2000+year,month,day)
    return birthday

def calculate_dates(original_date, now):
    delta1 = datetime(now.year, original_date.month, original_date.day)
    delta2 = datetime(now.year+1, original_date.month, original_date.day)
    days = (max(delta1, delta2) - now).days
    return days

bd = get_user_birthday()
now = datetime.now()
c = calculate_dates(bd, now)

print("Twoje urodziny przez:", c, "dni")