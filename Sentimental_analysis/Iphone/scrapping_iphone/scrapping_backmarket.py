from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time

URL = "https://www.backmarket.fr/fr-fr/r/p/iphone-13-128-go-minuit-debloque-tout-operateur/ef5660d2-6883-4b81-b47d-86e5720687ef?order_by=-created_at"  # à remplacer
MAX_REVIEWS = 6000

def scroll_gradually(driver, steps=25, delay=0.6):
    for _ in range(steps):
        driver.execute_script("window.scrollBy(0, 300);")
        time.sleep(delay)

def scrape_backmarket_reviews(URL):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 20)
    driver.get(URL)
    time.sleep(3)

    avis_dict = {}
    review_id = 0
    seen_texts = set()

    while True:
        scroll_gradually(driver, steps=25, delay=0.6)

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

        # Récupération des blocs d'avis
        comments = driver.find_elements(By.CSS_SELECTOR, "p.body-1.block.whitespace-pre-line")
        notes = driver.find_elements(By.XPATH, "//div[@aria-label][contains(@aria-label,'étoiles sur 5')]")


        for i in range(min(len(comments), len(notes))):
            try:
                texte = comments[i].text.strip()
                if texte in seen_texts:
                    continue
                seen_texts.add(texte)

                note_str = notes[i].get_attribute("aria-label")
                stars = float(note_str.split(" ")[2].replace(",", "."))  # ex "Note de 4,9 étoiles sur 5"

                if stars <= 2:
                    label = "négatif"
                elif stars == 3:
                    label = "neutre"
                else:
                    label = "positif"

                # Date si disponible
                date = dates[i].text.strip() if i < len(dates) else ""

                avis_dict[review_id] = {
                    "texte": texte,
                    "note": stars,
                    "label": label,
                }
                review_id += 1

            except Exception as e:
                continue

        print(f"[✓] Total actuel : {len(avis_dict)} avis.")

        if len(avis_dict) >= MAX_REVIEWS:
            print("[✓] Objectif atteint.")
            break

    driver.quit()
    return avis_dict

def save_to_csv(avis_dict, filename="avis_backmarket.csv"):
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "texte", "note", "label", "date"])
        for i, data in avis_dict.items():
            writer.writerow([i, data["texte"], data["note"], data["label"], data["date"]])
    print(f"[✓] {len(avis_dict)} avis enregistrés dans {filename}")

# Lancer
if __name__ == "__main__":
    avis = scrape_backmarket_reviews(URL)
    save_to_csv(avis)