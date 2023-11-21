# saisir un entier supérieur à zéro
while True:
    try:
        N = int(input("Entrez un entier supérieur à zéro (N) : "))
        if N > 0:
            break
        else:
            print("Veuillez saisir un entier supérieur à zéro.")
    except ValueError:
        print("Veuillez saisir un nombre entier.")

#  les tables de multiplication de 1 à N
for i in range(1, N + 1):
    print(f"\nTable de multiplication pour {i} :\n")
    for j in range(1, 11):
        resultat = i * j
        print(f"{i} x {j} = {resultat}")