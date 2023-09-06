CREATE KEYSPACE IF NOT EXISTS fromagerie
WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor': 3 };

Use fromagerie;

CREATE TABLE IF NOT EXISTS ligne_commande (
    codcli TEXT,
    nomcli TEXT,
    prenomcli TEXT,
    cpcli TEXT,
    villecli TEXT,
    codcde TEXT,
    datcde TEXT,
    timbrecli TEXT,
    timbrecde TEXT,
    nbcolis TEXT,
    codobj TEXT,
    qte TEXT,
    libobj TEXT,
    points TEXT,
    PRIMARY KEY (codcli, codcde, codobj)
);


TABLE