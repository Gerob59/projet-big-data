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
    cpcli = row[4]
    villecli = row[5]
    datcde = row[7]
    codobj = row[14]
    qte = row[15]

    # Remplacez les champs vides par 0 ou ""
    cpcli = cpcli if cpcli and (cpcli != "NULL") else ""
    villecli = villecli if villecli and (villecli != "NULL") else ""
    annee = datcde[:4] if datcde and (datcde != "NULL") else ""
    codobj = codobj if codobj and (codobj != "NULL") else "0"
    qte = qte if qte and (qte != "NULL") else "0"

    # print les data récupérés pour le donnée en lecture stdin au reducer
    print("%s,%s,%s,%s,%s" % (cpcli, villecli, annee, codobj, qte))
