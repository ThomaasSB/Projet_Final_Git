import pandas as pd
from sklearn.manifold import trustworthiness # [cite: 48]

def main():
    # 1. Charger l'original (numérique uniquement)
    df_orig = pd.read_csv('data/city_lifestyle_dataset.csv').select_dtypes(include='number')

    # 2. Fichiers à tester
    methods = {
        'PCA': 'outputs/pca_emb_2d.csv',
        't-SNE': 'outputs/tsne_emb_2d.csv',
        'UMAP': 'outputs/umap_emb_2d.csv'
    }

    print("=== Résultats Trustworthiness ===")
    
    # 3. Calcul et affichage 
    for name, path in methods.items():
        try:
            # Charger les données 2D
            df_red = pd.read_csv(path).select_dtypes(include='number')
            
            # Calcul du score avec n_neighbors=10 [cite: 49]
            score = trustworthiness(df_orig.values, df_red.values, n_neighbors=10) # [cite: 49]
            print(f"{name} : {score:.4f}")
            
        except Exception as e:
            # Gère les fichiers introuvables ou les erreurs de dimensions
            print(f"{name} : Erreur ({type(e).__name__})")

if __name__ == "__main__":
    main()