import json
import csv
import spacy

# Chargement du modèle spaCy français
nlp = spacy.load("fr_core_news_sm")

# Chargement des tweets
with open("../brut_data.txt", mode='r', encoding='utf-8') as file:
    data = json.load(file)
dico = {int(key): value for key, value in data.items()}

# Initialisation
positivité = {}
mots_forts_négatifs = set()
verbes_positifs = set()
verbes_neutres = set()

# Chargement du lexique et classification dynamique
with open("../etiquetage_v1/lexique_pos_fr.csv", mode='r', encoding='utf-8-sig') as file:
    reader = csv.reader(file, delimiter=',', quotechar='"')
    for row in reader:
        mot = row[0].lower()
        try:
            score = float(row[1])
            positivité[mot] = score

            # Catégorisation dynamique
            if score <= -0.7:
                mots_forts_négatifs.add(mot)
            elif score >= 0.7:
                # POS sera détecté par spaCy → on vérifiera plus tard si ce mot est un verbe
                verbes_positifs.add(mot)

            # neutres souvent utilisés : score ≈ 0
            if abs(score) < 0.05:
                verbes_neutres.add(mot)

        except ValueError:
            continue

# Pondérations grammaticales
poids_pos = {
    "ADJ": 1.0,
    "ADV": 0.8,
    "VERB": 0.7,
    "NOUN": 0.4
}

# --- Fonction principale ---

def etiquette(tweet):
    doc = nlp(tweet)
    tokens_lower = [token.text.lower() for token in doc]

    # Détection contextuelle dynamique
    contient_mot_très_négatif = any(mot in mots_forts_négatifs for mot in tokens_lower)
    contient_verbe_positif = any(token.text.lower() in verbes_positifs and token.pos_ == "VERB" for token in doc)
    tous_verbes_sont_neutres = all(token.text.lower() in verbes_neutres for token in doc if token.pos_ == "VERB")

    score_total = 0
    poids_total = 0

    for token in doc:
        mot = token.text.lower()
        print (lemma)

        # Activation de la négation si on trouve un "ne", "pas", "plus", etc.
        if lemma in {"ne", "pas", "plus", "jamais", "aucun", "point", "n'"}:
            negation_active = True
            print("neg")
            continue

        # Vérification si le mot est dans le lexique
        if lemma in positivité:
            print("oui")
            score = positivité[lemma]
            poids = poids_pos.get(pos, 0)
        pos = token.pos_
        poids = poids_pos.get(pos, 0)

        if mot in positivité and poids > 0:
            score = positivité[mot]
            score_total += score * poids
            poids_total += poids

    score_pondéré = score_total / poids_total if poids_total > 0 else 0

    # Règle 1 : mot très négatif + verbe positif => boost
    if contient_mot_très_négatif and contient_verbe_positif:
        score_pondéré += 0.3

    # Règle 2 : neutralité factuelle si verbes très neutres
    if contient_mot_très_négatif and tous_verbes_sont_neutres and not contient_verbe_positif:
        print("→ Neutralité factuelle détectée")
        score_pondéré = 0.5

    # Clamp final
    score_pondéré = min(max(score_pondéré, 0), 1)

    print(f"Score : {score_pondéré:.3f}")
    return score_pondéré

# Fonction d’étiquetage d’un dictionnaire complet
def etiquetage(dictionnaire):
    return {i: [dictionnaire[i], etiquette(dictionnaire[i])] for i in dictionnaire}

etiquette("Fils caché, compagne non divorcée... Ces rumeurs sur François Hollande qui prolifèrent sur Internet")
etiquette("Le nombre de mort augementer")




