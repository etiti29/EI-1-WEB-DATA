import pandas as pd
from sklearn.model_selection import train_test_split

# Charger le fichier concaténé
df = pd.read_csv(r"C:\Users\sarae\Desktop\ST4 - EI\EI-1-WEB-DATA\scrapping_iphone\avis_csv\avis_concatenes.csv")  # mets ici le chemin vers ton fichier

# Mélange aléatoire
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# 1. Découpe 10% pour validation
df_val, df_temp = train_test_split(df, test_size=0.9, random_state=42)

# 2. Découpe les 90% restants en 20% entraînement et 70% test
# Pour obtenir 20% du total en entraînement, il faut faire un split 2:7 sur les 90%
df_train, df_test = train_test_split(df_temp, test_size=7/9, random_state=42)

# Vérification des tailles
print(f"Validation : {len(df_val)} échantillons")
print(f"Train      : {len(df_train)} échantillons")
print(f"Test       : {len(df_test)} échantillons")

# Sauvegarde
df_val.to_csv("avis_validation.csv", index=False)
df_train.to_csv("avis_train.csv", index=False)
df_test.to_csv("avis_test.csv", index=False)

print("✅ Fichiers enregistrés : avis_validation.csv, avis_train.csv, avis_test.csv")
