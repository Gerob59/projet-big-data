#!/usr/bin/env python
"""reducer.py"""

import sys
import decimal
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd


# Fonction pour traiter une ligne de données et mettre à jour le dictionnaire mydata
def process_line(line, commandes):
    line = line.strip()  # Supprime les espaces superflus
    cpcli, codcde, timbrecde, Nbcolis, qte, points, timbrecli, villecli = line.split(
        ";"
    )

    try:
        Nbcolis = int(Nbcolis)  # Convertit en entier
        timbrecde = round(decimal.Decimal(timbrecde), 2)  # Convertit en float
        qte = int(qte)  # Convertit en entier
        points = int(points)  # Convertit en entier
        timbrecli = round(decimal.Decimal(timbrecli), 2)
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
            "timbrecli": timbrecli,
            "villecli": villecli,
        }
    else:
        # Mettez à jour les valeurs existantes
        commandes[codcde]["Nbcolis"] += Nbcolis
        commandes[codcde]["timbrecde"] += timbrecde
        commandes[codcde]["points_commande"] += points_commande
        commandes[codcde]["timbrecli"] += timbrecli


# Dictionnaire
commandes = {}

# Lecture de l'entrée standard
for line in sys.stdin:
    process_line(line, commandes)

# Triez le dictionnaire en fonction de la clé "points_commande"
sorted_commandes = sorted(
    commandes.items(), key=lambda x: x[1]["points_commande"], reverse=True
)

top_commandes = sorted_commandes[:100]

#
filtered_commandes = [
    commande
    for commande in top_commandes
    if (
        commande[1]["cpcli"].startswith("53")
        or commande[1]["cpcli"].startswith("61")
        or commande[1]["cpcli"].startswith("28")
    )
    and commande[1]["timbrecli"] == 0.0
]

# permet d'avoir de l'aleatoire dans le tirage
random.shuffle(filtered_commandes)

# tirer 5%
x = (len(filtered_commandes) * 5) // 100

top_random_commandes = filtered_commandes[:x]

# Créez un DataFrame à partir des données
mydata = []
for codcde, values in top_random_commandes:
    mydata.append(
        [
            codcde,
            values["cpcli"],
            values["villecli"],
            values["timbrecde"],
            values["timbrecli"],
            values["Nbcolis"],
            values["points_commande"],
        ]
    )

df = pd.DataFrame(
    mydata,
    columns=[
        "codcde",
        "cpcli",
        "villecli",
        "timbrecde",
        "timbrecli",
        "Nbcolis",
        "points_commande",
    ],
)

# Enregistrez le DataFrame dans un fichier Excel
excel_file = "/datavolume1/lot2_exo2_data.xlsx"
df.to_excel(excel_file, index=False)

# Extraire les labels (noms de commandes) et les valeurs (points)
labels = []
values = []
for data in top_random_commandes:
    labels.append(data[0])
    values.append(data[1]["timbrecde"])

# Créer le graphique en secteurs
fig = plt.figure(figsize=(8, 8))
plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=140)

# Ajouter un titre
plt.title("Répartition des timbrecde")

# Créez un graphique en secteurs pour la moyenne par ville
output_pdf_file = "/datavolume1/lot2_exo2_graphique.pdf"
with PdfPages(output_pdf_file) as pdf:
    pdf.savefig()

plt.close()
