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
    cpcli, datcde, codobj, qte, libobj = row[4], row[7], row[14], row[15], row[17]

    # Remplacez les champs vides par 0 ou ""
    cpcli = cpcli if cpcli and (cpcli != "NULL") else ""
    datcde = datcde if datcde and (datcde != "NULL") else ""
    codobj = codobj if codobj and (codobj != "NULL") else ""
    qte = qte if qte and (qte != "NULL") else "0"
    libobj = libobj if libobj and (cpcli != "NULL") else ""

    # Extraction de l'année à partir de datcde
    annee = datcde[:4]
    try:
        annee = int(annee)
    except ValueError:
        continue

    # Affichage des données si les conditions sont satisfaites
    if (
        cpcli.startswith("53") or cpcli.startswith("72") or cpcli.startswith("49")
    ) and annee >= 2004:
        print("%i;%s;%s;%s" % (annee, codobj, qte, libobj))
