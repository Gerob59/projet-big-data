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
    cpcli, codcde, datcde, timbrecde, Nbcolis, qte, points = (
        row[4],
        row[6],
        row[7],
        row[9],
        row[10],
        row[15],
        row[20],
    )

    # Remplacez les champs vides par 0 ou ""
    cpcli = cpcli if cpcli and (cpcli != "NULL") else ""
    codcde = codcde if codcde and (codcde != "NULL") else ""
    datcde = datcde if datcde and (datcde != "NULL") else ""
    timbrecde = timbrecde if timbrecde and (timbrecde != "NULL") else "0.0"
    Nbcolis = Nbcolis if Nbcolis and (Nbcolis != "NULL") else "0"
    qte = qte if qte and (qte != "NULL") else "0"
    points = points if points and (points != "NULL") else "0"

    annee = datcde[:4]  # Extraction de l'année à partir de datcde
    try:
        annee = int(annee)
    except ValueError:
        continue

    if annee >= 2006 and annee <= 2016:
        print("%s;%s;%s;%s;%s;%s" % (cpcli, codcde, timbrecde, Nbcolis, qte, points))
