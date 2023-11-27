def supprimer_doublons(liste):
    liste_unique = []  # Liste temporaire pour stocker les éléments uniques

    # Parcourir la liste d'origine
    for element in liste:
        # Vérifier si l'élément est déjà dans la liste temporaire
        if element not in liste_unique:
            liste_unique.append(element)

    # Remplacer la liste d'origine par la liste temporaire sans doublons
    liste.clear()
    liste.extend(liste_unique)

# Exemple d'utilisation
ma_liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
supprimer_doublons(ma_liste)

# Afficher la liste sans doublons
print("Liste sans doublons :", ma_liste)
