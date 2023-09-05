@REM copie de la data
docker cp dataw_fro03.csv hadoop-master:/root/

@REM copie des mappers-reducers
docker cp mapper_lot1_exo1.py hadoop-master:/root/
docker cp mapper_lot1_exo2.py hadoop-master:/root/
docker cp mapper_lot1_exo3.py hadoop-master:/root/
docker cp mapper_lot2_exo1.py hadoop-master:/root/
docker cp mapper_lot2_exo2.py hadoop-master:/root/
docker cp reducer_lot1_exo1.py hadoop-master:/root/
docker cp reducer_lot1_exo2.py hadoop-master:/root/
docker cp reducer_lot1_exo3.py hadoop-master:/root/
docker cp reducer_lot2_exo1.py hadoop-master:/root/
docker cp reducer_lot2_exo2.py hadoop-master:/root/

@REM copie des executables .sh
docker cp lot1_exo1.sh hadoop-master:/root/
docker cp lot1_exo2.sh hadoop-master:/root/
docker cp lot1_exo3.sh hadoop-master:/root/
docker cp lot2_exo1.sh hadoop-master:/root/
docker cp lot2_exo2.sh hadoop-master:/root/

@REM lancement des services hadoop
docker exec hadoop-slave1 /bin/bash -c './service_slv.sh'
docker exec hadoop-slave2 /bin/bash -c './service_slv.sh'