import json
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.base import TransformerMixin

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
    df = load_data_dict('data70_etiq.txt')

    # Utiliser l'intégralité des données pour l'apprentissage
    X_train = df['tweet']
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

    # Entraînement avec l'intégralité des données de data70_etiq
    pipeline.fit(X_train, y_train)

    # Pour le test, charger data20_etiq manuellement
    # Exemple de code pour charger et tester sur data20_etiq (manuellement après)
    # df_test = load_data_dict('data20_etiq.txt')
    # y_pred = pipeline.predict(df_test['tweet'])
    # print("Accuracy:", accuracy_score(df_test['label'], y_pred))
    # print(classification_report(df_test['label'], y_pred))

    def predict_sentiment(text):
        return pipeline.predict([text])[0]





# Fonction de test avec le modèle pipeline sur data20_etiq
def test(fichier):
    # Charger le fichier de test
    df_test = load_data_dict(fichier)
    
    # Séparer les tweets et les labels
    X_test = df_test['tweet']
    y_test = df_test['label']

    # Prédiction avec le modèle pipeline
    y_pred = pipeline.predict(X_test)

    # Calcul de l'accuracy et du classification report
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

# Appel de la fonction de test
test("data20_etiq.txt")