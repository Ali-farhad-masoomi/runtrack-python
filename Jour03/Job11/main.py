def time_to_text(minutes):
    if isinstance(minutes, int) and minutes >= 0:
        heures = minutes // 60
        minutes_restantes = minutes % 60

        if heures == 2 and minutes_restantes == 40:
            print("2 heures et 40 minutes")
        else:
            if heures == 0:
                if minutes == 1:
                    print(f"{minutes} minute")
                else:
                    print(f"{minutes} minutes")
            elif heures == 1:
                if minutes_restantes == 0:
                    print("1 heure")
                elif minutes_restantes == 1:
                    print("1 heure et 1 minute")
                else:
                    print(f"1 heure et {minutes_restantes} minutes")
            else:
                if minutes_restantes == 0:
                    print(f"{heures} heures")
                elif minutes_restantes == 1:
                    print(f"{heures} heures et 1 minute")
                else:
                    print(f"{heures} heures et {minutes_restantes} minutes")
    else:
        print("Veuillez entrer un nombre entier positif.")

# Appel de la fonction avec 2 heures et 40 minutes
time_to_text(160)
