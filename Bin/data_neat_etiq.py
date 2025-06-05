import json
import random

# Fonction qui crée 3 listes d'indices pour la partition 70%-20%-10%
def partition_random(n):
    indices = list(range(n + 1))  # indices de 0 à n
    random.shuffle(indices)
    n70 = int(0.7 * (n + 1))
    n20 = int(0.2 * (n + 1))
    l70 = indices[:n70]
    l20 = indices[n70:n70 + n20]
    l10 = indices[n70 + n20:]
    return l70, l20, l10

# Simulation de ta fonction read_saved_tweets qui charge les tweets
def read_saved_tweets(filepath):
    tweets = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                tweets.append(json.loads(line))
    return tweets

tweets_words = read_saved_tweets('sentiment_output.txt')
N = len(tweets_words)

l70, l20, l10 = partition_random(N - 1)

def create_lists(l):
    tweets_list = {}
    for k in l:
        tweets_list[k] = tweets_words[k]
    return tweets_list

data70_etiq = create_lists(l70)
data20_etiq = create_lists(l20)
data10_etiq = create_lists(l10)

with open('data70_etiq.txt', mode='w', encoding='utf-8') as file:
    json.dump(data70_etiq, file, ensure_ascii=False, indent=4)

with open('data20_etiq.txt', mode='w', encoding='utf-8') as file:
    json.dump(data20_etiq, file, ensure_ascii=False, indent=4)

with open('data10_etiq.txt', mode='w', encoding='utf-8') as file:
    json.dump(data10_etiq, file, ensure_ascii=False, indent=4)
