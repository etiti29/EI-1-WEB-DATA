# Importation des bibliothèques nécessaires
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time

# URL de la page produit à scraper (doit contenir les avis)
URL = "https://www.backmarket.fr/fr-fr/r/p/iphone-13-128-go-minuit-debloque-tout-operateur/ef5660d2-6883-4b81-b47d-86e5720687ef?order_by=-created_at"

# Limite maximale d'avis à récupérer
MAX_REVIEWS = 6000

# Fonction utilitaire pour faire défiler la page progressivement
def scroll_gradually(driver, steps=25, delay=0.6):
    for _ in range(steps):
        driver.execute_script("window.scrollBy(0, 300);")  # Scroll de 300px vers le bas
        time.sleep(delay)

# Fonction principale de scraping des avis
def scrape_backmarket_reviews(URL):
    # Initialisation du navigateur Chrome avec WebDriver Manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 20)  # Timeout pour les éléments dynamiques
    driver.get(URL)
    time.sleep(3)  # Laisse le temps à la page de charger

    avis_dict = {}       # Dictionnaire pour stocker les avis
    review_id = 0        # Compteur d'avis
    seen_texts = set()   # Pour éviter les doublons

    while True:
        # Scroll pour faire apparaître plus d’avis
        scroll_gradually(driver, steps=25, delay=0.6)

        # Attente jusqu’à ce que les avis soient visibles
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-qa="user-comment"]')))
        except:
            print("[!] Aucun avis visible.")
            break

        # Tente de cliquer sur le bouton "Charger plus d’avis"
        try:
            btn = driver.find_element(By.XPATH, "//span[contains(text(), 'Charger plus d’avis')]")
            driver.execute_script("arguments[0].scrollIntoView();", btn)
            time.sleep(1.2)
            btn.click()
            print("↻ Bouton cliqué pour charger plus d’avis...")
            time.sleep(3)
        except:
            print("[✓] Fin du chargement ou plus de bouton.")

        # Récupération des avis et des notes visibles
        comments = driver.find_elements(By.CSS_SELECTOR, "p.body-1.block.whitespace-pre-line")
        notes = driver.find_elements(By.XPATH, "//div[@aria-label][contains(@aria-label,'étoiles sur 5')]")
        # Erreur corrigée : la variable `dates` n'était pas définie

        for i in range(min(len(comments), len(notes))):
            try:
                texte = comments[i].text.strip()
                if texte in seen_texts:
                    continue
                seen_texts.add(texte)

                # Extraction de la note à partir de l'attribut aria-label
                note_str = notes[i].get_attribute("aria-label")
                stars = float(note_str.split(" ")[2].replace(",", "."))  # ex: "Note de 4,9 étoiles sur 5"

                # Attribution d'un label en fonction de la note
                if stars <= 2:
                    label = "négatif"
                elif stars == 3:
                    label = "neutre"
                else:
                    label = "positif"

                # Pas de date disponible ici, on la laisse vide
                date = ""

                # Stockage de l’avis dans le dictionnaire
                avis_dict[review_id] = {
                    "texte": texte,
                    "note": stars,
                    "label": label,
                    "date": date
                }
                review_id += 1

            except Exception as e:
                continue  # Ignore l’avis s’il y a une erreur

        print(f"[✓] Total actuel : {len(avis_dict)} avis.")

        # Condition d'arrêt : limite atteinte
        if len(avis_dict) >= MAX_REVIEWS:
            print("[✓] Objectif atteint.")
            break

    driver.quit()  # Ferme le navigateur
    return avis_dict  # Retourne tous les avis collectés

# Fonction pour sauvegarder les avis dans un fichier CSV
def save_to_csv(avis_dict, filename="avis_backmarket.csv"):
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "texte", "note", "label", "date"])  # En-têtes
        for i, data in avis_dict.items():
            writer.writerow([i, data["texte"], data["note"], data["label"], data["date"]])
    print(f"[✓] {len(avis_dict)} avis enregistrés dans {filename}")

# Exécution principale du script
if __name__ == "__main__":
    avis = scrape_backmarket_reviews(URL)
    save_to_csv(avis)
