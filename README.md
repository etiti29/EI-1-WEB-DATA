# EI-1-WEB-DATA

Sentimental analysis

Summary : 
I. Sentimental analysis twitter
II. Product satisfaction (iphone)
III. Informations supplémentaires
 
---------------------------------------------------------------
Faire cd EI_1_WEB_DATA avant de run les codes. 

I. Sentimental analysis twitter
    Etiquetage : Deux méthodes différentes ont été utilisées afin de réaliser l'étiquetage
        - à la main selon des règles établies en prenant en compte la base de données
        - avec l'algorithme Stanford
    

        A la main : 
        Deux algorithmes se trouvant dans Twitter/etiquetage
        - etiquetagev1.py :
            Ce script effectue un étiquetage de sentiment manuel (positif, négatif, neutre) à partir d’un lexique français et de règles linguistiques (pondération grammaticale, détection de négation).
            Il prend en entrée un fichier .txt (JSON) contenant les tweets, et génère un fichier tweets_etiquetés.json avec les scores de sentiment.

            Bibliothèques requises
            pip install spacy
            python -m spacy download fr_core_news_sm

        - etiquetage_en.py : 
            sentiment_en_vader.py permet de réaliser un étiquetage automatique de sentiments sur des textes en anglais à l’aide de VADER et spaCy, avec pondération grammaticale et gestion de la négation. À lancer avec :
            python sentiment_en_vader.py (nécessite un fichier JSON .txt en entrée).





        Stanford : 

        Le modèle Stanford CoreNLP utilise une analyse linguistique classique basée sur des règles et des arbres syntaxiques pour extraire le sentiment des textes.

        Il faut installer le package sur le lien https://stanfordnlp.github.io/CoreNLP/download.html puis télécharger le modèle français pour pouvoir gérer à la fois les textes en abglais et en français.
        
        Avant d'exécuter ce script, il est nécessaire d'installer les bibliothèques suivantes :

        pip install numpy pandas matplotlib scipy scikit-learn
        pip install stanfordcorenlp
        pip install langdetect
     



    Apprentissage : 

    Nous avons eu recours à trois algorithmes différents pour réaliser l'aprentissage et la sentimental analysis. 

    Random Forest :
        - random_forest.py (Sentimental_analysis\apprentissage\RandomForest\random_forest.py)
        1. Pour fit le modèle unhashtaguer ligne 84 et préciser le nom du fichier d'entrainement ligne 7.
        2. Pour tester le modele unhashtaguer ligne 85 et préciser le nom du fichier de validation
        3. pour tester vous même le modele sur un exemple unhashtaguer ligne 91 à 93 et préciser dans la variable tweet votre exemple 

        Avant d'exécuter ce script, il est nécessaire d'installer les bibliothèques suivantes : pip install numpy pandas scikit-learn joblib



    NaiveBayes :
        - naivebayes.py (Sentimental_analysis\apprentissage\NaiveBayes\naivebayes.py):
        Ce script Python effectue une analyse de sentiment sur des tweets ou des textes en utilisant un modèle de classification basé sur la méthode Naive Bayes. Le pipeline scikit-learn se compose des étapes suivantes :
        1. Nettoyage du texte: Suppression des URLs, mentions, hashtags, ponctuation et chiffres.
        2. Vectorisation TF-IDF : Transformation des textes en vecteurs numériques.
        3. Classification : Utilisation de la méthode Naive Bayes pour prédire l'étiquette (positif, négatif, neutre).
        Le modèle est formé à partir d'un jeu de données étiqueté et testé sur un autre jeu de données pour évaluer sa précision.

        Avant d'exécuter ce script, il est nécessaire d'installer les bibliothèques suivantes : pip install pandas scikit-learn stop-words


    SVC : 
        - svc.py (Sentimental_analysis\apprentissage\RandomForest\GridSearchRF.py): 
        Ce script Python effectue une analyse de sentiment sur des tweets ou des textes en utilisant un modèle de classification basé sur la méthode SVC (Support Vector Classification). Le pipeline scikit-learn se compose des étapes suivantes :

        1. Chargement des données : Chargement des données d'entraînement (`data70_etiq.txt`) et de test (`data10_etiq.txt`) depuis des fichiers JSON.
        2. Vectorisation TF-IDF : Transformation des textes en vecteurs numériques en utilisant `TfidfVectorizer`.
        3. Entraînement du modèle : Utilisation de SVC pour entraîner un modèle sur les données d'entraînement vectorisées.
        4. Évaluation du modèle : Prédiction des sentiments sur les données de test, calcul de l'accuracy, et génération d'un rapport de classification avec la matrice de confusion.
        5. Sauvegarde du modèle : Le modèle entraîné est sauvegardé sous forme de fichier `.joblib` pour une utilisation future.

        Avant d'exécuter ce script, il est nécessaire d'installer les bibliothèques suivantes : pip install pandas scikit-learn joblib


    GridSearch : 
        L'outil GridSearch a été utilisé sur les trois algorithmes d'apprentissage afin de comparer les performances de ces derniers.
        - GridSearchRF.py (Sentimental_analysis\apprentissage\grid search\SVC\GridSearchSVC.py)
        - GridSearchNB.py (Sentimental_analysis\apprentissage\NaiveBayes\GridSearchNB.py)
        - GridSearchSVC.py (Sentimental_analysis\apprentissage\RandomForest\GridSearchRF.py)

        Fonctionnement :
        - Utilise GridSearchCV pour ajuster les hyperparamètres des modèles suivants :
            1. SVM (Support Vector Machine) : Optimisation des paramètres `C`, `kernel`, et `gamma`.
            2. Naive Bayes : Recherche des meilleurs paramètres pour la vectorisation TF-IDF et le classifieur MultinomialNB.
            3. Random Forest: Recherche des meilleurs hyperparamètres pour le classificateur RandomForestClassifier.
        - Chaque modèle est évalué sur un jeu de données de test pour déterminer l'accuracy, générer un rapport de classification et afficher la matrice de confusion.
        - Sauvegarde du meilleur modèle pour chaque algorithme sous forme de fichier `.joblib`.

        Avant d'exécuter ce script, il est nécessaire d'installer les bibliothèques suivantes : pip install pandas scikit-learn joblib stop-words numpy



