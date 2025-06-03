import spacy

'''
# Charger le modèle de langue français
nlp = spacy.load("fr_core_news_sm")

# Phrase d'exemple
phrase = "L'iphone est super et son écran incassable"

# Analyse de la phrase
doc = nlp(phrase)

# Afficher la fonction grammaticale de chaque mot
for token in doc:
    print(f"Mot : {token.text}, Fonction grammaticale : {token.dep_}, Mot racine : {token.head.text}")
'''
    
produit_lexique={'commande': 0.7,'rapide' : 0.7,'livraison': 0.8,'aucune' : -0.8,'aucun':-0.8,'rayure':-0.9,'perdre': '-0.9', 'plus': '0.2', 'de': '0', '20': '0', 'pourcent': '0', 'ne': '-1', 'parler': '0', 'même': '0', '...': '-0.3', 'Déçu': '-1', 'content': '1', 'achat': '0.8', 'aller': '0', '93': '0', 'déçu': '-1', 'le': '0', 'mettre': '0', 'charge': '0.8', 'temps': '0', 'monter': '0','présent': '0.2', 'site': '0.2', 'iphon': '1', 'luire': '0.7', 'meme': '0', 'parfaire': '0.9', 'etat': '0.9', 'neuf': '0.9', 'batterie': '1', '100': '0', 'chargeur': '1', 'cabl': '1', 'seul': '0.2', 'recevoir': '0.3', 'souci': '-0.8', 'bout': '0', 'se': '0', 'décoller': '-0.9', ',': '0','gros': '0.4', 'j’': '0', 'avoir': '0.5', 'devoir': '-0.3', 'remplacer': '-0.7', 'et': '0', 'modèle': '0.4', 'importer': '0.4', 'état': '0.8', 'qui': '0', 'n’': '-1', 'donc': '0', 'pas': '-1', 'ce': '0','Conforme': '0.5', '.': '0', 'voir': '0.3', 'utilisation': '0.6', 'produire': '0.5', 'non': '-1', 'conforme': '0.5', 'description': '0.6',"excellent": 1,"decharger":-0.8,"recommander": 0.8,"bémol": -0.5 ,"telephone" : 1,'produit' :0.7,'iphone' : 1, "mobile" :0.8 ,"Apple" :1,"écran" :1,"iOS" : 1,"application" :0.5,"Siri":1,"smartphone" :0.5,"écouteur" :0.2,"App Store" :0.7 ,"Steve Jobs" :1,"mobile" :0.5 ,"téléphone" :0.5 ,"iTunes" : 0.6, "capteur" : 0.6,"compatible" : 0.6, "télécharger" :0.4,"USB" :0.3,"Android" :-1,"appareil" :0.3,"Samsung" : -1,"Wi-Fi" :0.5,"FaceTime" : 0.5 ,"appli" : 0.3 , "camera" : 0.8, "surchauffe" : -1,"admirer" :1,"adorer" : 1,"affectionner" : 0.7,"apprécier" : 0.6, "aimer" :0.9,"detester": -1,"degouter":-1,"demeurer" : 0.5, "devenir" : 0.5, "être" : 0.5, "sembler" : 0.4, "paraître": 0.4, "reste" :0.4,"fuir":-0.9}
def analyse(phrase):
    nlp = spacy.load("fr_core_news_sm")
    doc = nlp(phrase)
    score=0
    for token in doc :
        if token.dep_ not in ["det"]:
            if token.lemma_ in produit_lexique :  
                if token.head.lemma_ in produit_lexique and token.head.lemma != token.lemma : 
                    print(token.lemma_,token.head.lemma_)
                    score+=float(produit_lexique[token.lemma_])*float(produit_lexique[token.head.lemma_])
    print(score)
    if score >0.1 :
        print("positif")
    elif score <-0.1 :
        print("négatif")
    else : 
        print("neutre")
    

                

analyse("La commande est nulle, Le produit est rayé")

data="la batterie a perdu plus de 20% de sa capacité ne parlons même pas de la surchauffe du téléphone... Déçu Je suis contente de mon achat sauf que la batterie ne va pas plus que 93% et donc déçu. Je le met en charge et il met du temps à monter"


def apprentissage(data):
    d={}
    nlp = spacy.load("fr_core_news_sm")
    doc = nlp(data)
    for token in doc:
        if not token.lemma_ in produit_lexique and token.dep_ not in ['det','mark','case','nmod','dep','nsubj','cc','nummod']: 
            print(token.dep_)
            d[token.lemma_]=input(token.lemma_)
    print(d)
#apprentissage(data)
