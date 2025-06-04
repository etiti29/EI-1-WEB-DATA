import numpy as np

def TF_IDF(mot,tweet,vocabulaire,data): #calcule le score TF IDF d'un mot dans un tweet, connaisant l'ensemble des mots pertinents à considérer ainsi que l'ensemble des tweets du corpus
    tf=0
    tweet_split = tweet.split()
    for x in tweet_split:
        if x ==mot:
            tf+=1
    if tf==0:
        return 0
    idf = np.log(len(data.keys()/vocabulaire[mot][1]))
    return (1+ np.log(tf))*idf

def vectorisation(tweet, vocabulaire, data):
    """
    Transforme un tweet en un vecteur de scores TF-IDF pour chaque mot du vocabulaire.
    Chaque position du vecteur correspond à un mot du vocabulaire.
    """
    vecteur = [0 for i in range(len(vocabulaire.keys()))]  # Initialise le vecteur à 0
    tweet_split = tweet.split()  # Découpe le tweet en mots
    for x in tweet_split:
        # Calcule le score TF-IDF pour chaque mot et l'affecte à la bonne position dans le vecteur
        vecteur[vocabulaire[x][0]] = TF_IDF(x, tweet, vocabulaire, data)
    return vecteur