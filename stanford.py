from stanfordcorenlp import StanfordCoreNLP
import json
from langdetect import detect
from pre_traitement import read_saved_tweets,save_tweets,extract_twitter_data

# Chemin vers les fichiers CoreNLP
corenlp_path = './stanford-corenlp-4.5.9'

tweets = extract_twitter_data(['data/randomtweets3.txt']) 

dict_tweets = read_saved_tweets('brut_data.txt')
tweet_data = {}
nlp = StanfordCoreNLP(corenlp_path, lang='en')  # Utilisez 'en' pour l'anglais

with open("data_stanford/randomtweets3_sentiment.txt", "w", encoding="utf-8") as output_file:
    for tweet_id, tweet in tweets.items():
        """
        try:
            lang = detect(tweet)
        except:
            lang = "unknown"

        if lang == "en":
            # Initialiser le pipeline CoreNLP
            #nlp = StanfordCoreNLP(corenlp_path, lang='en')  # Utilisez 'en' pour l'anglais

            # Utiliser l'annotation pour analyser le sentiment
            props = {
                'annotators': 'sentiment',
                'outputFormat': 'json'
            }
            result = json.loads(nlp.annotate(tweet, properties=props))
            # Extraire le sentiment
            score = int(result['sentences'][0]['sentimentValue'])       
            
        elif lang == "fr":
            # Initialiser le pipeline CoreNLP
            #nlp = StanfordCoreNLP(corenlp_path, lang='fr')  # Utilisez 'en' pour l'anglais

            # Utiliser l'annotation pour analyser le sentiment
            props = {
                'annotators': 'sentiment',
                'outputFormat': 'json'
            }
            result = json.loads(nlp.annotate(tweet, properties=props))
            # Extraire le sentiment
            score = int(result['sentences'][0]['sentimentValue'])
            
        else:
            score = 0  # Neutre si la langue est inconnue
        """
        # Utiliser l'annotation pour analyser le sentiment
        props = {
                'annotators': 'sentiment',
                'outputFormat': 'json'
        }
        result = json.loads(nlp.annotate(tweet, properties=props))
        
        response = nlp.annotate(tweet, properties=props)
        
        if not response or response.strip() == "":
            print(f"Réponse vide pour le tweet {tweet_id} : {tweet!r}")
            continue
        try:
            result = json.loads(response)
        except Exception as e:
            print(f"Erreur JSON pour le tweet {tweet_id} : {e}")
            print("Réponse brute :", response)
            continue
        
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
        print("tweets save " + str(tweet_id))

    save_tweets(tweet_data, "randomtweets3_sentiment.txt")


# Fermer le pipeline CoreNLP
nlp.close()