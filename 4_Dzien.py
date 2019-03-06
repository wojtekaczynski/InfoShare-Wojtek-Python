# 1

x = True
while x:
    print(x)
    x=False
print("juz po za wihile")

# 2
password = input ("podaj hasło ")
while len(password) <6:
    print("Twoje hasło")
    password = input("podaj nowe hasło")

print(f"twoje haslo to {password} a jego dlugosc to {len(passsword}")
print("twoje haslo to {password} a jego dlugosc to {len(passsword}")

#3
i = 1
while i <100 :
    print(i)
    i += 1 # to samo i = i + 1

#4
moj_zakres = range (3,10)
for i in moj_zakres:
    print(i)

#5
nazwisko = "kowalski"
    for literka in nazwisko[::2]:
        print(literka.upper())

#6
nazwisko = "kowalski"
litery = list (nazwisko)
print(litery)

#7
myList = [1,2,3,4,5]
for cyfra in myList:
    print(cyfra)

#8
.Join

#9
lista_zakupow =["jajko", "pies", "kura"]
#opcka 1 z for
for rzecz_do_kupienia in lista_zakupow:
    print(rzecz_do_kupienia)
co_kupic = ",".join(lista_zakupow)
print(co_kupic)

#10
magic = "dsdsdsdsd"
for i in range(len(magic)):
    print(i, magic[i])

#11
moj_zakres = range(10)
lista_z_zakreu = list (moj_zakres)
print(lista_z_zakreu)

for i in moj_zakres:
    print (i, end = ",")
print()
for i in lista_z_zakreu:
    print(i, end= ",")

# policzyć liczby parzyste i nieparzyste w zakresie

zakres = range(1, 101)
parzyste = 0
nieparzyste = 0

for liczba in zakres:
    if liczba % 2 == 0
        parzyste +=1
    else:
        nieparzyste +=1
print("Parzyste: {} Nieparzyste {}".format(parzyste, nieparzyste))


# policz samogloski i spolgloski
zdanie = input("Podaje zdanie: ")

samogloski = 0
spolglowski = 0

lista_samogl = "aeiuyąęó"
for litera in zdanie:
    if litera.isalpha():
        if litera in lista_samogl:
            samogloski += 1
        else:
            spolglowski += 1
print(f"samoglosek: {samogloski}, spółgłosek: {spolglowski}")


# wydwanie reszty po zakupie

reszta = float(input("Ile mam wydac reszty: "))
dostepne_monety = [ 5, 2, 1, 0.5, 0.2, 0.1]
reszta_w_monetach = []

while (reszta >= 0.1):
    for moneta in dostepne_monety:
        # Jęsli moneta ma mniejsz wartość niż reszta to mozemu dodać monete do monet w rezcie
        if moneta <= reszta:
            #wydaje moenete
            reszta_w_monetach.append(moneta)
            # a teraz liczymy ile pozostało pieniędzy do wydania
            reszta = reszta - moneta
            break
czy_reszta = input("Mogę być winna gorsika?")
if czy_reszta.lower()== "NIE":
    reszta_w_monetach.append(0.1)
    print("wsystkie moenty: ")
for moneta in reszta_w_monetach:
    print(" {}zl, ".format (moneta), end ="")

# chcemy wyrysować wierzę z gwiazdek 3 geiazki to trzy poziomy, 5 giwazdek - 5 poziomow

wysokosc = int(input("Podaj wysokosc"))
#2n-1
napis_poczatek = "*" (2 * wysokosc - 1)
spacja = ""
while len(napis_poczatek) >1:
    print("{}{}".format(spacja, napis_poczatek))
    if len(napis_poczatek) >2:
        napis_poczatek = napis_poczatek[:-2]
    spacja = spacja + " "
