import sys
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import pandas as pd

# Créez un dictionnaire pour suivre le nombre de points par clients
points_par_clients = {}
# Créez un dictionnaire vide pour suivre les données des villes et de leurs clients
villes = {}

for line in sys.stdin:
    line = line.strip()

    codcli, cpcli, villecli, datcde, Nbcolis, qte, points = line.split(";")

    # typage des variables
    try:
        Nbcolis = int(Nbcolis)
        qte = int(qte)
        points = int(points)
    except ValueError:
        continue

    # calcul des points de commandes
    points_commande = (points if points > 0 else 0) * qte

    # Mettre à jour le dictionnaire points_par_clients
    if codcli in points_par_clients:
        points_par_clients[codcli] += points_commande
    else:
        points_par_clients[codcli] = points_commande

    # Mettre à jour le dictionnaire villes
    if villecli not in villes:
        villes[villecli] = {"cpcli": cpcli, "clients": {}}

    # Mettre à jour le dictionnaire villes
    if codcli not in villes[villecli]["clients"]:
        villes[villecli]["clients"][codcli] = {
            "nb_point": points_commande,
            "nb_colis": Nbcolis,
            "min_colis": Nbcolis,
            "max_colis": Nbcolis,
            "nb_cmd": 1,
        }
    else:
        client = villes[villecli]["clients"][codcli]
        client["nb_point"] += points_commande
        client["nb_colis"] += Nbcolis
        client["min_colis"] = min(client["min_colis"], Nbcolis)
        client["max_colis"] = max(client["max_colis"], Nbcolis)
        client["nb_cmd"] += 1
        villes[villecli]["clients"][codcli] = client

# Triez les clients par nombre de points décroissant
clients_tries = sorted(points_par_clients.items(), key=lambda x: x[1], reverse=True)
top_10_clients = [client[0] for client in clients_tries[:10]]

# variable pour stocker les data des top_10_clients
mydata = []

# Affichez les 10 meilleurs clients
for ville, data in villes.items():
    for codcli, client_info in data["clients"].items():
        if codcli in top_10_clients:
            mydata.append(
                (
                    data["cpcli"],
                    codcli,
                    client_info["nb_colis"] / client_info["nb_cmd"],  # moyenne
                    client_info["max_colis"] - client_info["min_colis"],  # ecart type
                )
            )

# Créez un DataFrame Pandas
df = pd.DataFrame(mydata)

# Créez un graphique en secteurs pour la moyenne par ville
output_pdf_file = "/datavolume1/lot1_exo2.pdf"
with PdfPages(output_pdf_file) as pdf:
    plot1 = plt.figure()
    plt.title("Moyenne de colis par commande par Ville")
    for value in mydata:
        plt.bar(value[0], value[2])  # ville, moyenne
    pdf.savefig(plot1)
    plt.close()  # Fermez le graphique (libère la mémoire)

    plot2 = plt.figure()
    plt.title("ecart-type des colis par commande par Ville")
    for value in mydata:
        plt.bar(value[0], value[3])  # ville, ecart type
    pdf.savefig(plot2)
    plt.close()  # Fermez le graphique (libère la mémoire)
