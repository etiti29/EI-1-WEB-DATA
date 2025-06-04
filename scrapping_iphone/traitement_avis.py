import os
import pandas as pd

# Dossier contenant les fichiers à concaténer
DOSSIER_CSV = r"C:\Users\sarae\Desktop\ST4 - EI\EI-1-WEB-DATA\scrapping_iphone\avis_csv"

# Récupération des fichiers .csv
fichiers_csv = [f for f in os.listdir(DOSSIER_CSV) if f.endswith(".csv")]
liste_df = []

for fichier in fichiers_csv:
    chemin = os.path.join(DOSSIER_CSV, fichier)
    try:
        df = pd.read_csv(chemin, sep=",", quoting=1, encoding="utf-8", header=None,
                         names=["id", "text_avis", "note", "label"])
        liste_df.append(df[["text_avis", "note", "label"]])  # on ne garde pas l'ancien id
    except Exception as e:
        print(f" Erreur dans {fichier} : {e}")

# Si aucun fichier valide trouvé
if not liste_df:
    print(" Aucun fichier n’a pu être chargé.")
    exit()

# Concaténation et nouvel ID
df_concatene = pd.concat(liste_df, ignore_index=True)
df_concatene.insert(0, 'id', range(len(df_concatene)))

# Sauvegarde
fichier_final = os.path.join(DOSSIER_CSV, "avis_concatenes.csv")
df_concatene.to_csv(fichier_final, index=False)

print(f"✅ {len(df_concatene)} avis concaténés avec succès dans : {fichier_final}")

