import json
import spacy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Chargement du modèle spaCy anglais
nlp = spacy.load("en_core_web_sm")

# Initialisation de VADER
vader = SentimentIntensityAnalyzer()

# Pondération des classes grammaticales
POS_WEIGHTS = {
    "ADJ": 1.5,
    "VERB": 1.3,
    "ADV": 1.2,
    "NOUN": 1.0
}

# Liste de mots de négation
NEGATIONS = {"not", "n't", "no", "never", "ne", "pas", "aucun", "jamais", "n'"}

def custom_sentiment_analysis(text):
    doc = nlp(text)
    vader_score = vader.polarity_scores(text)
    base_score = vader_score['compound']
    adjusted_score = 0
    total_weight = 0
    contains_negation = any(tok.lower_ in NEGATIONS for tok in doc)

    for tok in doc:
        if tok.pos_ in POS_WEIGHTS:
            token_score = vader.polarity_scores(tok.text)['compound']
            weight = POS_WEIGHTS[tok.pos_]
            if tok.is_upper:
                weight *= 1.2
            adjusted_score += token_score * weight
            total_weight += weight

    final_score = adjusted_score / total_weight if total_weight > 0 else base_score

    if contains_negation:
        final_score *= -1

    if "!" in text:
        final_score *= 1.3
        

    final_score = max(-1, min(1, final_score))
    return final_score

def get_sentiment_label(score):
    if score >= 0.05:
        return "positive"
    elif score <= -0.05:
        return "negative"
    else:
        return "neutral"

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
        
    with open(output_path, "w", encoding="utf-8") as f_out:
        json.dump(results, f_out, ensure_ascii=False, indent=2)

    print(f"Analyse terminée. Résultats enregistrés dans : {output_path}")

# === Exécution ===
if __name__ == "__main__":
    analyze_file("../brut_data_en.txt", "brut_data_en_output.json")

