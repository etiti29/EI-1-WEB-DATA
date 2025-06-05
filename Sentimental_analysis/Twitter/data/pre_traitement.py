import csv
import json
import random

def extract_twitter_data(csv_file_path):
    twitter_data = {}
    index = 0
    with open(csv_file_path, mode='r', encoding='utf-8-sig') as file: # 'utf-8-sig' pour gérer les BOM éventuels
        first = file.read(1) # Lire le premier caractère pour vérifier le délimiteur
        file.seek(0) #on remet le curseur au début du fichier
        #2 types de fichiers : avec des guillemets ou sans => 2 types de lecteurs
        if first == '"':
            reader = csv.reader(file, delimiter=',', quotechar='"')
            for row in reader:
                twitter_data[index] = row[1]
                index += 1
        else:
            reader = csv.DictReader(file, delimiter=';', quotechar='"')
            for row in reader:
                twitter_data[index] = row['content']
                index += 1

    
    return twitter_data

def extract_twitter_data_files(list_csv_file_path):
    """
    Extrait les données d'un fichier CSV et les transforme en un dictionnaire de dictionnaires.
    
    Args:
        csv_file_path (str): Chemin vers le fichier CSV.
    
    Returns:
        dict: Dictionnaire de dictionnaires contenant les données du CSV.
    """
    twitter_data = {}
    index=0
    for doc in list_csv_file_path:
        with open(doc, mode='r', encoding='utf-8-sig') as file: # 'utf-8-sig' pour gérer les BOM éventuels
            first = file.read(1) # Lire le premier caractère pour vérifier le délimiteur
            file.seek(0) #on remet le curseur au début du fichier
            #2 types de fichiers : avec des guillemets ou sans => 2 types de lecteurs
            if first == '"':
                reader = csv.reader(file, delimiter=',', quotechar='"')
                for row in reader:
                    twitter_data[index] = row[1]
                    index += 1
            else:
                reader = csv.DictReader(file, delimiter=';', quotechar='"')
                for row in reader:
                    twitter_data[index] = row['content']
                    index += 1

    
    return twitter_data

brut_data = extract_twitter_data(['data/hollande.txt','data/lemon.txt','data/pin.txt','data/swine-flu.txt','data/randomtweets1.txt','data/randomtweets2.txt','data/randomtweets3.txt','data/randomtweets4.txt','data/RihannaConcert2016En.txt','data/RihannaConcert2016Fr.txt','data/rumors_disinformation.txt','data/UEFA_Euro_2016_En.txt','data/UEFA_Euro_2016_Fr.txt'])
brut_data_en = extract_twitter_data(['data/swine-flu.txt','data/randomtweets3.txt','data/randomtweets4.txt','data/RihannaConcert2016En.txt','data/UEFA_Euro_2016_En.txt'])
        
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
        text = tweet_data
        words = text.split()  # Divise le texte en mots en utilisant les espaces comme séparateurs
        cleaned_words = [word.lower().rstrip('.?,!') for word in words]
        tweets_words[tweet_id] = cleaned_words
    
    return tweets_words

#data = extract_tweets(brut_data)
#print(data[0])  # Affiche les mots du tweet avec l'ID 1


def save_tweets(tweets, file_path):
    """
    Sauvegarde un dictionnaire de tweets dans un fichier JSON.
    
    Args:
        tweets (dict): Dictionnaire contenant les tweets.
        file_path (str): Chemin vers le fichier où sauvegarder les tweets.
    """
    with open(file_path, mode='w', encoding='utf-8') as file:
        json.dump(tweets, file, ensure_ascii=False, indent=4)

# Sauvegarder le dictionnaire dans un fichier texte
with open('brut_data.txt', mode='w', encoding='utf-8') as file:
    json.dump(brut_data, file, ensure_ascii=False, indent=4)
with open('data.txt', mode='w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
with open('brut_data_en.txt', mode='w', encoding='utf-8') as file:
    json.dump(brut_data_en, file, ensure_ascii=False, indent=4)

print("Les dictionnaires ont été sauvegardés.txt")


#####

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

#l70, l20, l10 = partition_random(100)
#print(len(l70), len(l20), len(l10))  # Devrait afficher environ 71 20 10 (car 0 à 100 = 101 éléments)
#print(sorted(l70 + l20 + l10) == list(range(101)))  # True, les listes forment bien une partition'''

import pandas as pd

import json

# Charger le CSV
df = pd.read_csv('scrapping_iphone/avis_validation.csv', encoding='latin1')
# Construire le dictionnaire de dictionnaires
tweets_dict = {
    row['id']: {
        'text_avis': row['text_avis'],
        'label': row['label']
    }
    for _, row in df.iterrows()
}


#print(tweets_dict)  # Afficher le dictionnaire de dictionnaires


# Supposons que tweets_dict existe déjà
# tweets_dict = { ... }

# 1. Ouvrir (ou créer) le fichier TXT en écriture
with open('avis_validation.txt', 'w', encoding='latin1') as f:
    # 2. Sérialiser le dictionnaire au format JSON avec indent pour lisibilité
    json.dump(tweets_dict, f, ensure_ascii=False, indent=4)

print("Export terminé : 'avis_validation.txt' créé.")
