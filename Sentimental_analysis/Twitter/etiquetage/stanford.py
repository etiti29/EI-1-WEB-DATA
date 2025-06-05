#Algo stanford sur un fichier de tweets

from stanfordcorenlp import StanfordCoreNLP
import json
from langdetect import detect
from EI_1_WEB_DATA.Sentimental_analysis.Twitter.data.pre_traitement import read_saved_tweets, save_tweets, extract_twitter_data

# Chemin vers les fichiers CoreNLP
corenlp_path = './stanford-corenlp-4.5.9'

# Charger les tweets
tweets = extract_twitter_data(['data/randomtweets3.txt'])
dict_tweets = read_saved_tweets('brut_data.txt')
tweet_data = {}

# Initialiser le pipeline CoreNLP
nlp = StanfordCoreNLP(corenlp_path, lang='en')  # Utilisez 'en' pour l'anglais

with open("data_stanford/randomtweets3_sentiment.txt", "w", encoding="utf-8") as output_file:
    for tweet_id, tweet in tweets.items():
        try:
            # Utiliser l'annotation pour analyser le sentiment
            props = {
                'annotators': 'sentiment',
                'outputFormat': 'json'
            }
            response = nlp.annotate(tweet, properties=props)

            if not response or response.strip() == "":
                print(f"Réponse vide pour le tweet {tweet_id} : {tweet!r}")
                continue

            result = json.loads(response)

            # Extraire le sentiment
            score = int(result['sentences'][0]['sentimentValue'])

            # Classification
            if score >= 3:
                label = "positif"
            elif score <= 1:
                label = "negatif"
            else:
                label = "neutre"

            tweet_data[tweet_id] = {
                "tweet": tweet,
                "score": score,
                "label": label
            }
            print(f"Tweet sauvegardé : {tweet_id}")

        except Exception as e:
            print(f"Erreur lors du traitement du tweet {tweet_id} : {e}")
            continue

# Sauvegarder les tweets analysés
save_tweets(tweet_data, "randomtweets3_sentiment.txt")

# Fermer le pipeline CoreNLP
nlp.close()
