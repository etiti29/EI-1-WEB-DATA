from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time

# Liste des URLs de produits Cdiscount
URLS = [ 
    "https://www.cdiscount.com/telephonie/telephone-mobile/apple-iphone-x-64go-argent-reconditionne-excel/f-1440402-auc3344908271351.html?idOffre=4197729920#mpos=0|mp", 
]

def slugify(url): 
    """Extrait un identifiant de nom de fichier depuis l’URL produit"""
    return url.split("/")[5]

def scrape_reviews(URL):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 15)
    driver.get(URL)
    time.sleep(3)

    try:
        bouton_avis = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-id='avis-accordion']")))
        driver.execute_script("arguments[0].scrollIntoView(true);", bouton_avis)
        time.sleep(1)
        bouton_avis.click()
        time.sleep(2)
    except:
        print(f"[!] Échec d'ouverture de l'accordéon 'Avis clients' pour {URL}")
        driver.quit()
        return {}

    avis_dict = {}
    page = 1
    review_id = 0

    while True:
        print(f"📄 Page {page} – {slugify(URL)}")

        items = driver.find_elements(By.CSS_SELECTOR, "li.c-customer-reviews__item")
        if not items:
            print("[!] Aucun avis trouvé sur cette page.")
            break

        for item in items:
            try:
                text_block = item.find_element(By.CSS_SELECTOR, "div.c-customer-review__content p")
                score_block = item.find_element(By.CSS_SELECTOR, "span.c-stars-result")
                text = text_block.text.strip()
                score = int(score_block.get_attribute("data-score"))

                stars = score // 20

                if stars <= 2:
                    label = "négatif"
                elif stars == 3:
                    label = "neutre"
                else:
                    label = "positif"

                avis_dict[review_id] = {
                    "texte": text,
                    "note": stars,
                    "label": label
                }
                review_id += 1
            except:
                continue

        print(f"[✓] {len(items)} avis traités sur la page {page}")

        try:
            bouton_suivant = driver.find_element(By.CSS_SELECTOR, "input[value='Suivant']")
            if bouton_suivant.get_attribute("disabled"):
                print("[✓] Fin des pages.")
                break
            driver.execute_script("arguments[0].click();", bouton_suivant)
            time.sleep(2)
            page += 1
        except:
            print("[!] Bouton suivant non trouvé ou erreur.")
            break

    driver.quit()
    return avis_dict

def save_dict_to_csv(avis_dict, filename):
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "texte", "note", "label"])
        for i, data in avis_dict.items():
            writer.writerow([i, data["texte"], data["note"], data["label"]])
    print(f"[✓] {len(avis_dict)} avis enregistrés dans {filename}")

# 🔁 Lancer pour chaque URL
for URL in URLS:
    avis = scrape_reviews(URL)
    output_filename = f"avis_{slugify(URL)}.csv"
    save_dict_to_csv(avis, output_filename)





