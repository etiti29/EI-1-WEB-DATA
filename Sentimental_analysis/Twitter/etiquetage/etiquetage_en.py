import json
import spacy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Chargement du modèle linguistique spaCy pour l’anglais
nlp = spacy.load("en_core_web_sm")

# Initialisation de l’analyseur de sentiment VADER
vader = SentimentIntensityAnalyzer()

# Pondération selon les classes grammaticales (plus de poids aux adjectifs/verbres)
POS_WEIGHTS = {
    "ADJ": 1.5,
    "VERB": 1.3,
    "ADV": 1.2,
    "NOUN": 1.0
}

# Liste de mots indiquant une négation (en anglais et en français)
NEGATIONS = {"not", "n't", "no", "never", "ne", "pas", "aucun", "jamais", "n'"}

# Fonction principale d’analyse de sentiment avec pondération grammaticale et détection de négation
def custom_sentiment_analysis(text):
    doc = nlp(text)
    vader_score = vader.polarity_scores(text)
    base_score = vader_score['compound']  # score global donné par VADER

    adjusted_score = 0
    total_weight = 0

    # Vérifie si le texte contient une forme de négation
    contains_negation = any(tok.lower_ in NEGATIONS for tok in doc)

    # Pondération grammaticale de chaque mot
    for tok in doc:
        if tok.pos_ in POS_WEIGHTS:
            token_score = vader.polarity_scores(tok.text)['compound']
            weight = POS_WEIGHTS[tok.pos_]
            if tok.is_upper:  # Majuscules = intensification
                weight *= 1.2
            adjusted_score += token_score * weight
            total_weight += weight

    # Moyenne pondérée ou score brut si aucun mot pondéré
    final_score = adjusted_score / total_weight if total_weight > 0 else base_score

    # Inversion du score si une négation est détectée
    if contains_negation:
        final_score *= -1

    # Amplifie si on détecte un point d’exclamation
    if "!" in text:
        final_score *= 1.3

    # Clamp du score entre -1 et 1
    final_score = max(-1, min(1, final_score))
    return final_score

# Convertit un score en une étiquette de sentiment
def get_sentiment_label(score):
    if score >= 0.05:
        return "positive"
    elif score <= -0.05:
        return "negative"
    else:
        return "neutral"

# Analyse un fichier JSON (clé=id, valeur=texte) et écrit un fichier JSON avec score + label
def analyze_file(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    results = {}
    for id_str, text in data.items():
        score = custom_sentiment_analysis(text)
        label = get_sentiment_label(score)
        results[id_str] = {
            "text": text,
            "score": score,
            "label": label
        }

    # Sauvegarde des résultats
    with open(output_path, "w", encoding="utf-8") as f_out:
        json.dump(results, f_out, ensure_ascii=False, indent=2)

    print(f"Analyse terminée. Résultats enregistrés dans : {output_path}")

# === Exécution directe si lancé comme script ===
if __name__ == "__main__":
    analyze_file("Sentimental_analysis/Twitter/data/brut_data.txt", "brut_data_en_output.json")

