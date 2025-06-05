"""
Script d’étiquetage automatique des avis iPhone en français par analyse lexicale et syntaxique.

Fonctionnement :
- Utilise le modèle spaCy `fr_core_news_sm` pour analyser la structure des phrases.
- Associe un score à chaque mot selon un lexique prédéfini pondéré.
- Calcule un score global pour prédire un label de sentiment (positif, neutre, négatif).

À lancer avec : `python etiquetage_iphone.py`

Bibliothèques nécessaires :
pip install spacy scikit-learn
python -m spacy download fr_core_news_sm
"""

import spacy
from sklearn.metrics import classification_report, accuracy_score
import json

# Lexique partiel des mots avec leur score de polarité (positif, négatif, neutre)
# (ce lexique est à compléter ou charger depuis un fichier selon le projet)
produit_lexique = {
    "super": "2", "déçu": "-1", "parfaitement": "2", "problème": "-1",
    "fonctionne": "1", "batterie": "1", "écran": "1", "rapide": "1",
    "satisfait": "1", "qualité": "1", "livraison": "0.8"
}

def analyse(phrase):
    """
    Analyse syntaxique et sémantique d’une phrase pour calculer un score de sentiment.
    Retourne : 'positif', 'neutre' ou 'négatif'.
    """
    nlp = spacy.load("fr_core_news_sm")
    doc = nlp(phrase)
    score = 0
    i = 0

    for token in doc:
        if token.dep_ not in ["det"]:  # Ignore les déterminants
            lemma = token.lemma_
            if lemma in produit_lexique and float(produit_lexique[lemma]) != 0:
                score += float(produit_lexique[lemma])
                i += 1

                head_lemma = token.head.lemma_
                if head_lemma in produit_lexique and head_lemma != lemma and float(produit_lexique[head_lemma]) != 0:
                    i += 1
                    score += float(produit_lexique[lemma]) * float(produit_lexique[head_lemma])

    score = score / (i + 1)

    if score > 0.3:
        return "positif"
    elif score < 0.1:
        return "négatif"
    else:
        return "neutre"

def etiquette(avis_list):
    """
    Étiquette une liste de textes d’avis avec l’analyse de sentiment.
    """
    return [analyse(texte) for texte in avis_list]

def test(fichier):
    """
    Teste l’étiquetage automatique sur un fichier JSON d’avis
    et affiche la précision et le rapport de classification.
    """
    with open(fichier, mode='r', encoding='utf-8') as file:
        data_test = json.load(file)

    # Conversion des clés en entiers si nécessaire
    data_test = {int(key): value for key, value in data_test.items()}

    # Sélection de sous-ensembles d’avis pour tester (à adapter)
    x_test = [content["text_avis"] for content in list(data_test.values())[:40]]
    y_test = [content["label"] for content in list(data_test.values())[60:100]]

    # Prédiction
    y_pred = etiquette(x_test)

    # Résultats
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

    erreurs = sum(1 for i in range(len(y_pred)) if y_pred[i] != y_test[i])
    print(f"{erreurs} erreurs sur {len(y_pred)} avis")

# Lancer un test sur fichier JSON quelconque.
test(r"C:\Users\sarae\Desktop\Clean ST4\EI_1_WEB_DATA\Sentimental_analysis\Iphone\scrapping_iphone\avis_validation.txt")

