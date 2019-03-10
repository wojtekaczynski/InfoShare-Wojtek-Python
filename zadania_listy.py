# 1L. napisz program sumujący wszystkie elementy w liscie

lista = [1, 4, 9, 16, 25]
dodawanie_listy = (lista[0]) + (lista[1]) + (lista[2]) + (lista[3]) + (lista[4])
print("Wartość dodanych elementów listy: ", dodawanie_listy)

# 2L. znajdz najwiekszy / najmniejszy element w liscie

lista = [5, 2, 3, 1, 4]
lista.sort()
print("Najmniejsz liczba z listy: ", lista [0])
print("Największa liczba z listy: ", lista [4])


# 3L. program ktory zmieni zdanie w liste wyrazow
zdanie = "Ala ma kota, kot ma Ale"

# 4L. znajdz liczbe stringow dl. min. 2, ktore zaczynaja sie i koncza na te same znaki
# ['abc', 'xyz', 'aba', '1221'] - odp = 2

# 5L. program znajdujacy wartosci, ktre wystepuja tylko raz
lista_a = [10,20,30,20,10,50,60,40,80,50,40]


# 6L. program usuwajacy zduplikowane wartosci w liscie (w miejscu! - tzn bez drugiej listy)
lista_b = [10,20,30,20,10,50,60,40,80,50,40]

lista_b = [10,20,30,20,10,50,60,40,80,50,40]
lista_b.sort()
lista_b = list(set(lista_b))
print(lista_b)

# 7L. program sprawdza czy dwie listy maja co najmniej jeden wspolny element,
# jesli tak wypisuje True

a = [11, 32, 44, 555]
b = range(55)
for element in a:
      if element in b:
          print(element, end=',')
