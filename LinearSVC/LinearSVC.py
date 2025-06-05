import json
import pandas as pd
from sklearn import svm
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib  # Ajout de l'import de joblib
import os  # Pour gérer la création de répertoire


# Charger les données d'entraînement (data70_etiq.txt)
with open('data_traité/data70_etiq.txt', encoding='utf-8') as f:
    data_train = json.load(f)

# Charger les données de test (data10_etiq.txt)
with open('data_traité/data10_etiq.txt', encoding='utf-8') as f:
    data_test = json.load(f)


# Initialiser les listes pour les tweets et labels
x_train = []
y_train = []
x_test = []
y_test = []

# Charger les tweets et labels d'entraînement
for key in data_train:
    tweet_data = data_train[key]
    x_train.append(tweet_data["tweet"])
    y_train.append(tweet_data["label"])

# Charger les tweets et labels de test
for key in data_test:
    tweet_data = data_test[key]
    x_test.append(tweet_data["tweet"])
    y_test.append(tweet_data["label"])


# Vectorisation du texte
vectorizer = TfidfVectorizer()

# Vérifier que x_train contient des données
if len(x_train) > 0:
    X_train_vec = vectorizer.fit_transform(x_train)
else:
    raise ValueError("x_train est vide. Assurez-vous que les données d'entraînement sont correctement chargées.")

# Vérifier que x_test contient des données
if len(x_test) > 0:
    X_test_vec = vectorizer.transform(x_test)
else:
    raise ValueError("x_test est vide. Assurez-vous que les données de test sont correctement chargées.")


# Définir le modèle LinearSVC
clf = svm.LinearSVC(C=1.0, max_iter=1000)  # Choisissez les paramètres ici, par exemple C=1.0 et max_iter=1000


# Entraînement du modèle
clf.fit(X_train_vec, y_train)


# Prédiction sur le jeu de test
y_pred = clf.predict(X_test_vec)


# Calcul de l'accuracy sur le jeu de test
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy sur jeu de test :", accuracy)

# Rapport de classification
print("Rapport de classification :\n", classification_report(y_test, y_pred))

# Matrice de confusion
print("Matrice de confusion :\n", confusion_matrix(y_test, y_pred))

# Sauvegarder le modèle
output_dir = 'LinearSVC_Model'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

joblib.dump(clf, os.path.join(output_dir, 'linear_svc_model.joblib'))
print(f"Modèle sauvegardé dans {os.path.join(output_dir, 'linear_svc_model.joblib')}")
