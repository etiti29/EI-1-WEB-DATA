"""
Script d'étiquetage automatique des tweets par analyse lexicale et syntaxique.

Fonctionnement :
- Utilise un pipeline scikit-learn avec un nettoyage de texte personnalisé, une vectorisation TF-IDF, et un classificateur Naive Bayes.
- Le nettoyage inclut la suppression des URLs, mentions, hashtags, ponctuation, et chiffres.
- Le modèle est entraîné sur un jeu de données étiqueté et évalue les tweets en fonction de leur sentiment (positif, neutre, négatif).
- Le modèle utilise une combinaison de stopwords en français et en anglais pour la vectorisation TF-IDF.

À lancer avec : `python etiquetage_sentiment.py`

Bibliothèques nécessaires :
pip install pandas scikit-learn stop-words
"""

# Imports des bibliothèques nécessaires
import json
import re
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.base import TransformerMixin

# Import des stopwords personnalisés (français et anglais)
from stop_words import stop_words_fr, stop_words_en


# Nettoyage de texte compatible avec scikit-learn
class TextCleaner(TransformerMixin):
    def transform(self, X, **transform_params):
        return [self.clean_text(text) for text in X]
    
    def fit(self, X, y=None, **fit_params):
        return self
    
    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r"http\S+", "", text)      # Supprime les URLs
        text = re.sub(r"@\w+", "", text)         # Supprime les mentions
        text = re.sub(r"#\w+", "", text)         # Supprime les hashtags
        text = re.sub(r"[^\w\s]", "", text)      # Supprime la ponctuation
        text = re.sub(r"\d+", "", text)          # Supprime les chiffres
        return text.strip()


# Fonction utilitaire pour charger un fichier JSON contenant des textes étiquetés
def load_data_dict(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data_dict = json.load(f)
    data_list = list(data_dict.values())
    return pd.DataFrame(data_list)


if __name__ == "__main__":
    # Chargement des données d'apprentissage (70 %)
    df = load_data_dict('Sentimental_analysis\Twitter\data\data_traité\data70_etiq.txt') #à changer par avis_train pour Iphone
    X_train = df['tweet']
    y_train = df['label'].str.lower()  # Normalisation des étiquettes

    # Fusion des stopwords pour le nettoyage TF-IDF
    combined_stopwords = list(stop_words_fr.union(stop_words_en))

    # Pipeline complet : nettoyage → vectorisation → classification
    pipeline = Pipeline([
        ('cleaner', TextCleaner()),
        ('tfidf', TfidfVectorizer(stop_words=combined_stopwords, max_features=5000)),
        ('clf', MultinomialNB())
    ])

    # Entraînement du modèle sur l’ensemble des données
    pipeline.fit(X_train, y_train)

    # Fonction pour prédire le sentiment d’un texte individuel
    def predict_sentiment(text):
        return pipeline.predict([text])[0]


# Fonction de test : évalue le modèle sur un fichier de test
def test(fichier):
    df_test = load_data_dict(fichier)
    X_test = df_test['tweet']
    y_test = df_test['label']
    
    y_pred = pipeline.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))


# Évaluation du modèle sur les 30 % restants (fichier de test)
test('Sentimental_analysis\Twitter\data\data_traité\data10_etiq.txt') #à changer par avis_validation pour Iphone
