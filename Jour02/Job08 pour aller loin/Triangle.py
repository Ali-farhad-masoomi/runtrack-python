# de saisir les trois longueurs
a = float(input("Entrez la longueur a : "))
b = float(input("Entrez la longueur b : "))
c = float(input("Entrez la longueur c : "))

if a + b > c and a + c > b and b + c > a:
    print("Il est possible de construire un triangle.")
    
    if a == b == c:
        print("Le triangle est équilatéral.")
    elif a == b or a == c or b == c:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Le triangle est rectangle et isocèle.")
        else:
            print("Le triangle est isocèle mais non rectangle.")
    else:
        print("Le triangle est quelconque.")
else:
    print("Il n'est pas possible de construire un triangle avec ces longueurs.")