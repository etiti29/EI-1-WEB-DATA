"""
Script d’étiquetage de phrases en français à l’aide d’un lexique de polarité
et d’une analyse grammaticale avec spaCy.

- Charge un lexique CSV de mots français avec un score de polarité.
- Analyse chaque phrase avec spaCy pour détecter la fonction grammaticale des mots.
- Calcule un score de sentiment pondéré.
- Prend en compte la négation contextuelle pour inverser le sens d’un mot.

Commandes :
- Lancer avec : `python etiquetage_lexique_spacy.py`
- Installer les dépendances :
    pip install spacy
    python -m spacy download fr_core_news_sm
"""

import json
import csv
import spacy

# Charger le modèle de langue française
nlp = spacy.load("fr_core_news_sm")

# Charger les données à étiqueter depuis un fichier JSON
with open("Sentimental_analysis/Twitter/data/brut_data.txt", mode='r', encoding='utf-8') as file:
    data = json.load(file)
dico = {int(key): value for key, value in data.items()}


# Initialisation des structures
positivité = {}
mots_forts_négatifs = set()
verbes_positifs = set()
verbes_neutres = set()

# Charger un lexique CSV avec des scores de polarité
with open('Sentimental_analysis/Twitter/etiquetage/lexique_pos_fr.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=',', quotechar='"')
    for row in reader:
        mot = row[0].lower()
        try:
            score = float(row[1])
            positivité[mot] = score

            if score <= -0.7:
                mots_forts_négatifs.add(mot)
            elif score >= 0.7:
                verbes_positifs.add(mot)
            if abs(score) < 0.05:
                verbes_neutres.add(mot)
        except ValueError:
            continue

# Pondération des mots selon leur rôle grammatical
poids_pos = {
    "ADJ": 1.0,
    "ADV": 0.8,
    "VERB": 0.7,
    "NOUN": 0.4
}

# Fonction principale d’étiquetage
def etiquette(tweet):
    doc = nlp(tweet)
    tokens_lower = [token.text.lower() for token in doc]

    contient_mot_très_négatif = any(mot in mots_forts_négatifs for mot in tokens_lower)
    contient_verbe_positif = any(token.text.lower() in verbes_positifs and token.pos_ == "VERB" for token in doc)
    tous_verbes_sont_neutres = all(token.text.lower() in verbes_neutres for token in doc if token.pos_ == "VERB")

    score_total = 0
    poids_total = 0
    negation_active = False

    for token in doc:
        mot = token.text.lower()
        pos = token.pos_
        poids = poids_pos.get(pos, 0)

        if mot in {"ne", "pas", "plus", "jamais", "aucun", "point", "n’", "n'"}:
            negation_active = True
            continue

        if mot in positivité and poids > 0:
            score = positivité[mot]
            if negation_active:
                score *= -1
                negation_active = False
            score_total += score * poids
            poids_total += poids

    score_pondéré = score_total / poids_total if poids_total > 0 else 0

    # Ajustements contextuels
    if contient_mot_très_négatif and contient_verbe_positif:
        score_pondéré += 0.3

    if contient_mot_très_négatif and tous_verbes_sont_neutres and not contient_verbe_positif:
        print("→ Neutralité factuelle détectée")
        score_pondéré = 0.5

    score_pondéré = min(max(score_pondéré, 0), 1)
    return score_pondéré

# Étiquetage complet d’un dictionnaire de textes
def etiquetage(dictionnaire):
    """
    Prend un dictionnaire avec des textes (clé = ID, valeur = dict avec 'tweet'),
    applique une étiquette à chaque texte, et sauvegarde le résultat dans un fichier JSON.
    """
    résultats = {}
    for i in dictionnaire:
        résultats[i] = {
            "tweet": dictionnaire[i],
            "label": etiquette(dictionnaire[i])
        }

    with open("tweets_etiquetés.json", "w", encoding="utf-8") as f:
        json.dump(résultats, f, ensure_ascii=False, indent=2)

    print("[✓] Fichier tweets_etiquetés.json généré.")



#lancer la fonction etiquetage sur un fichier .txt que l'on souhaite étiqueter. 
etiquetage(dico)
# Tests unitaires
print(etiquette("Fils caché, compagne non divorcée... Ces rumeurs sur François Hollande qui prolifèrent sur Internet"))






