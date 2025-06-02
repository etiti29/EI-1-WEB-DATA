import json
import csv

# ouverture des données des tweets
with open("brut_data.txt", mode='r', encoding='utf-8') as file:
    data = json.load(file)
dico= {int(key): value for key, value in data.items()}

#creation d'un dictionnaire de positivité des termes a partir d'une base de données existantes 
positivité={}
with open("etiquetage_v1/lexique_pos_fr.csv", mode='r', encoding='utf-8-sig') as file : 
    reader = csv.reader(file, delimiter=',', quotechar='"')
    for row in reader:
        positivité[row[0]]=row[1]


def etiquette(tweet): # détermine si un tweet est positif ou négatif
    mots = tweet.split()
    score_moyen_mots = 0
    nb_mots=0
    for mot in mots : 
        if mot in positivité.keys():
            score_moyen_mots+=float(positivité[mot])
            nb_mots+=1
    if nb_mots>0:
        print(nb_mots)
        score_moyen_mots=score_moyen_mots/nb_mots
    print(score_moyen_mots)

etiquette("Mon fils est sauve d'un cancer")



def etiquetage(dictionnaire):
    dictionnaire_etiqueté = {}
    for i in dictionnaire.keys():
        dictionnaire_etiqueté[i]=[dictionnaire[i],etiquette(dictionnaire[i])]
    return dictionnaire_etiqueté

