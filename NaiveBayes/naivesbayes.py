import json
import re
import pandas as pd
from sklearn.model_selection import train_test_split
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
    df = load_data_dict('data70_etiq.txt')

    # Convertir set en liste pour TfidfVectorizer
    combined_stopwords = list(stop_words_fr.union(stop_words_en))

    df['label'] = df['label'].str.lower()

    X_train, X_test, y_train, y_test = train_test_split(
        df['tweet'], df['label'], test_size=0.2, random_state=42, shuffle=True
    )

    pipeline = Pipeline([
        ('cleaner', TextCleaner()),
        ('tfidf', TfidfVectorizer(stop_words=combined_stopwords, max_features=5000)),
        ('clf', MultinomialNB())
    ])

    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    def predict_sentiment(text):
        return pipeline.predict([text])[0]

    exemples = [
        "I love this product!",
        "Je déteste ce service.",
        "C'est un bon jour.",
        "This is terrible."
    ]

    for ex in exemples:
        print(f"Texte: {ex}\nSentiment prédit: {predict_sentiment(ex)}\n")
