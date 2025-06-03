import numpy as np
import json
from sklearn.ensemble import RandomForestClassifier


with open("brut_data.txt", mode='r', encoding='utf-8') as file:
        data = json.load(file)
    # Convertir les clés en int
data = {int(key): [value,0] for key, value in data.items()}



#créé le vocabluaire associé à l'ensemble des tweets sous la forme d'un dictionnaire qui associe à un mot une liste contenant son identifiant et sa fréquence dans la data
def vocabulaire(data):   
    voc={}                  
    i=0
    for tweet in data.values():
        mots=tweet[0].split()
        for k in range(len(mots)):
            if mots[k] in voc.keys():
                if mots[k] not in tweet[:k-1]:
                    voc[mots[k]][1]+=1
            else :
                voc[mots[k]]=[i,1]
                i+=1
    return voc

voc=vocabulaire(data)

def TF_IDF(mot,tweet,vocabulaire,data): #calcule le score TF IDF d'un mot dans un tweet, connaisant l'ensemble des mots pertinents à considérer ainsi que l'ensemble des tweets du corpus
    tf=0
    tweet_split = tweet.split()
    for x in tweet_split:
        if x ==mot:
            tf+=1
    if tf==0:
        return 0
    idf = np.log(len(data.keys())/vocabulaire[mot][1])
    return (1+ np.log(tf))*idf

def vectorisation(tweet,vocabulaire,data):
    vecteur= [0 for i in range( len( vocabulaire.keys() ) ) ]
    tweet_split=tweet.split()
    for x in tweet_split:
        if x in vocabulaire.keys():
            vecteur[vocabulaire[x][0]]=TF_IDF(x,tweet,vocabulaire,data)
    return vecteur


x_train=[vectorisation(tweet[0]) for tweet in data.values()]
y_train=[tweet[1] for tweet in data.values()]
x_test=


rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(x_train, y_train)

y_pred = rf_classifier.predict(x_test)