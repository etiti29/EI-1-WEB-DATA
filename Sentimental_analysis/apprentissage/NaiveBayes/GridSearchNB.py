"""
Script de classification de texte par Naive Bayes avec GridSearch pour l'optimisation des hyperparamètres.

Fonctionnement :
- Charge les données à partir d'un fichier JSON (`data_90.txt`) contenant les tweets et leurs labels.
- Nettoie les tweets en supprimant les URLs, mentions, hashtags, ponctuation et chiffres.
- Utilise TF-IDF pour transformer les tweets en représentations numériques.
- Recherche des meilleurs hyperparamètres pour la vectorisation TF-IDF et le classificateur MultinomialNB avec GridSearchCV.
- Entraîne le modèle avec les meilleures configurations d'hyperparamètres et évalue les performances sur les données d'entraînement.
- Sauvegarde le meilleur modèle sous forme de fichier `.joblib` pour une réutilisation future.

À utiliser avec : `python classification_nb.py`

Bibliothèques nécessaires : pip install pandas scikit-learn joblib stop-words
"""


# Imports des bibliothèques nécessaires
import json
import re
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.base import TransformerMixin

import joblib  # Pour sauvegarder le modèle
import os  # Pour créer un dossier si besoin

# Import des stopwords personnalisés
from stop_words import stop_words_fr, stop_words_en


# Classe pour nettoyer le texte, utilisée dans le pipeline
class TextCleaner(TransformerMixin):
    def transform(self, X, **transform_params):
        return [self.clean_text(text) for text in X]
    
    def fit(self, X, y=None, **fit_params):
        return self
    
    # Méthode de nettoyage : minuscule, suppression d’éléments inutiles
    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r"http\S+", "", text)      # Supprime les URLs
        text = re.sub(r"@\w+", "", text)         # Supprime les mentions
        text = re.sub(r"#\w+", "", text)         # Supprime les hashtags
        text = re.sub(r"[^\w\s]", "", text)      # Supprime la ponctuation
        text = re.sub(r"\d+", "", text)          # Supprime les chiffres
        return text.strip()


# Fonction pour charger les données depuis un fichier JSON au format dict
def load_data_dict(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data_dict = json.load(f)
    return pd.DataFrame(list(data_dict.values()))


# Bloc principal
if __name__ == "__main__":
    # Chargement des données
    df = load_data_dict("Sentimental_analysis/apprentissage/NaiveBayes/data_90.txt")

    # Texte et étiquettes (à adapter selon la structure du fichier)
    X_train = df['tweet']  # Pour les avis iPhone : remplacer par df['text_avis']
    y_train = df['label'].str.lower()  # Mise en minuscule des labels pour homogénéité

    # Fusion des stopwords français et anglais
    combined_stopwords = list(stop_words_fr.union(stop_words_en))

    # Définition du pipeline : nettoyage → TF-IDF → classifieur Naive Bayes
    pipeline = Pipeline([
        ('cleaner', TextCleaner()),
        ('tfidf', TfidfVectorizer(stop_words=combined_stopwords, max_features=5000)),
        ('clf', MultinomialNB())
    ])

    # Grille de recherche pour ajuster les hyperparamètres
    param_grid = {
        'tfidf__max_features': [1000, 3000, 5000],
        'tfidf__ngram_range': [(1, 1), (1, 2), (1, 3)],
        'tfidf__min_df': [1, 2],
        'clf__alpha': [0.01, 0.1, 1.0, 10.0]
    }

    # Recherche des meilleurs paramètres avec validation croisée
    grid_search = GridSearchCV(pipeline, param_grid, cv=3, scoring='accuracy', n_jobs=-1, verbose=2)
    print("Début du GridSearch...")
    grid_search.fit(X_train, y_train)

    # Résultats de la recherche
    results_df = pd.DataFrame(grid_search.cv_results_)
    results_df['accuracy'] = results_df['mean_test_score']

    # Matrice des résultats par alpha et max_features
    scores_matrix = results_df.pivot_table(values='accuracy',
                                           index='param_clf__alpha',
                                           columns='param_tfidf__max_features')

    print("\nMatrice des résultats (accuracy) :")
    print(scores_matrix)

    # Meilleure configuration trouvée
    print("\nMeilleurs paramètres :", grid_search.best_params_)

    # Prédictions sur les données d'entraînement (à remplacer par un set de test pour une vraie évaluation)
    y_pred = grid_search.predict(X_train)
    print("Accuracy sur jeu complet :", accuracy_score(y_train, y_pred))
    print("Rapport de classification :\n", classification_report(y_train, y_pred))

    # Création du dossier de sortie si besoin
    output_dir = 'MultinomialNB'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Sauvegarde du meilleur modèle entraîné
    joblib.dump(grid_search.best_estimator_, os.path.join(output_dir, 'grid_search_nb_best.joblib'))
    print(f"Modèle sauvegardé dans {os.path.join(output_dir, 'grid_search_nb_best.joblib')}")
