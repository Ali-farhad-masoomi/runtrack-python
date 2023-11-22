def verifie_pair_impair(nombre):
    if isinstance(nombre, int) and nombre >= 0:
        if nombre % 2 == 0:
            return "pair"
        else:
            return "impair"
    else:
        return "Le nombre n'est pas un chiffre entier positif"

# Appels de la fonction avec différentes valeurs
resultat1 = verifie_pair_impair(6)
resultat2 = verifie_pair_impair(13)
resultat3 = verifie_pair_impair(0)
resultat4 = verifie_pair_impair(-5)
resultat5 = verifie_pair_impair("non_entier")

# Affichage des résultats
print("6 est", resultat1)
print("13 est", resultat2)
print("0 est", resultat3)
print("-5 est", resultat4)
print("\"non_entier\" est", resultat5)