II. Product satisfaction (iphone)

    Scrapping : 
        Se trouve dans la partie Iphone/scrapping_iphone
        - scrapping_Cdiscount.py :
        Ce script fonctionne correctement et permet d'extraire les avis clients d’une fiche produit Cdiscount. Il suffit d’exécuter le fichier (python scrapping_Cdiscount.py) après avoir ajouté l’URL du produit dans la variable URLS.
        Bibliothèques nécessaires :
        pip install selenium webdriver-manager

        - scrapping_backmarket.py :
        Ce script vise à extraire les avis de produits sur le site BackMarket, mais il est actuellement bloqué (à cause d’une protection anti-bot ou d’un changement de structure de page). Il s’exécute de la même manière : python scrapping_backmarket.py.

        - scrapping_fnac.py :
        Ce fichier est conçu pour collecter les avis depuis les pages produits de la Fnac, mais il ne fonctionne pas actuellement à cause d’un blocage côté site. L'exécution se fait avec python scrapping_fnac.py.

        - scrapping_rakuten.py :
        Le script tente de récupérer les avis publiés sur Rakuten, mais il est également bloqué. Il peut être lancé via la commande python scrapping_rakuten.py, une fois l’URL du produit renseignée.

        On obtient à chaque fois des fichier csv avec : un id, l'avis correspondant, le nombre d'étoiles et la classification. 
        
        Le fichier conversion_totxt.py permet de convertir un fichier CSV d’avis en un fichier .txt contenant le dictionnaire JSON attendu par le script etiquetage_iphone.py.
        Il se lance avec : python csv_to_json_txt.py  
        
        Le fichier traitement_avis.py permet de concaténer tous les fichiers d’avis collectés en un seul fichier CSV, tandis que division_avis.py permet ensuite de diviser ce fichier en trois ensembles : 10 % pour la validation, 20 % pour l’entraînement, et 70 % pour le test.
        Bibliothèque nécessaire :
        pip install pandas
        pip install pandas scikit-learn


    Etiquetage : 
        Sentimental_analysis\Iphone\etiquetage\etiquetage_iphone.py
         1. Test de l'algo d'etiquetage : unhashtaguer ligne 88 (le test ne se fait que sur 40 avis pour en selectionner plus cf ligne 74 et 75 en fin de ligne)
         2. Pour tester sur un avis en particulier unhashtaguer ligne 89 et mettez la phrase voulue en argument


III. Informations supplémentaires

    - Bin regroupe des fichiers sur lesquels nous avons travaillé et que nous avons préféré garder au cas ou un autre fichier venait à encourir un dysfonctionnement

    - LinearSVC_Model et SVM_Model regroupe les données d'apprentissage de svc.py et GridSearchSVC.py (les autres algorithmes d'apprentissage stockent également leur données mais directement dans leurs dossiers respectifs)