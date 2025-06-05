import json
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.base import TransformerMixin
import joblib  # Ajout de l'import de joblib
import os  # Ajout pour gérer les répertoires

# Importer tes stopwords personnalisés
from stop_words import stop_words_fr, stop_words_en

class TextCleaner(TransformerMixin):
    def transform(self, X, **transform_params):
        return [self.clean_text(text) for text in X]
    
    def fit(self, X, y=None, **fit_params):
        return self
    
    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r"http\S+", "", text)
        text = re.sub(r"@\w+", "", text)
        text = re.sub(r"#\w+", "", text)
        text = re.sub(r"[^\w\s]", "", text)
        text = re.sub(r"\d+", "", text)
        return text.strip()

def load_data_dict(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data_dict = json.load(f)
    data_list = list(data_dict.values())
    return pd.DataFrame(data_list)

if __name__ == "__main__":
    # Charger le jeu de données pour l'apprentissage
    df = load_data_dict("data_90.txt")

    # Utiliser l'intégralité des données pour l'apprentissage
    X_train = df['tweet'] #à changer par text_avis pour avis_iphone
    y_train = df['label']

    # Convertir set en liste pour TfidfVectorizer
    combined_stopwords = list(stop_words_fr.union(stop_words_en))

    df['label'] = df['label'].str.lower()

    # Pipeline de prétraitement et d'entraînement
    pipeline = Pipeline([
        ('cleaner', TextCleaner()),
        ('tfidf', TfidfVectorizer(stop_words=combined_stopwords, max_features=5000)),
        ('clf', MultinomialNB())
    ])

    # Définir la grille de recherche d'hyperparamètres
    param_grid = {
        'tfidf__max_features': [1000, 3000, 5000],
        'tfidf__ngram_range': [(1, 1), (1, 2), (1, 3)],
        'tfidf__min_df': [1, 2],
        'clf__alpha': [0.01, 0.1, 1.0, 10.0]
    }

    # Lancer GridSearchCV
    grid_search = GridSearchCV(pipeline, param_grid, cv=3, scoring='accuracy', n_jobs=-1, verbose=2)
    print("Début du GridSearch...")
    grid_search.fit(X_train, y_train)

    # Récupérer les résultats sous forme de DataFrame
    results_df = pd.DataFrame(grid_search.cv_results_)

    # Ajouter une colonne pour l'accuracy de chaque combinaison de paramètres
    results_df['accuracy'] = results_df['mean_test_score']

    # Afficher la matrice des résultats avec les scores d'accuracy pour chaque combinaison de paramètres
    scores_matrix = results_df.pivot_table(values='accuracy', 
                                           index=['param_clf__alpha'], 
                                           columns='param_tfidf__max_features')

    print("\nMatrice des résultats (accuracy) :")
    print(scores_matrix)

    # Meilleurs paramètres
    print("\nMeilleurs paramètres :", grid_search.best_params_)

    # Évaluation sur le même jeu (tu peux remplacer par un test séparé)
    y_pred = grid_search.predict(X_train)
    print("Accuracy sur jeu complet :", accuracy_score(y_train, y_pred))
    print("Rapport de classification :\n", classification_report(y_train, y_pred))

    # Assurez-vous que le répertoire pour sauvegarder le modèle existe
    output_dir = 'MultinomialNB'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Sauvegarder le meilleur modèle
    joblib.dump(grid_search.best_estimator_, os.path.join(output_dir, 'grid_search_nb_best.joblib'))
    print(f"Modèle sauvegardé dans {os.path.join(output_dir, 'grid_search_nb_best.joblib')}")
