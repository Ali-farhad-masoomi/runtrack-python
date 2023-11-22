def calcule_moyenne(n1,n2,n3):
    moyenne = (n1 + n2 + n3)/3
    return moyenne

print("Saisir vos 3 notes : ")


moyenne_etudiant = calcule_moyenne(20,20,10)

print ("L'étudiant a pour moyenne ",moyenne_etudiant)

if (moyenne_etudiant>=15 and moyenne_etudiant<=20):
    print("Très bon élève")
elif (moyenne_etudiant >=11 and moyenne_etudiant <=14):
    print("Bon élève")
elif (moyenne_etudiant >= 8 and moyenne_etudiant <=10):
    print("Élève moyen")
elif (moyenne_etudiant >= 0 and moyenne_etudiant <=7):
    print("Élève devant faire des efforts")
else: print("Erreur de saisie des notes")
