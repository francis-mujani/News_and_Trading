# Projet News & Trading avec Apache Spark Standalone Cluster on Docker



## Contents


| Application            | URL                                      |    Description                                             |
| ---------------------- | ---------------------------------------- | ---------------------------------------------------------- |
| JupyterLab             | [localhost:8888](http://localhost:8888/) | Mon interface Jupyter notebook                             |
| Apache Spark Master    | [localhost:8080](http://localhost:8080/) | Spark Master node                                          |
| Apache Spark Worker I  | [localhost:8081](http://localhost:8081/) | Spark Worker node with 1 core and 512mo (default)          |
| Apache Spark Worker II | [localhost:8082](http://localhost:8082/) | Spark Worker node with 1 core and 512mo (default)          |
| Flask                  | [localhost:3000](http://localhost:5000/) | Dashboard with flask                                       |


### Build les images Docker

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
