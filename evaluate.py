import pandas as pd
from sklearn.manifold import trustworthiness
import argparse

def calculer_trustworthiness(df_orig, path_red):
    df_red = pd.read_csv(path_red).select_dtypes(include='number')
    return trustworthiness(df_orig.values, df_red.values, n_neighbors=10)

def main():
    parser = argparse.ArgumentParser(description="Calculateur de Trustworthiness")
    parser.add_argument('--models', nargs='+', help="Liste des modèles à tester (ex: PCA t-SNE)")
    args = parser.parse_args()

    # Configuration des chemins
    disponibles = {'PCA': 'outputs/pca_emb_2d.csv', 't-SNE': 'outputs/tsne_emb_2d.csv', 'UMAP': 'outputs/umap_emb_2d.csv'}
    
    # Choix de l'utilisateur ou par défaut
    a_tester = {k: v for k, v in disponibles.items() if k in args.models} if args.models else disponibles

    df_orig = pd.read_csv('data/city_lifestyle_dataset.csv').select_dtypes(include='number')

    print(f"=== Analyse pour : {list(a_tester.keys())} ===")
    for name, path in a_tester.items():
        try:
            score = calculer_trustworthiness(df_orig, path)
            print(f"{name} : {score:.4f}")
        except Exception as e:
            print(f"{name} : Erreur ({e})")

if __name__ == "__main__":
    main()