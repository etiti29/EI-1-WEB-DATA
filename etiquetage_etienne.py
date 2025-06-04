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
    
produit_lexique={'latéral': '0', 'Bonjour': '0', 'air': '0', 'dommage': '-1', 'préciser': '0.4', 'récupérable': '0.3', 'avai': '0', 'en': '0', 'fonctionnement': '1', 'physique': '0', 'boite': '0.4', 'blister': '0.5', 'également': '0', 'pré-installé': '0.5', 'attention': '-1', 'livrer': '0.7', 'posséder': '0.4', 'e-sim': '1', 'part': '0', 'hésiter': '-0.3', 'aussi': '0', 'casser': '-1', 'facilement': '1', 'mais': '0', 'sinon': '0.5', 'ensemble': '0', 'signaler': '-0.7', 'tel': '1', 'réellement': '1', 'croire': '1', 'choquer': '1', 'satisfait': '1', 'colis': '0.5', '24h': '0', 'délaisser': '-0.6', 'moi': '0', 'y': '0', 'vous': '0', 'regretter': '-0.8', ';': '0', '-).produit': '0', 'reconditionnement': '0.5','reconnaître': '0.4', 'inconnue': '-0.4', 'absolument': '2', 'escro': '-2', '.vendeur': '0.4', 'sérieux': '1', 'envoyer': '1', 'J’': '0', 'peur': '-1', 'avis': '1', 'c': '0', 'top': '2', 'convenable': '0.5', 'cependant': '-0.5', 'payer': '0.4', 'expresse': '1', 'cela': '0', 'chauffe': '-1', 'beaucoup': '2', 'décollage': '-1', 'eter': '0', 'trop': '2', 'cher': '-1', 'contre': '-0.3', 'haut': '0', 'focntionne': '1', 'parleur': '1', 'deception': '-1', 'nouveau': '1', 'tarvail': '0', 'realiser': '0.3', 'reconditionneur': '0.3', 'photo': '1', 'mise': '0', 'cm': '0', 'objet': '0', 'impossible': '-1', 'prendre': '0.5', 'exemple': '0', 'fleur': '0', 'document': '0.4', 'etc.': '-0.3', 'surtout': '2', 'vidéo': '1', 'instant': '0.8', 'manquer': '-0.7','prix': '1', 'coque': '1', 'vitre': '1', 'protection': '1', 'verre': '1', 'trempé': '1', 'original': '1', 'aurai': '0', 'venir': '0.5', 'fortement': '2', 'vendeur': '1', 'équipe': '1', 'adaptateur': '1', 'm’': '0', 'donner': '1', 'fil': '1', 'abordable': '1', 'je': '0', 'utiliser': '1', 'coqu': '1', 'arrière': '1', 'parfaitement': '2', 'moins': '-1', 'jour': '0', 'semaine': '0', 'charger': '1', '10h': '0', 'rien': '-0.5', 'niquel': '2','déçue': '-1', 'l’': '0', 'acheter': '0', 'janvier': '0', '..': '0', '25': '0', 'déjà': '0', 'savoir': '0', 'correctement': '1', 'boîte': '1', 'câbl': '1', 'SMARTPHONE': '1', 'RECONDITIONNER': '1', 'SATISFAIT': '1', 'arriver': '1', 'vie': '0.3', 'merci': '1', 'encore': '-0.5', '.le': '0', 'envoi': '0.5', 'pouvoir': '0.5', 'me': '0', 'prononcer': '0', 'durabilité': '1', 'rapport': '1', 'meilleur': '2', 'trace': '-1', 'd’': '0', 'usur': '-1', 'emballer': '1', 'protéger': '1', 'offerte': '2', 'nickel': '2', 's’': '0', 'utilis': '1', 'un': '0', 'peu': '0.3', 'vite': '1', 'penser': '1', 'normal': '0.4', 'que': '0', 'c’': '0', 'mini': '0.6', 'niveau': '0.6', 'vivement': '0.9', '.iphone': '1', 'rapidement': '1', 'propre': '1', 'paramètre': '1', 'oled': '1', '(': '0', 'origin': '1', 'vue': '0', 'qualité': '1', ')': '0', 'mieux': '2', 'quoi': '-1', 'foncer': '2', 'oeil': '0', 'fermer': '0', 'faire': '1', 'update': '1', 'mois': '0', 'suivre': '0', 'moment': '0','mèr': '1', 'h': '0', '?': '1', 'bonjour': '0', 'information': '0', 'commander': '1', 'fourni': '1', 'ailleurs': '0', 'doute': '-0.5', 'affich': '0.5', 'capacité': '1', 'maximum': '1', 'tenir': '0', 'journée': '0', 'cdt': '1', 'mal': '-1', 'petit': '-1','décharger':-1,'défaillant' : -1,'fille' : 1,'ravir' : 1,'problème':-1 ,'bon':1.5,'impeccable': '1', 'trouver': '0.5', 'vraiment': '2', 'très': '2', 'bien': '2', 'reconditionné': '0', 'fonctionner': '1', 'juste': '0', 'manqu': '-0.6', 'accessoire': '1', 'prise': '1', 'super': '2', 'dire': '0', 'tester': '1', 'premier': '1', 'reconditionner': '0', '13': '0', '…': '-0.4', 'choisir': '0', 'bon': '2', 'final': '0.2', 'il': '0', 'tout': '0', 'compétitif': '1', '!': '2','commande': 0.7,'rapide' : 0.7,'livraison': 0.8,'aucune' : -0.8,'aucun':-0.8,'rayure':-0.9,'perdre': '-0.9', 'plus': '0.2', 'de': '0', '20': '0', 'pourcent': '0', 'ne': '-1', 'parler': '0', 'même': '0', '...': '-0.3', 'Déçu': '-1', 'content': '1', 'achat': '0.8', 'aller': '0', '93': '0', 'déçu': '-1', 'le': '0', 'mettre': '0', 'charge': '0.8', 'temps': '0', 'monter': '0','présent': '0.2', 'site': '0.2', 'iphon': '1', 'luire': '0.7', 'meme': '0', 'parfaire': '0.9', 'etat': '0.9', 'neuf': '0.9', 'batterie': '1', '100': '0', 'chargeur': '1', 'cabl': '1', 'seul': '0.2', 'recevoir': '0.3', 'souci': '-0.8', 'bout': '0', 'se': '0', 'décoller': '-0.9', ',': '0','gros': '0.4', 'j’': '0', 'avoir': '0.5', 'devoir': '-0.3', 'remplacer': '-0.7', 'et': '0', 'modèle': '0.4', 'importer': '0.4', 'état': '0.8', 'qui': '0', 'n’': '-1', 'donc': '0', 'pas': '-1', 'ce': '0','Conforme': '0.5', '.': '0', 'voir': '0.3', 'utilisation': '0.6', 'produire': '0.5', 'non': '-1', 'conforme': '0.5', 'description': '0.6',"excellent": 1,"decharger":-0.8,"recommander": 0.8,"bémol": -0.5 ,"telephone" : 1,'produit' :0.7,'iphone' : 1, "mobile" :0.8 ,"Apple" :1,"écran" :1,"iOS" : 1,"application" :0.5,"Siri":1,"smartphone" :0.5,"écouteur" :0.2,"App Store" :0.7 ,"Steve Jobs" :1,"mobile" :0.5 ,"téléphone" :0.5 ,"iTunes" : 0.6, "capteur" : 0.6,"compatible" : 0.6, "télécharger" :0.4,"USB" :0.3,"Android" :-1,"appareil" :0.3,"Samsung" : -1,"Wi-Fi" :0.5,"FaceTime" : 0.5 ,"appli" : 0.3 , "camera" : 0.8, "surchauffe" : -1,"admirer" :1,"adorer" : 1,"affectionner" : 0.7,"apprécier" : 0.6, "aimer" :0.9,"detester": -1,"degouter":-1,"demeurer" : 0.5, "devenir" : 0.5, "être" : 0.5, "sembler" : 0.4, "paraître": 0.4, "reste" :0.4,"fuir":-0.9}
def analyse(phrase):
    nlp = spacy.load("fr_core_news_sm")
    doc = nlp(phrase)
    score=0
    i=0
    for token in doc :
        if token.dep_ not in ["det"]:
            if token.lemma_ in produit_lexique :  
                score+=float(produit_lexique[token.lemma_])
                i+=1
                if token.head.lemma_ in produit_lexique and token.head.lemma != token.lemma : 
                    print(token.lemma_,token.head.lemma_)
                    i+=1
                    score+=float(produit_lexique[token.lemma_])*float(produit_lexique[token.head.lemma_])
                    if token.head.head.lemma_ in produit_lexique and token.head.head.lemma != token.head.lemma : 
                        print(token.lemma_,token.head.lemma_,token.head.head.lemma_)
                        i+=1
                        score+=float(produit_lexique[token.lemma_])*float(produit_lexique[token.head.lemma_])*float(produit_lexique[token.head.head.lemma_])
    score=score/i
    print(score)
    if score >0.3 :
        print("positif")
    elif score <-0.3 :
        print("négatif")
    else : 
        print("neutre")
    

                

