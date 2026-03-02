import pandas as pd
import numpy as np
from sklearn.manifold import trustworthiness
from sklearn.neighbors import NearestNeighbors
import argparse
import sys

def calculer_trustworthiness(df_orig, path_red, n_neighbors=10):
    df_red = pd.read_csv(path_red).select_dtypes(include='number')
    return trustworthiness(df_orig.values, df_red.values, n_neighbors=n_neighbors)

def calculer_continuity(df_orig, path_red, n_neighbors=10):
    X = df_orig.values
    Y = pd.read_csv(path_red).select_dtypes(include='number').values

    nbrs_X = NearestNeighbors(n_neighbors=n_neighbors).fit(X)
    nbrs_Y = NearestNeighbors(n_neighbors=n_neighbors).fit(Y)

    neigh_X = nbrs_X.kneighbors(return_distance=False)
    neigh_Y = nbrs_Y.kneighbors(return_distance=False)

    score = 0
    n = X.shape[0]

    for i in range(n):
        intersection = set(neigh_X[i]).intersection(set(neigh_Y[i]))
        score += len(intersection) / n_neighbors

    return score / n

def main():
    parser = argparse.ArgumentParser(description="Comparateur de méthodes de réduction de dimension")
    parser.add_argument('--models', nargs='+')

    args = parser.parse_args([] if "ipykernel" in sys.modules else None)

    disponibles = {
        'PCA': 'outputs/pca_emb_2d.csv',
        't-SNE': 'outputs/tsne_emb_2d.csv',
        'UMAP': 'outputs/umap_emb_2d.csv'
    }

    if not args.models:
        print("Modèles disponibles :", list(disponibles.keys()))
        choix = input("Entrez les modèles à tester séparés par un espace (ou ENTER pour tous) : ")
        if choix.strip():
            args.models = choix.split()

    a_tester = {k: v for k, v in disponibles.items() if not args.models or k in args.models}

    df_orig = pd.read_csv('data/city_lifestyle_dataset.csv').select_dtypes(include='number')

    resultats = []

    print("\n=== Analyse en cours ===\n")

    for name, path in a_tester.items():
        try:
            trust = calculer_trustworthiness(df_orig, path)
            cont = calculer_continuity(df_orig, path)

            resultats.append({
                "Méthode": name,
                "Trustworthiness": trust,
                "Continuity": cont
            })

        except Exception as e:
            print(f"{name} : Erreur ({e})")

    df_res = pd.DataFrame(resultats)
    df_res = df_res.sort_values(by="Trustworthiness", ascending=False)

    print("\n=== Résultats comparatifs ===\n")
    print(df_res.to_string(index=False))

if __name__ == "__main__":
    main()
