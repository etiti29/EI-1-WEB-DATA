import csv

def extract_twitter_data(csv_file_path):
    """
    Extrait les données d'un fichier CSV et les transforme en un dictionnaire de dictionnaires.
    
    Args:
        csv_file_path (str): Chemin vers le fichier CSV.
    
    Returns:
        dict: Dictionnaire de dictionnaires contenant les données du CSV.
    """
    twitter_data = {}
    
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            tweet_id = int(row['Tweet_ID'])
            twitter_data[tweet_id] = {
                'Username': row['Username'],
                'Text': row['Text'],
                'Retweets': int(row['Retweets']),
                'Likes': int(row['Likes']),
                'Timestamp': row['Timestamp']
            }
    
    return twitter_data

def extract_tweets(dict):
    """
    Transforme le dictionnaire des tweets en un dictionnaire où chaque ID de tweet est associé à une liste de mots.
    
    Args:
        dict (dict): Dictionnaire contenant les données des tweets.
    
    Returns:
        dict: Dictionnaire avec les IDs de tweets comme clés et les listes de mots comme valeurs.
    """
    tweets_words = {}
    
    for tweet_id, tweet_data in dict.items():
        text = tweet_data['Text']
        words = text.split()  # Divise le texte en mots en utilisant les espaces comme séparateurs
        cleaned_words = [word.lower().rstrip('.') for word in words]
        tweets_words[tweet_id] = cleaned_words
    
    return tweets_words

document = extract_twitter_data('twitter_dataset.csv')

tweets = extract_tweets(document)

print(tweets[1])

#####


import random

def partition_random(N):
    # Ensemble complet des entiers de 0 à N
    full_list = list(range(N+1))
    random.shuffle(full_list)
    
    taille_70 = int(0.7 * (N+1))
    taille_20 = int(0.2 * (N+1))
    taille_10 = (N+1) - taille_70 - taille_20  # pour que la somme soit exacte
    
    list_70 = full_list[:taille_70]
    list_20 = full_list[taille_70:taille_70+taille_20]
    list_10 = full_list[taille_70+taille_20:]
    
    return list_70, list_20, list_10

l70, l20, l10 = partition_random(100)
print(len(l70), len(l20), len(l10))  # Devrait afficher environ 71 20 10 (car 0 à 100 = 101 éléments)
print(sorted(l70 + l20 + l10) == list(range(101)))  # True, les listes forment bien une partition


####