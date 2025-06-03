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
    
produit_lexique={"excellent": 1,"decharger":-0.8,"recommander": 0.8,"bémol": -0.5 ,"telephone" : 1,'produit' :0.7,'iphone' : 1, "mobile" :0.8 ,"Apple" :1,"écran" :1,"iOS" : 1,"application" :0.5,"Siri":1,"smartphone" :0.5,"écouteur" :0.2,"App Store" :0.7 ,"Steve Jobs" :1,"mobile" :0.5 ,"téléphone" :0.5 ,"iTunes" : 0.6, "capteur" : 0.6,"compatible" : 0.6, "télécharger" :0.4,"USB" :0.3,"Android" :-1,"appareil" :0.3,"Samsung" : -1,"Wi-Fi" :0.5,"FaceTime" : 0.5 ,"appli" : 0.3 , "camera" : 0.8, "surchauffe" : -1,"admirer" :1,"adorer" : 1,"affectionner" : 0.7,"apprécier" : 0.6, "aimer" :0.9,"detester": -1,"degouter":-1,"demeurer" : 0.5, "devenir" : 0.5, "être" : 0.5, "sembler" : 0.4, "paraître": 0.4, "reste" :0.4,"fuir":-0.9}
def analyse(phrase):
    nlp = spacy.load("fr_core_news_sm")
    doc = nlp(phrase)
    score=0
    for token in doc :
        if token.dep_ not in ["det"]:
            print(token.lemma_)
            if token.lemma_ in produit_lexique :  
                if token.head.lemma_ in produit_lexique and token.head.lemma != token.lemma : 
                    print(token.lemma_,token.head.lemma_)
                    score+=produit_lexique[token.lemma_]*produit_lexique[token.head.lemma_]
    print(score)
    if score >0.1 :
        print("positif")
    elif score <-0.1 :
        print("négatif")
    else : 
        print("neutre")
    

                

analyse("Pour un état excellent, la batterie se décharge très vite")