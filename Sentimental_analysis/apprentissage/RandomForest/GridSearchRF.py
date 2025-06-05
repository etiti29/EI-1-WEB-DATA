"""
Script de classification de texte par **Random Forest** avec **GridSearch** pour l'optimisation des hyperparamètres.

Fonctionnement :
- Charge les données à partir d'un fichier JSON (`data20_etiq.txt`) contenant les tweets et leurs labels.
- Crée un vocabulaire à partir des mots présents dans les tweets.
- Utilise un RandomForestClassifier pour classifier les tweets en fonction de leur sentiment.
- Effectue une recherche des meilleurs hyperparamètres avec GridSearchCV (n_estimators, max_depth, min_samples_split, etc.).
- Entraîne le modèle avec les meilleures configurations d'hyperparamètres et évalue les performances sur les données d'entraînement.
- Sauvegarde le meilleur modèle sous forme de fichier `.joblib` pour une réutilisation future.

À utiliser avec : `python classification_rf.py`

Bibliothèques nécessaires : pip install pandas scikit-learn joblib numpy
"""



import numpy as np
import json
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.metrics import classification_report, accuracy_score
import joblib
import pandas as pd

# --- Fonctions vocabulaire et TF-IDF ---

def vocabulaire(data):   
    voc = {}                  
    i = 0
    for content in data.values():
        mots = content['tweet'].split()
        for k in range(len(mots)):
            if mots[k] in voc.keys():
                if mots[k] not in mots[:k]:
                    voc[mots[k]][1] += 1
            else:
                voc[mots[k]] = [i, 1]
                i += 1
    return voc

def TF_IDF(mot, tweet, vocabulaire, data):
    tf = 0
    tweet_split = tweet.split()
    for x in tweet_split:
        if x == mot:
            tf += 1
    if tf == 0:
        return 0
    idf = np.log(len(data.keys()) / vocabulaire[mot][1])
    return (1 + np.log(tf)) * idf

def vectorisation(tweet, vocabulaire, data):
    vecteur = [0 for _ in range(len(vocabulaire.keys()))]
    tweet_split = tweet.split()
    for x in tweet_split:
        if x in vocabulaire.keys():
            vecteur[vocabulaire[x][0]] = TF_IDF(x, tweet, vocabulaire, data)
    return vecteur

# --- Transformer sklearn pour ta vectorisation ---

class CustomVectorizer(BaseEstimator, TransformerMixin):
    def __init__(self, vocab=None, data=None):
        self.vocab = vocab
        self.data = data
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return [vectorisation(tweet, self.vocab, self.data) for tweet in X]

# --- Chargement des données ---

def load_data(filepath):
    with open(filepath, mode='r', encoding='utf-8') as file:
        data = json.load(file)
    data = {int(key): value for key, value in data.items()}
    X = [v['tweet'] for v in data.values()]
    y = [v['label'] for v in data.values()]
    return X, y, data

if __name__ == "__main__":
    # Charger données
    fichier = "Sentimental_analysis\Twitter\data\data_traité\data20_etiq.txt"  # modifie le chemin si besoin
    X, y, data_dict = load_data(fichier)

    # Construire vocabulaire
    voc = vocabulaire(data_dict)

    # Construire pipeline
    pipeline = Pipeline([
        ('vect', CustomVectorizer(vocab=voc, data=data_dict)),
        ('clf', RandomForestClassifier(random_state=42))
    ])

    # Définir la grille de recherche d'hyperparamètres
    param_grid = {
        'clf__n_estimators': [50, 100, 200],
        'clf__max_depth': [None, 10, 20],
        'clf__min_samples_split': [2, 5],
        'clf__min_samples_leaf': [1, 2],
        'clf__max_features': ['sqrt']  # 'auto' peut générer un warning
    }

    # Lancer GridSearchCV
    grid_search = GridSearchCV(pipeline, param_grid, cv=3, scoring='accuracy', n_jobs=-1, verbose=2)
    print("Début du GridSearch...")
    grid_search.fit(X, y)

    # Récupérer les résultats sous forme de DataFrame
    results_df = pd.DataFrame(grid_search.cv_results_)

    # Afficher la matrice des résultats avec les scores d'accuracy
    scores_matrix = results_df.pivot_table(values='mean_test_score', 
                                           index=['param_clf__n_estimators', 'param_clf__max_depth', 'param_clf__min_samples_split', 'param_clf__min_samples_leaf'], 
                                           columns='param_clf__max_features')

    print("\nMatrice des résultats (accuracy) :")
    print(scores_matrix)

    # Meilleurs paramètres
    print("\nMeilleurs paramètres :", grid_search.best_params_)

    # Évaluation sur le même jeu (tu peux remplacer par un test séparé)
    y_pred = grid_search.predict(X)
    print("Accuracy sur jeu complet :", accuracy_score(y, y_pred))
    print("Rapport de classification :\n", classification_report(y, y_pred))

    # Sauvegarder le meilleur modèle
    joblib.dump(grid_search.best_estimator_, 'RandomForest/grid_search_rf_best.joblib')
    print("Modèle sauvegardé dans RandomForest/grid_search_rf_best.joblib")
