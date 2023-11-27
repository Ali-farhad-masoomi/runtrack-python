def afficher_deuxieme_element():
    fruits = ["pomme", "cerise", "orange"]
    
    # Assurez-vous que la liste a au moins deux éléments avant d'essayer d'accéder au deuxième élément
    if len(fruits) >= 2:
        deuxieme_element = fruits[1]
        print(deuxieme_element)
    else:
        print("La liste ne contient pas assez d'éléments.")

# Appel de la fonction
afficher_deuxieme_element()