analyse("Très heureuse cet achat. Iphone en Excellent état, on dirait un neuf. Par contre , Come c'est une reconditionné, je ne sais pas s'il résiste à l'eau... Si quelqu'un peut m'orienter sur cette question ?")
print(len(produit_lexique.keys()))

data="Bonjour au bout de 1 mois le bouton latéral ne fonctionne plus.Bonjour, Le téléphone il a l’air tout neuf. J’ai même reçu une coque de protection Et un chargeur rapide Avec 100% de batterie. Pour le moment tout va bien Je ferais un update de l’utilisation du téléphone. Dommage je n’ai pas pris en photo le téléphone quand je l’ai reçu.Il fonctionne super bien.Vous devriez préciser que la TVA n'est pas récupérable, si je l'avais su, je ne l'aurais pas acheté...J’ai reçu mon iPhone 13 en super état avec une coque et un écran de protection, batterie à 100 %, il est vraiment comme neuf. Merci à Hassen.iPhone 13 mini en parfait état (fonctionnement et physique après vérification). Fourni dans une boite en carton sous blister avec tous ses accessoires. Fourni également avec une coque + protège écran pré-installé. Attention, le modèle livré ne possède pas de E-SIM pour ma part, ce qui est un peu dommage. Je recommande ce vendeur sans hésiter !!.Le batterie se décharge très rapidement. Aussi le téléphone se casse très facilement mais sinon dans l’ensemble ça va.Rien à signaler… ça fonctionne très bien ?Tel reçu dans les temps, 100% de batterie, très bon Vendeur je recommande.Réellement On croirait qu’il est neuf très Bien reconditionné, je suis choqué Très satisfaite.Je recommande, envoi rapide, le téléphone est propre, batterie 100% et petit plus une coque en cadeau.Batterie à 100%, on verra bien avec le temps. Pas une seule rayure il est nickel !Merci au vendeur, très content de mon achat colis reçu en 24h le téléphone est impeccable , pas une rayures batterie a 100% merci pour la coque de protection offerte . je recommande sans hésiter ce vendeur. Pour ce qui hésite a délaisser leur iPhone gros iPhone XR comme moi pour ce modèle , un conseil allez y vous aller pas regretter ;-).produit conforme de très bon reconditionnement."
'''51,au vue des témoignages j'étais un peu septique mais avec une grande surprise le téléphone est nickel je vous l'assure,5,3
52,C’est un très bon téléphone.le prix est très bas par rapport au performance proposé je recommande,4,3
53,"Le téléphone est fonctionner très bien et la batterie est à 100 pour 100, la livraison ça été très rapide je suis satisfait merci.",5,3
54,"Très heureuse cet achat. Iphone en Excellent état, on dirait un neuf. Par contre , Come c'est une reconditionné, je ne sais pas s'il résiste à l'eau... Si quelqu'un peut m'orienter sur cette question ?",5,3
55,"Iphone mini 13 même dimension que le 8. Acheter pour ma fille j'avais déjà commandé le 11 y a 2ans sur cdiscount on était ravie dû coup j'ai repris le 13 pour son anniv. Ça l'a change comme il est plus petit que le 11, mais à + d'option c'est le but. Je recommande, arrivé en 3jrs.",5,3
56,Iphone en très bon état ...fonctionne très bien :,5,3
57,Je recommande sans hésitations . Le produit est conforme au descriptif Très bon vendeur et livraison rapide,5,3
58,Je recommande ce vendeur pour son sérieux et son professionnalisme.,5,3
59,"Cette iphone est très intéressant car on peut le tenir a seulement une main pour écrire un message par exemple,et en plus il est tout aussi performant qu'un iphone 13. Le seul point négatif est la taille de l'écran.",4,3
60,Un peu petit selon ma petite fille....,5,3
61,Je l’ai reçu très rapidement merci Cdiscount je le recommande fortement aucune rayure batterie à 100% pour un reconditionné je suis très agréablement surprise de la qualité comme neuf n’hésitez pas,5,3
62,iPhone 13 mini minuit au top RAS. J’ai commandé le même coloris PINK au même vendeur. Très satisfaite de ce vendeur.,5,3
63,La capacité de batterie ne tient pas du tout sa fait 3 mois que je les acheter et elle et déjà à 83% de capacité.,2,1
64,"Coque, protection écran déjà installé sur le produit, chargeur et câble fourni. Emballé comme neuf. Etat batterie 100% parfait",5,3
65,Au top comme neuf fonctionne bien,5,3
66,Parfait très bon vendeur,4,3
67,"à fuir ! Livraison longue, appareil non conforme ... pas besoin de m'étendre plus",1,1
68,Iphone 13 mini C'est vraiment un bijou,5,3
69,"Le produit semble fonctionner parfaitement. La batterie ne donne pas de signe de faiblesse pour le moment. Produit très propre, fourni avec un coque et une protection écran. Compte tenu du prix, sensiblement inférieur aux autres vendeurs, je ne peux que recommander CDISCOUNT pour ce type d'achat. Patrick CARON",4,3
70,Super comme NEUF.?????,5,3
71,"moi qui en attendaismieux de ce produit, il n'auras pas durer longtemps, il est déjà HS. je ne recommande pas du tout",1,1
72,"Téléphone acheté le 29/06/2024, 3 semaines plus tard suite à une chute la vitre arrière est complètement brisée et l'écran présente un trait blanc (téléphone protégé par une coque Rhinoshield ainsi qu'un vers trempé Rhinoshield), le téléphone reste utilisable. Je décide cependant de le faire réparer. après le changement de l'écran et de la vitre arrière, le téléphone chauffe anormalement. Le problème a été résolu grâce au retrait du capteur d'empreinte digital, cependant le téléphone s'allume mais s'éteint tout seul... Verdict un composant dans la carte mère était hs donc trop coûteux à réparer... Le réparateur m'a affirmé que le téléphone avait déjà subis pas mal de réparations.. Je suis d'accord pour accorder une seconde vie aux téléphone mais à ce prix là et vu le nombre d'anomalies depuis l'achat c'est de l'arnaque. Je ne suis pas du genre à critiquer à tout va, mon commentaire servira à prévenir les futures clients",1,1
73,L'iphone est comme neuf (pas de fissure...),5,3
74,Petit téléphone sympa . Bien arrivé et en super état tout fonctionnel. Un téléphone qui se glisse facilement dans les poches . Le chargeur n'est pas fourni juste le câble dommage. Conforme à l'annonce de vente. Batterie à 100 %. Que du bon .,5,3
75,aucune rayure 100% de batterie et livraison rapide merci,5,3
76,La commande est arrivée rapidement en bonne état. L'iPhone est en parfait état avec une batterie de capacité maximale de 88%. Il est fourni avec une câble USB.,5,3
77,ESCROC FUYEZ TRES VITE,1,1
78,"Oui très bien très bien, l’utiliser le iPhone 13 mini",4,3
79,Parfait petit comme j’aime,5,3
80,"Le téléphone est arrivé dans un état quasi neuf, aucune fissure ou trace de choc. Je l'ai reçu dans les temps. Le niveau de charge maximum de la batterie est à 85%, ce qui est très satisfaisant pour un reconditionné. Vu le prix bas, j'avais peur d'être déçue mais c'est une expérience d'achat très positive pour moi, je recommande !",5,3
81,"Le téléphone a une soucis de micro ,j'ai envoyé un mail sans suite",1,1
82,"Je suis ravie de mon achat, le téléphone est comme neuf, il est en parfait état. Il est tout à fait conforme à sa description sur le site internet Cdiscount. Livraison très rapide, je recommande !",5,3
83,Satisfait de l’iphone 13,5,3
84,"Rien à redire, je fais rarement d’avis mais c’est un très bon produit sans marque d’usure",5,3
85,Réception dans les temps. Produit parfaitement conforme à mes attentes et à la description.,5,3
86,Reçu rapidement et en état parfait. content de mon achat,5,3
87,Mon petit-fils est satisfait,4,3
88,Très bonne achat reçu très rapidement rien à dire pour le moment mon fils est content et juste Un câble mais pas le chargeur... Pour le moment rien à redire..,5,3
89,"Livraison rapide,conforme à la commande état neuf avec une batterie à 100%. Livré avec chargeur et verre trempé. Je recommande",5,3
90,Il est très bien petit et pour le prix nickel fait son job aucune rayure et état de la batterie top 98,5,3
91,Envoi rapide et tel bien protégé Juste un petit éclat sur le tour du téléphone donc presque parfait ?,4,3
92,"Un peu déçu de ce téléphone, l’état de la batterie étant de 87% et avec peu d’accessoires, un simple câble de chargeur et même pas de clé pour insérer la carte SIM. A par ce le téléphone marche nickel pour l’instant.",3,2
93,"Je suis ravie ! la taille de ce smartphone est parfaite ! Elle me rappelle celle du 4S. Les fonctionnalités ne changent pas d'un Iphone à l'autre mais celui-ci compte tenu de sa taille, c'est un bijou de technologie. Je le recommande vraiment pour ceux qui seraient à la recherche un téléphone à taille raisonnable. Dommage qu'Apple n'ait pas continué à sortir des modèles de cette taille. Suis anti Apple mais fan absolue de ce modèle. L'appareil photo en revanche rame un peu pour ce qui est de la mise au point de l'objectif ... Sinon, la batterie tient la journée (je ne passe pas ma vie au téléphone ou sur les réseaux sociaux ou encore sur les applications). J'avais un androïd avant celui-ci et c'est précisément la taille qui m'a fait faire ce choix ! seul point noir dans l'histoire c'est le transfert des données d'androïd vers Iphone ! depuis la nuit des temps des mobiles, cette étape est un vrai casse-tête ! j'ai du transférer les données une à une ... idem le jour où je devrais repasser sur androïd ... Je recommande ce modèle sans hésiter !",5,3
94,"Choisir l'iPhone 13 Mini en couleur minuit, c'est opter pour l'élégance et la sophistication à portée de main. Avec sa taille compacte et son design raffiné, cet iPhone incarne la puissance et la beauté dans un format parfaitement adapté à votre style de vie dynamique. Plongez dans un monde de performances exceptionnelles, d'innovation technologique et de possibilités infinies avec l'iPhone 13 Mini.",5,3
95,J’ai reçu ce téléphone ce matin est je ne suis pas déçu de cette achats incroyables la batterie neuf aucun défaut je vous le conseille fort,5,3
96,"Très bien emballé, batterie 100%, reçu rapidement, très satisfait de mon achat même au bout trois mois .... Je recommande",5,3
97,"Livraison rapide bien protégé, téléphone comme neuf très satisfaite de mon achat",5,3
98,"Portable qui a fonctionné que 15 jours, qualité pas au rendez vous.",1,1
99,"Téléphone trop fragile, cassé au bout d’un mois d’utilisation, reçu qu’avec cable chargeur.",1,1
100,Envoi rapide; état impeccable; batterie 95%,4,3
101,Téléphone propre et conforme,5,3
102,jetait hésitant a acheter du reconditionné mais franchement j’ai était très agréablement surpris le téléphone est arriver en moins d’une semaine avec l’état de la batterie a 100% une vitre de protection et un chargeur avec une prise secteur très très satisfait de mon achat surtout pour ce prix la,5,3
103,Contente de mon achat,4,3
104,"Je suis tellement content, le téléphone est complètement neuf ! Aucune rayure, fonctionne parfaitement avec une batterie à 100% ! pour le prix c est cadeau! merci beaucoup",5,3
105,"Mise en fonction simple et didactique.Transfert de données impeccable. Bémol sur la batterie qui semble ne pas bien tenir la charge. En résumé, plutôt bien.",4,3
106,"Le téléphone est arrivé très bien emballe, chargeur et câble fourni avec en plus un verre trempé, l'écran possédait le film de protection d'origine et le téléphone n'avait aucune rayure c'est incroyable, la batterie était a 100% tout est d'origine JE RECOMMANDE !!!!!!!!!",5,3
107,Très bien…………………………………………,5,3
108,"C'est littéralement le premier iphone que j’achète en reconditionné donc j'avais un peur de la qualité mais quand je l'ai recu il était vrmt comme neuf. À ce prix-là, c'est une affaire. Encore merci !",5,3
109,"Livraison dans les temps, batterie à 100 %. le seul petit truc qui manque, c'est les protections. Sinon totalement satisfait.",5,3
110,"Bonjour téléphone reçu, en parfaite état bien emballé et rapidement ce pendant c’est bien dommage le support de chargeur n’est pas fournis….. je recommande",4,3
111,"Parfait (boîte de présentation bof, cable bof mais Ce n’est pas le principal). Le tel nickel ?",5,3
112,Super arrivé vite en très bon état aucune rayure La batterie est à 90% sa peut aller et sinon tout est niquel mais le téléphone n’a pas de protection dommage,5,3
113,Aujourd'hui je suis Très satisfait par ce produit par la description apporté sur sa qualité de fonctionnement par sa qualité visuelle quasiment neuf si il n'était pas mentionné que ce produit et reconditionné rien ne le montre je ne peux que recommander ce produit et le professionnalisme apporté par le vendeur THL- Electronic Technology shop,5,3
114,"Très bon produit , comme neuf. Il manque le chargeur, très regrettable pour le prix.",5,3
115,"Bien reçu, la batterie a 86% un peut dommage pour le prix , le câble du chargeur m’a lâché au bout de 2j , sinon dans l ensemble satisfait aucune rayure visible juste vraiment dommage pour la batterie",4,3
116,Au top ? envoie soigner rapide,5,3
117,"Reçu le lendemain après avoir passé la commande, batterie à 100%, état impeccable et fonctionnel de suite. Petit bémol, il n’y a que le câble de charge et non la prise .. Sinon c’est absolument parfait!",5,3
118,"Très satisfait , en excellent état , etat batterie 100% , juste manque bloc chargeur .",5,3
119,"Très satisfait de mon achat, aucun défaut sur le téléphone, batterie à 100%, l’emballage du téléphone par contre n’est pas top mais il est arrivé intact. Je recommande fortement !",5,3
120,Envoi ultra rapide et colis conforme.,5,3'''


def apprentissage(data):
    d={}
    nlp = spacy.load("fr_core_news_sm")
    doc = nlp(data)
    for token in doc:
        if not token.lemma_ in produit_lexique and type(token.text) != "int" and token.dep_ not in ['det','mark','case','nmod','dep','nsubj','cc','nummod']: 
            print(token.dep_)
            d[token.lemma_]=input(token.lemma_)
    print(d)
#apprentissage(data)
