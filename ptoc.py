import csv
from cassandra.cluster import Cluster

# Établir une connexion avec le cluster Cassandra
cluster = Cluster(["localhost"])
session = cluster.connect("fromagerie")

# Créez un lecteur CSV pour gérer les données
with open("dataw_fro03.csv", "r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)

    # Ignorer la première ligne (en-tête)
    next(csv_reader, None)

    # Parcourez les lignes du CSV
    for row in csv_reader:
        # Extract values from the CSV row
        (
            codcli,
            genrecli,
            nomcli,
            prenomcli,
            cpcli,
            villecli,
            codcde,
            datcde,
            timbrecli,
            timbrecde,
            Nbcolis,
            cheqcli,
            barchive,
            bstock,
            codobj,
            qte,
            Colis,
            libobj,
            Tailleobj,
            Poidsobj,
            points,
            indispobj,
            libcondit,
            prixcond,
            puobj,
        ) = row

        # Remplacez les champs vides ou null par 0 ou ""
        codcli = codcli if codcli and (codcli != "NULL") else ""
        nomcli = nomcli if nomcli and (nomcli != "NULL") else ""
        prenomcli = prenomcli if prenomcli and (prenomcli != "NULL") else ""
        cpcli = cpcli if cpcli and (cpcli != "NULL") else ""
        villecli = villecli if villecli and (villecli != "NULL") else ""
        codcde = codcde if codcde and (codcde != "NULL") else ""
        # recupere uniquement la date dans un format plus court
        datcde = datcde[:10] if datcde and (datcde != "NULL") else ""
        timbrecli = timbrecli if timbrecli and (timbrecli != "NULL") else "0.0"
        timbrecde = timbrecde if timbrecde and (timbrecde != "NULL") else "0.0"
        Nbcolis = Nbcolis if Nbcolis and (Nbcolis != "NULL") else "0"
        codobj = codobj if codobj and (codobj != "NULL") else ""
        qte = qte if qte and (qte != "NULL") else "0"
        libobj = libobj if libobj and (libobj != "NULL") else ""
        points = points if points and (points != "NULL") else "0"

        # Assurez-vous d'adapter cette requête à votre schéma de table modifié
        query = """
            INSERT INTO ligne_commande 
            (codcli, nomcli, prenomcli, cpcli, villecli, codcde, datcde, timbrecli, timbrecde, nbcolis, codobj, qte, libobj, points)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        session.execute(
            query,
            (
                codcli,
                nomcli,
                prenomcli,
                cpcli,
                villecli,
                codcde,
                datcde,
                timbrecli,
                timbrecde,
                Nbcolis,
                codobj,
                qte,
                libobj,
                points,
            ),
        )

# Fermer la session et la connexion au cluster
session.shutdown()
cluster.shutdown()
