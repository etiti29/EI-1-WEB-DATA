from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import csv

URL = "https://fr.shopping.rakuten.com/mfp/shop/7270256/apple-iphone-13?pid=7197507097&sellerLogin=KNDigital&fbbaid=16370875570&rd=1"  # Remplace par une vraie URL
MAX_REVIEWS = 6000


def setup_driver():
    options = Options()
    options.add_argument('--start-maximized')  # fenêtre normale
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver = setup_driver()
wait = WebDriverWait(driver, 60)

def scroll_softly(driver, steps=10):
    for _ in range(steps):
        wait
        driver.execute_script("window.scrollBy(0, 300);")
        time.sleep(random.uniform(0.2, 0.6))

def scrape_rakuten_reviews(url):
    driver = setup_driver()
    wait = WebDriverWait(driver, 60)
    driver.get(url)
    time.sleep(random.uniform(3, 5))

    reviews = {}
    seen = set()
    review_id = 0
    page = 1

    while True:
        print(f"📄 Page {page} – scraping...")

        scroll_softly(driver)

        try:
            wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.reviewCtn.reviewDetails")))
        except:
            print("[!] Aucun avis détecté.")
            break

        blocks = driver.find_elements(By.CSS_SELECTOR, "div.reviewCtn.reviewDetails")

        for block in blocks:
            try:
                note_elem = block.find_element(By.CSS_SELECTOR, "p.starRating > span.value")
                note = int(note_elem.text.strip())

                comment_elem = block.find_element(By.CSS_SELECTOR, "blockquote.description")
                raw_html = comment_elem.get_attribute("innerHTML")
                texte = ' '.join(raw_html.replace("<br>", "\n").split()).strip()

                if texte in seen:
                    continue
                seen.add(texte)

                label = "négatif" if note <= 2 else "neutre" if note == 3 else "positif"

                reviews[review_id] = {
                    "texte": texte,
                    "note": note,
                    "label": label
                }
                review_id += 1

                if review_id >= MAX_REVIEWS:
                    break

            except:
                continue

        print(f"[✓] {len(reviews)} avis collectés.")

        if review_id >= MAX_REVIEWS:
            print("[✓] Objectif atteint.")
            break

        # Pagination – cliquer sur "Suivant"
        try:
            next_btn = driver.find_element(By.ID, "link_next")
            if "inactive" in next_btn.get_attribute("class"):
                print("[✓] Fin des pages.")
                break
            driver.execute_script("arguments[0].scrollIntoView();", next_btn)
            time.sleep(random.uniform(1.5, 3))
            next_btn.click()
            time.sleep(random.uniform(2.5, 5))
            page += 1
        except:
            print("[!] Erreur ou plus de page.")
            break

    driver.quit()
    return reviews

def save_reviews_to_csv(reviews, filename="avis_rakuten.csv"):
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "texte", "note", "label"])
        for i, data in reviews.items():
            writer.writerow([i, data["texte"], data["note"], data["label"]])
    print(f"[✓] {len(reviews)} avis enregistrés dans {filename}")

# Lancer
if __name__ == "__main__":
    avis = scrape_rakuten_reviews(URL)
    save_reviews_to_csv(avis)
