#!/usr/bin/env python
"""reducer.py"""

# import csv
import sys
import decimal
import pandas as pd


# Fonction pour traiter une ligne de données et mettre à jour le dictionnaire mydata
def process_line(line, commandes):
    line = line.strip()  # Supprime les espaces superflus
    cpcli, codcde, timbrecde, Nbcolis, qte, points = line.split(";")

    try:
        Nbcolis = int(Nbcolis)  # Convertit en entier
        timbrecde = round(decimal.Decimal(timbrecde), 2)  # Convertit en float
        qte = int(qte)  # Convertit en entier
        points = int(points)  # Convertit en entier
    except ValueError:
        return  # Ignorer les lignes non valides

    # calcul des points de commandes
    points_commande = max(points, 0) * qte

    # Créez une entrée pour cette commande dans le dictionnaire
    if codcde not in commandes:
        commandes[codcde] = {
            "cpcli": cpcli,
            "Nbcolis": Nbcolis,
            "timbrecde": timbrecde,
            "points_commande": points_commande,
        }
    else:
        # Mettez à jour les valeurs existantes
        commandes[codcde]["Nbcolis"] += Nbcolis
        commandes[codcde]["timbrecde"] += timbrecde
        commandes[codcde]["points_commande"] += points_commande


# Dictionnaire
commandes = {}

# Lecture de l'entrée standard
for line in sys.stdin:
    process_line(line, commandes)

# Triez le dictionnaire en fonction de la clé "points_commande"
sorted_commandes = sorted(
    commandes.items(), key=lambda x: x[1]["points_commande"], reverse=True
)


# Créez un DataFrame à partir des données
mydata = []
for codcde, values in sorted_commandes[:100]:
    mydata.append(
        [
            codcde,
            values["cpcli"],
            values["Nbcolis"],
            values["timbrecde"],
            values["points_commande"],
        ]
    )

df = pd.DataFrame(
    mydata,
    columns=[
        "codcde",
        "cpcli",
        "Nbcolis",
        "timbrecde",
        "points_commande",
    ],
)

# Enregistrez le DataFrame dans un fichier Excel
excel_file = "/datavolume1/lot2_exo1.xlsx"
df.to_excel(excel_file, index=False)
