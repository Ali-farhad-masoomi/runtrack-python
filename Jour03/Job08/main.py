def affiche_produits(type, saison):
    if type == "fruits":
        if saison == "hiver":
            print("Orange, mandarine et kiwi")
        elif saison == "ete":
            print("Poire, fraise, cassis")
        else:
            print("Saison non reconnue pour les fruits")
    elif type == "legume":
        if saison == "hiver":
            print("Carotte, topinambour, endive")
        elif saison == "ete":
            print("Artichaut, aubergine, navet")
        else:
            print("Saison non reconnue pour les légumes")
    else:
        print("Type non reconnu")

# Exemples d'appel de la fonction
affiche_produits("fruits", "hiver")
affiche_produits("fruits", "ete")
affiche_produits("legume", "hiver")
affiche_produits("legume", "ete")
affiche_produits("poisson", "printemps")  # Exemple avec un type non reconnu
