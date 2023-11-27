def arrondir_et_trier(liste):
    n = len(liste)

    # Arrondir les nombres dans la liste
    for i in range(n):
        liste[i] = int(liste[i] + 0.5)  # Arrondir à l'entier le plus proche

    # Tri à bulles
    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]

# Exemple d'utilisation
ma_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
arrondir_et_trier(ma_liste)

# Afficher la liste arrondie et triée
print("Liste arrondie et triée :", ma_liste)
