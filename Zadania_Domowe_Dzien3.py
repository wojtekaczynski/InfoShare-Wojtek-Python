# 1. sprawdź czy jest wygrana w kółko i krzyżyk
#   input: string 9 znaków x, o, n
#   znaki oznaczają pozycje wierszami od gornego

gra = "xox" \
      "oxo" \
      "xox"
if (gra [0] == gra [4] == gra[8]) or (gra [2] == gra [4] == gra[6]):
    if not gra[4] == ".":
        print("Wygrał")
elif (gra [0] == gra [4] == gra[8]) or (gra [2] == gra [4] == gra[6]):
        print("Wygrał")

# 2. obliczanie roku przestępnego
# podzielny przez 4, nie podzielny przez 100 ale podzielny przez 400

rok = input(" podaj rok: ")
rok = int(rok)
# % - modulo
if rok % 400 == 0:
    print("rok jest przestepny")
elif rok % 4 == 0 and rok % 4 !=0:
    print("rok jest przestepny")
else:
    print("nie jest podzielny")


# 3. czy liczba jest podzielna przez 3, 5, 7

dane = input("poda liczbe: ")
dane = int(dane)
if dane.isdigit() and int(dane) !=0:
    liczba = int(dane)
if liczba % 3 == 0:
    print ("podzielna przez 3")
if liczba % 5 == 0:
    print("podzielna przez 5")
if liczba % 7 == 0:
    print("podzielna przez 7")

# 4. oblicz ocenę na podstawie progu procentowego

procent_oceny = int(input("Podaj procent swojego testu: "))
#ujednolicenie_procent = int(procent_oceny)

if (procent_oceny >=100 and procent_oceny <=80):
    print("Dostałeś piątkę")
elif (procent_oceny >=79 and procent_oceny <=50):
    print("Dostałeś czwórkę")
elif (procent_oceny >=49 and procent_oceny <=30):
    print("Dostałeś trójkę")
elif procent_oceny >=29:
    print("Dostałeś dwójkę")

# 5. ruletka: otrzymawszy liczbę, sprawdź czy jest ona:
#   czerwona czy czarna*
#   wysoka czy niska (do 18, od 18)
#   parzysta czy nieparzysta

# - NIE JESTEM W STANIE ZNALEŻĆ ROZWIĄZNANIA

# 6. blackjack - na inpucie wejście 2 karty
#   wartości: 2-9, J Q K = 10, A = 1 lub 11
#   określ ruch jaki powinien być wykonany:
#   jeszcze jedna karta, stop,

# - NIE JESTEM W STANIE ZNALEŻĆ ROZWIĄZNANIA

# 7. po podaniu nazwy miesiaca, program napisze ilosc dni w miesiacu

miesiac = input("podaj miesiac: ")
ujednolicenie = miesiac.lower()
if ujednolicenie == "styczen":
    print("31 dni w miesiącu")
elif ujednolicenie == "luty":
    print("28 dni w miesiącu")
elif ujednolicenie == "marzec":
    print("31 dni w miesiącu")
elif ujednolicenie == "kwiecien":
    print("30 dni w miesiącu")
elif ujednolicenie == "maj":
    print("31 dni w miesiącu")
elif ujednolicenie == "czerwiec":
    print("30 dni w miesiącu")
elif ujednolicenie == "lipiec":
    print("31 dni w miesiącu")
elif ujednolicenie == "sierpien":
    print("31 dni w miesiącu")
elif ujednolicenie == "wrzesien":
    print("30 dni w miesiącu")
elif ujednolicenie == "pazdziernik":
    print("31 dni w miesiącu")
elif ujednolicenie == "listopad":
    print("30 dni w miesiącu")
elif ujednolicenie == "grudzien":
    print("31 dni w miesiącu")
else:
    print("Podałeś miesiąc, kótry nie istnieje lub podaj nazwę miesiąca bez PL znaków")

# 8. podane 3 boki trojkata, okresl
#     - czy uda sie narysowac trojkata
#       * dl. jednego boku musi byc < dlugosc sumy dwoch pozostalych
#     - czy jest to tr. roznoboczny, rownoramienny czy rownoboczny

# - NIE JESTEM W STANIE ZNALEŻĆ ROZWIĄZNANIA


# 9. inupt - miesiąc oraz dzien,
#   okreslic pore roku

