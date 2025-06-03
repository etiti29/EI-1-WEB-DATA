from transformers import pipeline
from pre_traitement import extract_twitter_data,save_tweets

try:
    # Modèle multilingue performant pour sentiment (ex: 'nlptown/bert-base-multilingual-uncased-sentiment')
    #classifier = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
    classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    #classifier = pipeline("sentiment-analysis", model="tblard/tf-allocine")

    tweets = extract_twitter_data(['data/randomtweets3.txt']) 
    tweet_data = {}
    tweet_id = 0
    
    for text in tweets.values():
        result = classifier(text)[0]
        tweet_data[tweet_id] = {
            "tweet": text,
            "score": result['score'],
            "label": result['label']
        }
        tweet_id += 1
        print(f"Texte: {text}\nSentiment: {result['label']} (score: {result['score']:.3f})\n")
        

    save_tweets(tweet_data, "randomtweets3_sentiment.txt")
except Exception as e:
    print(e)