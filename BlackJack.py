card0 = str(input("Podaj pierwsza karte")) #7
card1 = str(input("Podaj pierwsza karte")) #A

punkty_min = 0
punkty_max = 0
high_card_points = 10
low_ace_points  = 1
high_ace_points  = 1

if card0 in "23456789":
    punkty_min = punkty_min + input(card0)
    punkty_max = punkty_max + input(card0)
elif card0 in "JQK":
    punkty_min = punkty_min + high_card_points
    punkty_max = punkty_max + high_card_points
elif card0 in "A":
    punkty_min = punkty_min + low_ace_points
    punkty_max = punkty_max + high_ace_points

if card1 in "23456789":
    punkty_min = punkty_min + input(card1)
    punkty_max = punkty_max + input(card1)
elif card1 in "JQK":
    punkty_min = punkty_min + high_card_points
    punkty_max = punkty_max + high_card_points
elif card1 in "A":
    punkty_min = punkty_min + low_ace_points
    punkty_max = punkty_max + high_ace_points

## decydujemy czy dobrać czy nie?

if punkty_min == 21 or punkty_max == 21:
    print("stop, masz 21 punktów")
elif   punkty_min > 18 or punkty_max > 18:
    print ("stop masz co najmniej 19 punktów")
else:
    print("jeszcze jedna")