miesiac = input("Podaj miesiac: ")
dzien=input("Podaj dzień miesiąca: ")
ujednolicenie_miesiac = miesiac.lower()
ujednolicenie_dzien = int(dzien)

if ujednolicenie_miesiac == "styczen" and (ujednolicenie_dzien >=1 and ujednolicenie_dzien <=31):
    print("Pora roku: Zima")
elif ujednolicenie_miesiac == "luty" and (ujednolicenie_dzien >=1 and ujednolicenie_dzien <=28):
    print("Pora roku: Zima")
elif ujednolicenie_miesiac == "marzec" and (ujednolicenie_dzien >=1 and ujednolicenie_dzien <=19):
    print("Pora roku: Zima")
elif ujednolicenie_miesiac == "marzec" and (ujednolicenie_dzien >=20 and ujednolicenie_dzien <=31):
    print("Pora roku: Wiosna")
elif ujednolicenie_miesiac == "kwiecien" and (ujednolicenie_dzien >=1 and ujednolicenie_dzien <=30):
    print("Pora roku: Wiosna")
elif ujednolicenie_miesiac == "maj" and (ujednolicenie_dzien >=1 and ujednolicenie_dzien <=31):
    print("Pora roku: Wiosna")
elif ujednolicenie_miesiac == "czerwiec" and (ujednolicenie_dzien >=1 and ujednolicenie_dzien <=20):
    print("Pora roku: Wiosna")
elif ujednolicenie_miesiac == "czerwiec" and (ujednolicenie_dzien >=21 and ujednolicenie_dzien <=30):
    print("Pora roku: Lato")
elif ujednolicenie_miesiac == "lipiec" and (ujednolicenie_dzien >=1 and ujednolicenie_dzien <=31):
    print("Pora roku: Lato")
elif ujednolicenie_miesiac == "sierpien" and (ujednolicenie_dzien >=1 and ujednolicenie_dzien <=31):
    print("Pora roku: Lato")
elif ujednolicenie_miesiac == "wrzesien" and (ujednolicenie_dzien >=1 and ujednolicenie_dzien <=21):
    print("Pora roku: Lato")
elif ujednolicenie_miesiac == "wrzesien" and (ujednolicenie_dzien >=22 and ujednolicenie_dzien <=30):
    print("Pora roku: Jesień")
elif ujednolicenie_miesiac == "pazdziernik" and (ujednolicenie_dzien >=1 and ujednolicenie_dzien <=31):
    print("Pora roku: Jesień")
elif ujednolicenie_miesiac == "listopad" and (ujednolicenie_dzien >=1 and ujednolicenie_dzien <=30):
    print("Pora roku: Jesień")
elif ujednolicenie_miesiac == "grudzien" and (ujednolicenie_dzien >=1 and ujednolicenie_dzien <=20):
    print("Pora roku: Zima")
elif ujednolicenie_miesiac == "grudzien" and (ujednolicenie_dzien >=21 and ujednolicenie_dzien <=31):
    print("Pora roku: Zima")
else:
    print("Podałeś miesiąc, kótry nie istnieje")
    print("Podaj nazwę miesiąca bez PL znaków")
    print("Podałeś ilość dni większą niż dany miesiąc")

# 10. zamiana temperatury
#     wejscie: "35C" "100F"
#     wyjście "Temperatura w {typ} to {xxx} stopni"
#     C = (F - 32) * (5/9)
#     F = C * (9 / 5) + 32

# Nie udało mi się. Chciałem wyciągnąć zgodnie z wejsciem (z zapisu 35F lub 35C) literę F lub C by program wiedział jaki wzór użyć a następnie wyciągnąć
# samą licznę by podstawić ją pod wzór coś na styl:
podaj_temp = input("Podaj temperaturę np 35F lub 35C: ")
rozdzielenie_rodzaj = (podaj_temp [-1]).lower()
rozdzielenie_wartosc = podaj_temp.replace("f","0") or podaj_temp.replace("c","0")
print(rozdzielenie_rodzaj)
print(rozdzielenie_wartosc)
if rozdzielenie_rodzaj == "c":
    F = rozdzielenie_wartosc * (9 / 5) + 32
print(F)
if rozdzielenie_rodzaj == "f":
    C = (rozdzielenie_wartosc - 32) * (5 / 9)
print(C)