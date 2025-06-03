import json
from langdetect import detect
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from pattern.fr import sentiment as fr_sentiment

from pre_traitement import read_saved_tweets

analyzer = SentimentIntensityAnalyzer()
dict_tweets = read_saved_tweets('brut_data.txt')

with open("sentiment_output.txt", "w", encoding="utf-8") as output_file:
    for tweet_id, tweet in dict_tweets.items():
        try:
            lang = detect(tweet)
        except:
            lang = "unknown"

        if lang == "en":
            score = analyzer.polarity_scores(tweet)["compound"]
        elif lang == "fr":
            score = fr_sentiment(tweet)[0]
        else:
            score = 0.0  # Neutre si la langue est inconnue

        # Classification
        if score >= 0.5:
            label = "positif"
        elif score <= -0.5:
            label = "négatif"
        else:
            label = "neutre"

        tweet_data = {
            "id": tweet_id,
            "tweet": tweet,
            "score": round(score, 3),
            "label": label
        }

        output_file.write(json.dumps(tweet_data, ensure_ascii=False) + "\n")
