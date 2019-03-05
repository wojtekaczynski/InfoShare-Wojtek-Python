a=5.1
type (a)
print(type(a))

print("Czesc")


print(a, end="\n")
print(a, end=" Ala")

print("\n")
zmienna = "Czesc SwieciE"
# len długość słowa
print(len(zmienna))
# nawiasy [] powoduja podanie indeksu
print (zmienna [1])
print (zmienna [-1])
print ("indeks" [-1])


a= "ABCDEFG"
print(len(a))
print (a[3:4])
#przechodzeniem z krokiem -2 od końca
print (a[::-2])

# przekazywanie danych
imie = "Joanna"
print ("Hej " + imie)
wiek = 65
print ("Hej {} masz {} lat".format (imie, wiek))
#print (f "Hej {imie} masz {wiek} lat")

plik0 ="c:user\\nowy folder"
print (plik0)

plik1 =r"c:user\nowy folder"
print (plik1)

print("Czesc "*10)

#zminne bool
t = True
f = False
print(t and t)
print (not t)
print (not t and f)
print (not f or f)
print (5>4 or f)
#!= rozne
#== porównanie

print (3<2 and not 4 ==3 or 2!=0)

print("\n jajo")

liczba=23.0
print (liczba.is_integer())

a = 3
b = 4
print (int(a/b))

print (0.1 + 0.1 + 0.1 == 0.3)
print ("{:.17}".format(0.3))

#round
a=round(0.1+0.2,10)==round(0.3,10)
print(a)

#input
#wzrost = float (imput ("Twój wzrost ="))
#print ("{:.2f}".format(wzrost)

wiek = int(input("Ile masz lat = "))
print (wiek)


imie = input("Twoje imie = ")
print (imie.capitalize())

miasto = "Hamburg"
print( miasto.find("a"))