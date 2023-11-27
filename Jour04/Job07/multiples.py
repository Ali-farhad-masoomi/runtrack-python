def compter_multiples_de_trois(liste):
    # Utiliser une compréhension de liste pour filtrer les multiples de 3
    multiples_de_trois = [nombre for nombre in liste if nombre % 3 == 0]
    
    # Retourner la longueur de la liste des multiples de 3
    return len(multiples_de_trois)

# Liste donnée
L = [8, 24, 48, 2, 16]

# Appeler la fonction pour compter les multiples de 3 dans la liste
nombre_de_multiples_de_trois = compter_multiples_de_trois(L)

# Afficher le résultat
print(f"Le nombre de multiples de 3 dans la liste est : {nombre_de_multiples_de_trois}")
