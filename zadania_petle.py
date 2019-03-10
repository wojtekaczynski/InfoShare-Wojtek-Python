# 1P. program wydający resztę z dostępnych monet: 5, 2, 1, 0.5, 0.2, 0.1

# 2P. Narysuj piramidę Mario - jako input - wysokość piramidy
# np. piramida wysokości 3 ma wyglądać:
#
#   *
#  ***
# *****
#

# 3P. program, ktory obliczy ilosc liczb parzystych i nieparzystych w danym zakresie

zakres = range(1, 20)
parzyste = 0
nieparzyste = 0

for liczba in zakres:
    if liczba % 2 == 0:
        parzyste +=1
    else:
        nieparzyste +=1
print("Parzyste: {} Nieparzyste {}".format(parzyste, nieparzyste))

# 4P. program, ktory wypisze liczby od 0 do 20 poza liczbami podzielnymi przez 4

for liczba in range(21):
    if liczba % 4:
        print(liczba, end=',')

# 5P. program, ktory wypisze liczby (0 do 100) z ciagu Fibonacciego
# 0, 1, 1, 2, 3, 5, 8, 13, 21

# 6P. program wypisujący tabliczkę mnozenia (1 do 10) dla podanej liczby
# uzyc formatowania stringow!


# 7P. if elif else
# oblicz wiek psa z ludzkich lat w psich latach
# przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku
# kolejne lata, psi rok to 4 ludzkie lata
# np. 15 ludzkich lat to 73 psie lata

