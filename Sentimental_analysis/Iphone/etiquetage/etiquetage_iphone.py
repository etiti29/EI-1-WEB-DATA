"""
Script d’étiquetage automatique des avis iPhone en français par analyse lexicale et syntaxique.

Fonctionnement :
- Utilise le modèle spaCy `fr_core_news_sm` pour analyser la structure des phrases.
- Associe un score à chaque mot selon un lexique prédéfini pondéré.
- Calcule un score global pour prédire un label de sentiment (positif, neutre, négatif).

À lancer avec : `python etiquetage_iphone.py`

Bibliothèques nécessaires :
pip install spacy scikit-learn
python -m spacy download fr_core_news_sm
"""

import spacy
from sklearn.metrics import classification_report, accuracy_score
import json

# Lexique partiel des mots avec leur score de polarité (positif, négatif, neutre)
# (ce lexique est à compléter ou charger depuis un fichier selon le projet)
produit_lexique = {'très': 2, 'heureux' : 1,'heureuse' : 1,'latéral': '0', 'Bonjour': '0', 'air': '0', 'dommage': '-1', 'préciser': '0.4', 'récupérable': '0.3', 'avai': '0', 'en': '0', 'fonctionnement': '1', 'physique': '0', 'boite': '0.4', 'blister': '0.5', 'également': '0', 'pré-installé': '0.5', 'attention': '-1', 'livrer': '0.7', 'posséder': '0', 'e-sim': '1', 'part': '0', 'hésiter': '-0.3', 'aussi': '0', 'casser': '-1', 'facilement': '1', 'mais': '0', 'sinon': '0.5', 'ensemble': '0', 'signaler': '-0.7', 'tel': '1', 'réellement': '1', 'croire': '1', 'choquer': '1', 'satisfait': '1', 'colis': '0.5', '24h': '0', 'délaisser': '-0.6', 'moi': '0', 'y': '0', 'vous': '0', 'regretter': '-0.8', ';': '0', '-).produit': '0', 'reconditionnement': '0.5','reconnaître': '0.4', 'inconnue': '-0.4', 'absolument': '2', 'escro': '-2', '.vendeur': '0.4', 'sérieux': '1', 'envoyer': '1', 'J’': '0', 'peur': '-1', 'avis': '1', 'c': '0', 'top': '2', 'convenable': '0.5', 'cependant': '-0.5', 'payer': '0.4', 'expresse': '1', 'cela': '0', 'chauffe': '-1', 'beaucoup': '2', 'décollage': '-1', 'eter': '0', 'trop': '2', 'cher': '-1', 'contre': '-0.3', 'haut': '0', 'focntionne': '1', 'parleur': '1', 'deception': '-1', 'nouveau': '1', 'tarvail': '0', 'realiser': '0.3', 'reconditionneur': '0.3', 'photo': '1', 'mise': '0', 'cm': '0', 'objet': '0', 'impossible': '-1', 'prendre': '0.5', 'exemple': '0', 'fleur': '0', 'document': '0.4', 'etc.': '-0.3', 'surtout': '2', 'vidéo': '1', 'instant': '0.8', 'manquer': '-0.7','prix': '1', 'coque': '1', 'vitre': '1', 'protection': '1', 'verre': '1', 'trempé': '1', 'original': '1', 'aurai': '0', 'venir': '0.5', 'fortement': '2', 'vendeur': '1', 'équipe': '1', 'adaptateur': '1', 'm’': '0', 'donner': '1', 'fil': '1', 'abordable': '1', 'je': '0', 'utiliser': '1', 'coqu': '1', 'arrière': '1', 'parfaitement': '2', 'moins': '-1', 'jour': '0', 'semaine': '0', 'charger': '1', '10h': '0', 'rien': '-0.5', 'niquel': '2','déçue': '-1', 'l’': '0', 'acheter': '0', 'janvier': '0', '..': '0', '25': '0', 'déjà': '0', 'savoir': '0', 'correctement': '1', 'boîte': '1', 'câbl': '1', 'SMARTPHONE': '1', 'RECONDITIONNER': '1', 'SATISFAIT': '1', 'arriver': '1', 'vie': '0.3', 'merci': '1', 'encore': '-0.5', '.le': '0', 'envoi': '0.5', 'pouvoir': '0.5', 'me': '0', 'prononcer': '0', 'durabilité': '1', 'rapport': '1', 'meilleur': '2', 'trace': '-1', 'd’': '0', 'usur': '-1', 'emballer': '1', 'protéger': '1', 'offerte': '2', 'nickel': '2', 's’': '0', 'utilis': '1', 'un': '0', 'peu': '0.3', 'vite': '1', 'penser': '1', 'normal': '0.4', 'que': '0', 'c’': '0', 'mini': '0.6', 'niveau': '0.6', 'vivement': '0.9', '.iphone': '1', 'rapidement': '1', 'propre': '1', 'paramètre': '1', 'oled': '1', '(': '0', 'origin': '1', 'vue': '0', 'qualité': '1', ')': '0', 'mieux': '2', 'quoi': '-1', 'foncer': '2', 'oeil': '0', 'fermer': '0', 'faire': '1', 'update': '1', 'mois': '0', 'suivre': '0', 'moment': '0','mèr': '0', 'h': '0', '?': '1', 'bonjour': '0', 'information': '0', 'commander': '1', 'fourni': '1', 'ailleurs': '0', 'doute': '-0.5', 'affich': '0.5', 'capacité': '1', 'maximum': '1', 'tenir': '0', 'journée': '0', 'cdt': '1', 'mal': '-1', 'petit': '-1','décharger':-1,'défaillant' : -1,'fille' : 1,'ravir' : 1,'problème':-1 ,'bon':1.5,'impeccable': '1', 'trouver': '0.5', 'vraiment': '2', 'très': '2', 'bien': '2', 'reconditionné': '0', 'fonctionner': '1', 'juste': '0', 'manqu': '-0.6', 'accessoire': '1', 'prise': '1', 'super': '2', 'dire': '0', 'tester': '1', 'premier': '1', 'reconditionner': '0', '13': '0', '…': '1.4', 'choisir': '0', 'bon': '2', 'final': '0', 'il': '0', 'tout': '0', 'compétitif': '1', '!': '2','commande': 0.7,'rapide' : 0.7,'livraison': 0.8,'aucune' : -0.8,'aucun':-0.8,'rayure':-0.9,'perdre': '-0.9', 'plus': '1.4', 'de': '0', '20': '0', 'pourcent': '0', 'ne': '-2', 'parler': '0', 'même': '0', '...': '1.4', 'Déçu': '-1', 'content': '1', 'achat': '0.8', 'aller': '0', '93': '0', 'déçu': '-1', 'le': '0', 'mettre': '0', 'charge': '0.8', 'temps': '0', 'monter': '0','présent': '0', 'site': '0', 'iphon': '1', 'luire': '0.7', 'meme': '0', 'parfaire': '0.9', 'etat': '0.9', 'neuf': '0.9', 'batterie': '1', '100': '1', 'chargeur': '1', 'cabl': '1', 'seul': '0', 'recevoir': '0', 'souci': '-0.8', 'bout': '0', 'se': '0', 'décoller': '-0.9', ',': '0','gros': '1.3', 'j’': '0', 'avoir': '0', 'devoir': '-0.3', 'remplacer': '-0.7', 'et': '0', 'modèle': '0.5', 'importer': '0', 'état': '0.8', 'qui': '0', 'n’': '-1', 'donc': '0', 'pas': '-2', 'ce': '0','Conforme': '0.7', '.': '0', 'voir': '0', 'utilisation': '0.6', 'produire': '0', 'non': '-1', 'conforme': '0.7', 'description': '0',"excellent": 1,"decharger":-0.8,"recommander": 0.8,"bémol": -0.7 ,"telephone" : 1,'produit' :0.7,'iphone' : 1, "mobile" :0.8 ,"Apple" :1,"écran" :1,"iOS" : 1,"application" :0.5,"Siri":1,"smartphone" :0.5,"écouteur" :0.5,"App Store" :0.7 ,"Steve Jobs" :1,"mobile" :1 ,"téléphone" :1 ,"iTunes" : 0.6, "capteur" : 0.6,"compatible" : 0.6, "télécharger" :0.7,"USB" :0.5,"Android" :-1,"appareil" :0.8,"Samsung" : -1,"Wi-Fi" :0.7,"FaceTime" : 0.7 ,"appli" : 0.7 , "camera" : 0.8, "surchauffe" : -1,"admirer" :1,"adorer" : 1,"affectionner" : 0.7,"apprécier" : 0.8, "aimer" :0.9,"detester": -1,"degouter":-1,"demeurer" : 0, "devenir" : 0, "être" :0, "sembler" : 0, "paraître": 0, "reste" :0,"fuir":-0.9}

