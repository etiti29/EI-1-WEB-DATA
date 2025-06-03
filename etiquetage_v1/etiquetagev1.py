import json
import csv
import spacy

# Chargement du modèle spaCy français
nlp = spacy.load("fr_core_news_sm")

# Chargement du corpus brut
with open("../brut_data.txt", mode='r', encoding='utf-8') as file:
    data = json.load(file)
dico = {int(key): value for key, value in data.items()}

# Chargement du lexique de polarité
positivité = {}
mots_forts_négatifs = set()
verbes_positifs = set()
verbes_neutres = set()

with open("../etiquetage_v1/lexique_pos_fr.csv", mode='r', encoding='utf-8-sig') as file:
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

# Poids selon la classe grammaticale
poids_pos = {
    "ADJ": 1.0,
    "ADV": 0.8,
    "VERB": 0.7,
    "NOUN": 0.4
}

def etiquette(tweet):
    doc = nlp(tweet)
    tokens = list(doc)

    score_total = 0
    poids_total = 0
    negation_active = False

    contient_mot_très_négatif = False
    contient_verbe_positif = False
    tous_verbes_sont_neutres = True

    for i, token in enumerate(tokens):
        lemma = token.lemma_.lower()
        pos = token.pos_
        mot = token.text.lower()

        # Activation de la négation si on trouve un "ne", "pas", "plus", etc.
        if lemma in {"ne", "pas", "plus", "jamais", "aucun", "point", "n'"}:
            negation_active = True
            print("neg")
            continue

        # Vérification si le mot est dans le lexique
        if lemma in positivité:
            score = positivité[lemma]
            poids = poids_pos.get(pos, 0)

            # Inversion du score si négation active
            score_total += score * poids
            poids_total += poids

            # Mémorisation pour règles contextuelles
            if score <= -0.7:
                contient_mot_très_négatif = True
            if score >= 0.7 and pos == "VERB":
                contient_verbe_positif = True

        # Vérification neutralité verbes
        if pos == "VERB" and lemma not in verbes_neutres:
            tous_verbes_sont_neutres = False

    score_pondéré = score_total / poids_total if poids_total > 0 else 0

    # Règle 1 : très négatif + verbe positif => boost
    if contient_mot_très_négatif and contient_verbe_positif:
        score_pondéré += 0.3

    # Règle 2 : phrase neutre factuelle
    if contient_mot_très_négatif and tous_verbes_sont_neutres and not contient_verbe_positif:
        print("→ Neutralité factuelle détectée")
        score_pondéré = 0.5
    
    if negation_active:
        if score_pondéré != 0:
            score_pondéré *= -1
        else:
            score_pondéré = 1.0  # ta règle : neutre inversé = très positif
        negation_active = False


    score_pondéré = min(max(score_pondéré, 0), 1)

    print(f"Score : {score_pondéré:.3f}")
    return score_pondéré

def etiquetage(dictionnaire):
    return {i: [dictionnaire[i], etiquette(dictionnaire[i])] for i in dictionnaire}

etiquette("Le peuple fait la fête a Montparnasse, a Paris avec Delanoe, Hidalgo, Huchon, le fils Hollande ... Du pain et des jeux, vive le peuple !")



