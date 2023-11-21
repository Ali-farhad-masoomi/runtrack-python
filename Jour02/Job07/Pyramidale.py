chaine_initiale = "abcdefghijklmnopqrstuvwxyz" * 10

nombre_lignes = 10

index = 0
for ligne in range(1, nombre_lignes + 1):
    espace = " " * (nombre_lignes - ligne)
    caracteres = chaine_initiale[index : index + (2 * ligne - 1)]
    print(espace + caracteres + espace)
    index += (2 * ligne - 1)