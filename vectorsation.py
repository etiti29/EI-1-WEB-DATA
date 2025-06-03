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

def vectorisation(tweet,vocabulaire,data):
    vecteur= [0 for i in range( len( vocabulaire.keys() ) ) ]
    tweet_split=tweet.split()
    for x in tweet_split:
        vecteur[vocabulaire[x][0]]=TF_IDF(x,tweet,vocabulaire,data)
    return vecteur