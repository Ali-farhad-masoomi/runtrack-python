def echanger_premier_et_dernier(liste):
    if len(liste) >= 2:
        # Échanger les valeurs de la première et de la dernière case
        liste[0], liste[-1] = liste[-1], liste[0]

# Liste initiale
ma_liste = [1, 2, 3, 4, 5]

# Afficher la liste initiale
print(ma_liste)

# Appeler la fonction pour échanger les valeurs
echanger_premier_et_dernier(ma_liste)

# Afficher la liste après l'échange
print(ma_liste)
