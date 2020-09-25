# Projet News & Trading avec Apache Spark Standalone Cluster on Docker



## Contents


| Application            | URL                                      |    Description                                             |
| ---------------------- | ---------------------------------------- | ---------------------------------------------------------- |
| JupyterLab             | [localhost:8888](http://localhost:8888/) | Mon interface Jupyter notebook                             |
| Apache Spark Master    | [localhost:8080](http://localhost:8080/) | Spark Master node                                          |
| Apache Spark Worker I  | [localhost:8081](http://localhost:8081/) | Spark Worker node with 1 core and 512mo (default)          |
| Apache Spark Worker II | [localhost:8082](http://localhost:8082/) | Spark Worker node with 1 core and 512mo (default)          |
| Flask                  | [localhost:3000](http://localhost:5000/) | Dashboard with flask                                       |


### Pour lancer le projet il suffit d'ouvrir le terminal et de lancer ces commandes :
##### D'abord cloné le projet en local
### 1. 
```bash
## 1. cloné le projet  
git clone + 'url'
```
### 2.
2.1. récuperer l'api_key sur l'adresse suivante: https://www.alphavantage.co/
2.2. Ouvrez le terminal

```bash
## Aller dans flask puis dans api
cd flask
cd 
```

## 1. créer un fichier dans le dossier api

```bash
touch api_key.py
```
2.3 Coller le code ci-dessous en remplaçant les X par votre api_key que vous avez recuperez chez alphavantage
```bash
API_KEY = "XXXXXXXXX"
```
### 3.
```bash
# Remettez vous dans la racine du projet
cd ..
# puis lancer docker-compose pour builder les images et lancer le projet en meme temps
doker-compose up
```

## Lancer le projet partie 2
### Build d'abord les images et lancer le projet par la suite
```bash
cd build
```

1. Editer le fichier [build.yml] pour choisir vos propre versions

2. Build the images;

# Donner la permission au fichier build.sh
```bash
chmod +x build.sh ; ./build.sh
```

3. Build le cluster (lancer le projet);

```bash
docker-compose up
```

4. Le projet est lancé et pour Stoper les clusters, taper  `ctrl+c`.

- Infrastructure

| Component      | Version |
| -------------- | ------- |
| Docker Engine  | 1.13.0+ |
| Docker Compose | 1.10.0+ |
| Python         | 3.7.3   |
| Scala          | 2.12.11 |
| R              | 3.5.2   |
| Flask          | .....   |



- Jupyter Kernels

| Component      | Version | Provider                                |
| -------------- | ------- | --------------------------------------- |
| Python         | 2.1.4   | [Jupyter](https://jupyter.org/)         |
| Scala          | 0.10.0  | [Almond](https://almond.sh/)            |
| R              | 1.1.1   | [IRkernel](https://irkernel.github.io/) |

- Applications

| Component      | Version                 | Docker Tag                                           |
| -------------- | ----------------------  | ---------------------------------------------------- |
| Apache Spark   | 2.4.0 \| 2.4.4 \| 3.0.0 | -hadoop-2.7                      |
| JupyterLab     | 2.1.4                   | -spark- |
| Flask          |                         |         |



 - **Francis mujani** - fmujani08@gmail.com
