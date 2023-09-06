#!/usr/bin/env python
"""reducer.py"""

import sys
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt


# Fonction pour traiter une ligne de données et mettre à jour le dictionnaire mydata
def process_line(line, mydata):
    line = line.strip()  # Supprime les espaces superflus
    annee, codobj, qte, libobj = line.split(";")

    try:
        qte = int(qte)  # Convertit en entier
    except ValueError:
        return  # Ignorer les lignes non valides

    # Crée un dictionnaire pour l'objet s'il n'existe pas déjà
    if codobj not in mydata:
        mydata[codobj] = {"libobj": libobj}

    # Met à jour la quantité vendue pour l'année donnée
    if annee not in mydata[codobj]:
        mydata[codobj][annee] = {"qte": qte}
    else:
        mydata[codobj][annee]["qte"] += qte


# Fonction pour imprimer les données
def create_plt(mydata):
    plt.figure()
    for codobj, data in mydata.items():
        libobj = data["libobj"]
        x_values = []  # Liste pour les années
        y_values = []  # Liste pour les quantités

        for annee, info in data.items():
            if annee == "libobj":
                continue  # Exclut la clé "libobj" en sautant l'itération
            qte = info["qte"]
            x_values.append(annee)
            y_values.append(qte)

        plt.plot(x_values, y_values, label=libobj)


# Dictionnaire
mydata = {}

# Lecture de l'entrée standard
for line in sys.stdin:
    process_line(line, mydata)

# Appel de la fonction pour imprimer les données
create_plt(mydata)

# Créez un graphique en secteurs pour la moyenne par ville
output_pdf_file = "/datavolume1/lot1_exo3.pdf"
with PdfPages(output_pdf_file) as pdf:
    pdf.savefig()
