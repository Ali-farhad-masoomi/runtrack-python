def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        # Assurez-vous que vous ne divisez pas par zéro
        if num2 != 0:
            return num1 / num2
        else:
            return "Erreur : Division par zéro"
    elif operator == '%':
        # Assurez-vous que vous ne faites pas de modulo par zéro
        if num2 != 0:
            return num1 % num2
        else:
            return "Erreur : Modulo par zéro"
    else:
        return "Erreur : Opérateur non valide"

# Exemples d'appel de la fonction
resultat_addition = calcule(5, '+', 3)
resultat_multiplication = calcule(4, '*', 6)
resultat_division = calcule(8, '/', 2)

# Affichage des résultats
print("Résultat de l'addition :", resultat_addition)
print("Résultat de la multiplication :", resultat_multiplication)
print("Résultat de la division :", resultat_division)