# Note : Le lexique ci-dessus est un exemple simplifié. Il doit être enrichi pour une utilisation réelle.
def analyse(phrase):
    """
    Analyse syntaxique et sémantique d’une phrase pour calculer un score de sentiment.
    Retourne : 'positif', 'neutre' ou 'négatif'.
    """
    nlp = spacy.load("fr_core_news_sm")
    doc = nlp(phrase)
    score = 0
    i = 0

    for token in doc:
        if token.dep_ not in ["det"]:  # Ignore les déterminants
            lemma = token.lemma_
            if lemma in produit_lexique and float(produit_lexique[lemma]) != 0:
                score += float(produit_lexique[lemma])
                i += 1

                head_lemma = token.head.lemma_
                if head_lemma in produit_lexique and head_lemma != lemma and float(produit_lexique[head_lemma]) != 0:
                    i += 1
                    score += float(produit_lexique[lemma]) * float(produit_lexique[head_lemma])

    score = score / (i + 1)

    if score > 0.3:
        return "positif"
    elif score < 0.1:
        return "négatif"
    else:
        return "neutre"

def etiquette(avis_list):
    """
    Étiquette une liste de textes d’avis avec l’analyse de sentiment.
    """
    return [analyse(texte) for texte in avis_list]

def test(fichier):
    """
    Teste l’étiquetage automatique sur un fichier JSON d’avis
    et affiche la précision et le rapport de classification.
    """
    with open(fichier, mode='r', encoding='utf-8') as file:
        data_test = json.load(file)

    # Conversion des clés en entiers si nécessaire
    data_test = {int(key): value for key, value in data_test.items()}

    # Sélection de sous-ensembles d’avis pour tester (à adapter)
    x_test = [content["text_avis"] for content in list(data_test.values())[0:40]]
    y_test = [content["label"] for content in list(data_test.values())[0:40]]

    # Prédiction
    y_pred = etiquette(x_test)

    # Résultats
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

    erreurs = sum(1 for i in range(len(y_pred)) if y_pred[i] != y_test[i])
    print(f"{erreurs} erreurs sur {len(y_pred)} avis")

# Lancer un test sur fichier JSON quelconque.
#test("Sentimental_analysis/Iphone/scrapping_iphone/AVIS TXT/avis_validation.txt")
#print(analyse("Bonjour, je suis très satisfait de mon nouvel iPhone !"))
