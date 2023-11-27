def remplacer_valeur(liste, index):
    # Remplace la valeur à l'index par la somme des cases voisines
    if index > 0 and index < len(liste) - 1:
        liste[index] = liste[index - 1] + liste[index + 1]

# Création de la liste
L = [1, 2, 3, 4, 5]

# Afficher la deuxième valeur de la liste
deuxieme_valeur = L[1]
print(deuxieme_valeur)

# Appeler la fonction pour remplacer L[3] par la somme des cases voisines L[2] & L[4]
remplacer_valeur(L, 3)

# Afficher le tableau après la modification
print(L)

# Afficher la dernière valeur de la liste
derniere_valeur = L[-1]
print(derniere_valeur)
