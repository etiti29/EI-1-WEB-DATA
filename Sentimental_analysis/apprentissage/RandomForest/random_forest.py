import numpy as np
import json
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
texte="text_avis"  #mettre tweet pour le cas des tweets
fichier_entrainement="Sentimental_analysis/Iphone/scrapping_iphone/AVIS TXT/avis_train.txt"
# pour le cas des tweets on peut utiliser le fichier Sentimental_analysis/Twitter/data/data_traité/data70_etiq.txt

with open(fichier_entrainement, mode='r', encoding='utf-8') as file:
    data = json.load(file)
# Convertir les clés en int
data = {int(key): value for key, value in data.items()}




#créé le vocabluaire associé à l'ensemble des tweets sous la forme d'un dictionnaire qui associe à un mot une liste contenant son identifiant et sa fréquence dans la data
def vocabulaire(data):   
    voc={}                  
    i=0
    for content in data.values():
        mots=content[texte].split()
        for k in range(len(mots)):
            if mots[k] in voc.keys():
                if mots[k] not in mots[:k-1]:
                    voc[mots[k]][1]+=1
            else :
                voc[mots[k]]=[i,1]
                i+=1
    return voc


# Calcule le score TF-IDF d'un mot dans un tweet, connaissant l'ensemble des mots pertinents à considérer ainsi que l'ensemble des tweets du corpus
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

# Transforme un tweet en vecteur de caractéristiques en utilisant le vocabulaire et les scores TF-IDF
def vectorisation(tweet,vocabulaire,data):
    vecteur= [0 for i in range( len( vocabulaire.keys() ) ) ]
    tweet_split=tweet.split()
    for x in tweet_split:
        if x in vocabulaire.keys():
            vecteur[vocabulaire[x][0]]=TF_IDF(x,tweet,vocabulaire,data)
    return vecteur

voc=vocabulaire(data)

# Entraîne le modèle Random Forest sur les données d'entraînement et sauvegarde le modèle
def fit(fichier):
    x_train=[vectorisation(content[texte],voc,data) for content in data.values()]
    y_train=[content["label"] for content in data.values()]
    rf_classifier = RandomForestClassifier(n_estimators=200, random_state=42,max_depth=None , max_features="sqrt",min_samples_leaf=1,min_samples_split=5)
    rf_classifier.fit(x_train, y_train)
    joblib.dump(rf_classifier, 'Sentimental_analysis/apprentissage/RandomForest/random_forest_model.joblib')

# Teste le modèle sur un fichier de test et affiche les métriques de performance
def test(fichier):
    with open(fichier, mode='r', encoding='utf-8') as file:
        data_test = json.load(file)
    # Convertir les clés en int
    data_test = {int(key): value for key, value in data_test.items()}
    x_test=[vectorisation(content[texte],voc,data_test) for content in data_test.values()]
    y_test=[content["label"] for content in data_test.values()]
    y_pred = rf_classifier.predict(x_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))
    k=0
    for i in range(len(y_test)):
        if y_pred[i]!=y_test[i]:
            k+=1
    print(k, len(y_pred))

rf_classifier = joblib.load('Sentimental_analysis/apprentissage/RandomForest/random_forest_model.joblib')

fit(fichier_entrainement)
test("Sentimental_analysis/Iphone/scrapping_iphone/AVIS TXT/avis_validation.txt")
# pour le cas des tweets on peut utiliser le fichier Sentimental_analysis/Twitter/data/data_traité/data10_etiq.txt


# Chargement du modèle et prédiction d'un exemple
'''
tweet = "Parfait ! Reçu très rapidement et comme neuf. Batterie à 100%."
y_pred = rf_classifier.predict([vectorisation(tweet,voc,data)])
print(y_pred)
'''