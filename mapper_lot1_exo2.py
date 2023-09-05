#!/usr/bin/env python
"""mapper.py"""

import sys
import csv

# Créez un lecteur CSV pour gérer les données
csv_reader = csv.reader(sys.stdin)

# Ignorer la première ligne (en-tête)
next(csv_reader, None)

# Parcourez les lignes du CSV
for row in csv_reader:
    # Extraire les champs du CSV
    codcli, cpcli, villecli, datcde, Nbcolis, qte, points = (
        row[0],
        row[4],
        row[5],
        row[7],
        row[10],
        row[15],
        row[20],
    )

    # Remplacez les champs vides par 0 ou ""
    codcli = codcli if codcli and (codcli != "NULL") else ""
    cpcli = cpcli if cpcli and (cpcli != "NULL") else ""
    villecli = villecli if villecli and (villecli != "NULL") else ""
    datcde = datcde if datcde and (datcde != "NULL") else ""
    Nbcolis = Nbcolis if Nbcolis and (Nbcolis != "NULL") else "0"
    qte = qte if qte and (qte != "NULL") else "0"
    points = points if points and (points != "NULL") else "0"

    annee = datcde[:4]
    try:
        annee = int(annee)
    except ValueError:
        continue

    # Imprimez les données récupérées pour les données après 2008
    if annee >= 2008:
        print(
            "%s;%s;%s;%s;%s;%s;%s"
            % (codcli, cpcli, villecli, datcde, Nbcolis, qte, points)
        )
