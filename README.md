# EI-1-WEB-DATA

Sentimental analysis

Summary : 
I. Sentimental analysis twitter
II. Product satisfaction (iphone)
 
---------------------------------------------------------------

I. Sentimental analysis twitter
    Etiquetage : Trois méthodes différentes ont été utilisées afin de réaliser l'étiquetage
        - à la main selon des règles établies en prenant en compte la base de données
        - avec l'algorithme Stanford
        - avec VADER



        Stanford : 
        Ce script Python permet d'effectuer [préciser la fonctionnalité principale du fichier]. Il utilise plusieurs bibliothèques populaires pour manipuler et analyser les données, tout en offrant des fonctionnalités telles que [préciser des fonctionnalités spécifiques].
        Avant d'exécuter ce script, il est nécessaire d'installer les bibliothèques suivantes :

        pip install numpy pandas matplotlib scipy scikit-learn
        pip install stanfordcorenlp
        pip install langdetect



        VADER :
       



    Apprentissage : 

    Nous avons eu recours à trois algorithmes différents pour réaliser l'aprentissage et la sentimental analysis. 

    Random Forest

    NaiveBayes :
        - naivebayes.py :
        Ce script Python effectue une analyse de sentiment sur des tweets ou des textes en utilisant un modèle de classification basé sur la méthode Naive Bayes. Le pipeline scikit-learn se compose des étapes suivantes :
        1. Nettoyage du texte: Suppression des URLs, mentions, hashtags, ponctuation et chiffres.
        2. Vectorisation TF-IDF : Transformation des textes en vecteurs numériques.
        3. Classification : Utilisation de la méthode Naive Bayes pour prédire l'étiquette (positif, négatif, neutre).
        Le modèle est formé à partir d'un jeu de données étiqueté et testé sur un autre jeu de données pour évaluer sa précision.

        Avant d'exécuter ce script, il est nécessaire d'installer les bibliothèques suivantes : pip install pandas scikit-learn stop-words


    SVC : 
        - svc.py : 
        Ce script Python effectue une analyse de sentiment sur des tweets ou des textes en utilisant un modèle de classification basé sur la méthode **LinearSVC** (Support Vector Classification). Le pipeline scikit-learn se compose des étapes suivantes :

        1. Chargement des données : Chargement des données d'entraînement (`data70_etiq.txt`) et de test (`data10_etiq.txt`) depuis des fichiers JSON.
        2. Vectorisation TF-IDF : Transformation des textes en vecteurs numériques en utilisant `TfidfVectorizer`.
        3. Entraînement du modèle : Utilisation de **LinearSVC** pour entraîner un modèle sur les données d'entraînement vectorisées.
        4. Évaluation du modèle : Prédiction des sentiments sur les données de test, calcul de l'accuracy, et génération d'un rapport de classification avec la matrice de confusion.
        5. Sauvegarde du modèle : Le modèle entraîné est sauvegardé sous forme de fichier `.joblib` pour une utilisation future.

        Avant d'exécuter ce script, il est nécessaire d'installer les bibliothèques suivantes : pip install pandas scikit-learn joblib




    GridSearch


II. Product satisfaction (iphone)

    Scrapping : 
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
