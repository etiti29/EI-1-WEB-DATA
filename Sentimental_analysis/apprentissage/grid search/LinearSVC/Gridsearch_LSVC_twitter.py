import json
import pandas as pd
from sklearn import svm
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split  # Importation de la fonction de séparation aléatoire
import joblib  # Ajout de l'import de joblib
import os  # Pour gérer la création de répertoire




# Charger les données
# Charger les données à partir du fichier JSON
with open('data_traité/data20_etiq.txt', encoding='utf-8') as f:
    data = json.load(f)


# Vérifier la taille du dataset
print(f"Nombre total de tweets dans le dataset : {len(data)}")


# Initialiser les listes
x = []
y = []


# Charger les tweets et les labels
for key in data:
    tweet_data = data[key]
    x.append(tweet_data["tweet"])
    y.append(tweet_data["label"])


# Séparation des données en train et test (80% pour l'entraînement, 20% pour le test)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


# Vérification de la taille des ensembles
print(f"Nombre d'exemples dans l'ensemble d'entraînement (x_train) : {len(x_train)}")
print(f"Nombre d'exemples dans l'ensemble de test (x_test) : {len(x_test)}")


# Vectorisation du texte
vectorizer = TfidfVectorizer()


# Vérifier que x_train contient des données
if len(x_train) > 0:
    X_vec = vectorizer.fit_transform(x_train)
else:
    raise ValueError("x_train est vide. Assurez-vous que les données d'entraînement sont correctement chargées.")


# Vérifier que x_test contient des données
if len(x_test) > 0:
    X_test_vec = vectorizer.transform(x_test)
else:
    raise ValueError("x_test est vide. Assurez-vous que les données de test sont correctement chargées.")


# Définir le modèle SVC
clf = svm.SVC()


# Définir la grille de recherche des hyperparamètres pour le SVC
param_grid = {
    'C': [0.1, 1.0, 10.0],  # Paramètre de régularisation
    'kernel': ['linear', 'rbf'],  # Choix du noyau
    'gamma': ['scale', 'auto'],  # Paramètre de noyau RBF
}


# Initialisation du GridSearchCV
grid_search = GridSearchCV(clf, param_grid, cv=3, scoring='accuracy', n_jobs=-1, verbose=2)


# Lancer le GridSearchCV
print("Début du GridSearch...")
grid_search.fit(X_vec, y_train)


# Récupérer les résultats sous forme de DataFrame
results_df = pd.DataFrame(grid_search.cv_results_)


# Ajouter une colonne pour l'accuracy de chaque combinaison de paramètres
results_df['accuracy'] = results_df['mean_test_score']


# Afficher la matrice des résultats avec les scores d'accuracy pour chaque combinaison de paramètres
scores_matrix = results_df.pivot_table(values='accuracy',
                                       index=['param_C', 'param_kernel'],
                                       columns='param_gamma')


print("\nMatrice des résultats (accuracy) :")
print(scores_matrix)


# Meilleurs paramètres
print("\nMeilleurs paramètres :", grid_search.best_params_)


# Évaluation sur le jeu de test
y_pred = grid_search.predict(X_test_vec)
print("Accuracy sur jeu de test :", accuracy_score(y_test, y_pred))
print("Rapport de classification :\n", classification_report(y_test, y_pred))
print("Matrice de confusion :\n", confusion_matrix(y_test, y_pred))


# Assurez-vous que le répertoire pour sauvegarder le modèle existe
output_dir = 'SVM_Model'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


# Sauvegarder le meilleur modèle
joblib.dump(grid_search.best_estimator_, os.path.join(output_dir, 'grid_search_svc_best.joblib'))
print(f"Modèle sauvegardé dans {os.path.join(output_dir, 'grid_search_svc_best.joblib')}")



