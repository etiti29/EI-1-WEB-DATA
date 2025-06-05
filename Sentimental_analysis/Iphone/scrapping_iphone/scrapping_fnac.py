from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time

# Liste d'URLs FNAC produit avec avis clients
URLS = [
    "https://www.fr.fnac.ch/IPHONE-A-1/a19813594", 
    "https://www.fr.fnac.ch/iPhone-15-6-1-5G-Double-SIM-128-Go-Noir/a18573408",
    "https://www.fr.fnac.ch/iPhone-15-6-1-5G-Double-SIM-128-Go-Bleu/a18573440",
    "https://www.fr.fnac.ch/iPhone-14-6-1-5G-Double-SIM-128-Go-Noir-minuit/a17312754"
]

def slugify(url):
    return url.split("/")[3] if "/a" in url else url.split("/")[4]

def scrape_fnac_reviews(URL):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 15)
    driver.get(URL)
    time.sleep(3)

    avis_dict = {}
    review_id = 0

    try:
        # Attente du premier avis
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.f-nCarousel__item")))
        print(f"[✓] Avis détectés sur {slugify(URL)}")
    except:
        print(f"[!] Aucun avis trouvé sur {URL}")
        driver.quit()
        return {}

    while True:
        items = driver.find_elements(By.CSS_SELECTOR, "li.f-nCarousel__item")
        if not items:
            break

        for item in items:
            try:
                text = item.find_element(By.CSS_SELECTOR, "p.customerReviewsComment__description").text.strip()
                score = item.find_element(By.CSS_SELECTOR, "span.f-star-score").text.strip()
                stars = int(score)

                # Label : 1-2 = négatif, 3 = neutre, 4-5 = positif
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

        # Pagination FNAC : cliquer sur la flèche droite si elle existe
        try:
            next_btn = driver.find_element(By.CSS_SELECTOR, "button.f-nCarousel__arrow--next")
            if next_btn.is_enabled():
                driver.execute_script("arguments[0].click();", next_btn)
                time.sleep(1.5)
            else:
                break
        except:
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
    avis = scrape_fnac_reviews(URL)
    output_filename = f"avis_fnac_{slugify(URL)}.csv"
    save_dict_to_csv(avis, output_filename)
