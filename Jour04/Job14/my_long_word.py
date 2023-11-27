def is_separator(char):
    """
    Vérifie si le caractère est un séparateur (espace, virgule, point, etc.).
    """
    separators = [' ', ',', '.', ';', ':', '!', '?']
    return char in separators

def my_long_word(longueur_min, phrase):
    """
    Retourne les mots de la phrase ayant une longueur supérieure à longueur_min.
    """
    mots = []  # Liste pour stocker les mots qui satisfont la condition
    mot_actuel = ""  # Variable pour stocker le mot en cours de lecture

    # Parcourir chaque caractère de la phrase
    for char in phrase:
        if is_separator(char):
            # Si le caractère est un séparateur, ajouter le mot actuel à la liste s'il satisfait la condition
            if len(mot_actuel) > longueur_min:
                mots.append(mot_actuel)
            mot_actuel = ""  # Réinitialiser le mot actuel
        else:
            # Si le caractère n'est pas un séparateur, ajouter le caractère au mot actuel
            mot_actuel += char

    # Ajouter le dernier mot s'il satisfait la condition
    if len(mot_actuel) > longueur_min:
        mots.append(mot_actuel)

    # Retourner les mots sous forme d'une seule chaîne de caractères
    return ' '.join(mots)

# Exemple d'utilisation
resultat = my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")

# Afficher le résultat
print("Output :", resultat)
