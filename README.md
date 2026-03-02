# Projet Final 2025–2026  
## Utilisation de Github et docker

## Équipe de projet
- **Daniel DA SILVA**
- **Thomas BELAID**
- **Franck XU**

**Institution** : Université Paris Cité  

---

##  Objectifs


- Git et GitHub (branches, commits, Pull Requests)
- Implémentation de méthodes de réduction de dimension
- Intégration collaborative dans la branche main
- Comparaison des méthodes via la métrique trustworthiness
- Conteneurisation complète avec Docker


Une fois les contributions fusionnées, un script Python compare les performances des méthodes implémentées.

---


## Processus de Développement avec Docker (Bonus)

Pour garantir un environnement identique pour tous les membres du groupe (même version de Python et des librairies), nous avons choisi de développer l'intégralité du projet sous **Docker**, avec un **volume monté**.

## Processus de Développement avec Docker

Pour garantir un environnement identique pour tous les membres du groupe (même version de Python et des librairies), nous avons choisi de développer l'intégralité du projet sous **Docker**, avec un **volume monté**.

### Développement en local avec volume monté 

Aucun code n'a été exécuté directement sur nos machines hôtes. Les serveurs **Jupyter** ont été lancés depuis le conteneur Docker en montant la racine du projet ($(pwd)) dans /app :

```bash
docker run --rm -it -p 8888:8888 -v "$(pwd):/app" projet_final jupyter-notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

### Avantages

- Ajustement progressif du `Dockerfile` et du `requirements.txt` (ex. ajout de `umap-learn`).
- Travail sur les notebooks (`.ipynb`) via le navigateur, avec sauvegarde automatique sur la machine locale grâce au volume.

### Mise à jour du code et des données sans rebuild

Le montage de volume permet de tester de nouvelles données ou de modifier `evaluate.py` **sans reconstruire l'image Docker**.  


---
## Méthodes Implémentées

-  PCA   
-  t-SNE 
-  UMAP 

Chaque méthode :

- projette les données en 2 dimensions
- génère une visualisation 2D
- exporte les données réduites
- inclut une courte analyse du graphique

---

## Structure du dépôt

```bash
.
├── data/
│   └── city_lifestyle_dataset.csv
│   └── kaggle_readme.md
├── notebooks/
│   ├── pca.ipynb
│   ├── tsne.ipynb
│   └── umap.ipynb
├── evaluate.py
├── outputs/
│   ├── pca_2d.csv
│   ├── tsne_2d.csv
│   └── umap_2d.csv
├── Dockerfile
├── requirements.txt
└── README.md
```

## Installation (Version Locale)

###  Cloner le dépôt

```bash
git clone https://github.com/ThomaasSB/Projet_PPD.git
cd Projet_PPD
```

###  Créer un environnement virtuel

```bash
python -m venv venv
```

###  Activer l’environnement

Windows :
```bash
venv\Scripts\activate
```

Linux / macOS :
```bash
source venv/bin/activate
```

###  Installer les dépendances

```bash
pip install -r requirements.txt
```

###  Lancer le script de comparaison

```bash
python evaluate.py
```

---

## Dockerisation

Le projet est conteneurisé afin de garantir la reproductibilité.

### Exécution avec Docker

Build de l'image :
   ```bash
   docker build -t projet-final-git .
   ```


Lancer l'évaluation complète :

   ```bash
docker run --rm -it projet-final-git
   ```










