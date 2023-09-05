#!/usr/bin/env python
"""reducer.py"""

import sys

# Créez un dictionnaire pour suivre le nombre de commandes par (année, ville, codobj)
commandes_par_annee_ville_objet = {}

for line in sys.stdin:
    line = line.strip()

    cpcli, villecli, annee, codobj, qte = line.split(",")

    try:
        annee = int(annee)
        qte = int(qte)
    except ValueError:
        continue

    if cpcli.startswith("53") and annee >= 2010 and qte > 5:
        # Créez une clé unique pour chaque (année, ville, codobj)
        cle = (annee, codobj, villecli)

        # Mettez à jour le dictionnaire en incrémentant le compteur pour cette clé
        if cle in commandes_par_annee_ville_objet:
            commandes_par_annee_ville_objet[cle] += 1
        else:
            commandes_par_annee_ville_objet[cle] = 1

# Parcourez le dictionnaire et imprimez le résultat
for cle, nombre_commandes in commandes_par_annee_ville_objet.items():
    annee, villecli, codobj = cle
    print("%s\t%s\t%s\t%i" % (annee, villecli, codobj, nombre_commandes))
