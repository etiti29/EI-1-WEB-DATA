import csv
import json

def csv_to_json_txt(input_csv_path, output_txt_path):
    """
    Convertit un fichier CSV d'avis (avec colonnes id, text_avis, note, label)
    en un fichier .txt contenant un dictionnaire JSON structuré par ID.
    """
    avis_dict = {}

    with open(input_csv_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            id_str = row["id"].strip()
            avis_dict[id_str] = {
                "text_avis": row["text_avis"].strip(),
                "label": row["label"].strip()
            }

    with open(output_txt_path, mode='w', encoding='utf-8') as txtfile:
        json.dump(avis_dict, txtfile, ensure_ascii=False, indent=2)

    print(f"[✓] Fichier .txt généré dans : {output_txt_path}")
    
    
csv_to_json_txt ("avis_validation.csv","avis_validation.txt")
