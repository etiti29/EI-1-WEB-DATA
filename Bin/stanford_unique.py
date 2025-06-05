#Algo stanford sur un seul tweet

from stanfordcorenlp import StanfordCoreNLP
import json
from langdetect import detect
from Sentimental_analysis.Twitter.data.pre_traitement import read_saved_tweets,save_tweets,extract_twitter_data

# Chemin vers les fichiers CoreNLP
corenlp_path = './stanford-corenlp-4.5.9'

tweet_data = {}
nlp = StanfordCoreNLP(corenlp_path, lang='en')  # Utilisez 'en' pour l'anglais

tweet = "South Africa: Two Cases of Swine Flu Confirmed in Bloemfentein…"

# Utiliser l'annotation pour analyser le sentiment
props = {
        'annotators': 'sentiment',
        'pipelineLanguage': 'en',
        'outputFormat': 'json'
}
result = json.loads(nlp.annotate(tweet, properties=props))
# Extraire le sentiment
score = int(result['sentences'][0]['sentimentValue'])

#Classification
if score >= 3:
    label = "positif"
elif score <= 1:
    label = "negatif"
else:
    label = "neutre"

print(tweet)
print(f"Score: {score}, Label: {label}")

# Fermer le pipeline CoreNLP
nlp.close()