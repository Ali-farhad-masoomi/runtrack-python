def tri_bulles(liste):
    n = len(liste)

    # Parcourir tous les éléments de la liste
    for i in range(n):
        # Derniers i éléments sont déjà triés, pas besoin de les re-vérifier
        for j in range(0, n-i-1):
            # Échanger si l'élément trouvé est plus grand que le suivant
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]

# Exemple d'utilisation
ma_liste = [64, 34, 25, 12, 22, 11, 90]
tri_bulles(ma_liste)

# Afficher la liste triée
print("Liste triée :", ma_liste)
