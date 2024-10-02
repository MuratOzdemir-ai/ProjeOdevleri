from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_driver_path = "C:\\Users\\MURAT\\Desktop\\chromedriver-win64\\chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

araclar = {
    "mini": "https://www.sahibinden.com/ilan/vasita-arazi-suv-pickup-mini-baykar-dan-2023-mini-cooper-1.5-countryman-1.5-edition-iconic-1182655601/detay",
    "jeep": "https://www.sahibinden.com/ilan/vasita-arazi-suv-pickup-jeep-sahibinden-2023-model-jeep-compass-1193230558/detay",
}

fiyatlar = {}

for arac, url in araclar.items():
    driver.get(url)
    try:
        fiyat_elementi = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[4]/div[1]/div/div[2]/div[2]/h3/span'))
        )
        fiyatlar[arac] = fiyat_elementi.text
    except Exception as e:
        print(f"{arac} için hata: {e}")

for arac, fiyat in fiyatlar.items():
    print(f"{arac} fiyatı: {fiyat}")

if len(fiyatlar) == 2:
    try:
        mini_fiyat = float(fiyatlar["mini"].replace(' TL', '').replace('.', '').replace(',', '.'))
        jeep_fiyat = float(fiyatlar["jeep"].replace(' TL', '').replace('.', '').replace(',', '.'))

        if mini_fiyat < jeep_fiyat:
            print("Mini Countryman daha ucuz.")
        else:
            print("Jeep Compass daha ucuz.")
    except ValueError as e:
        print(f"Fiyat dönüştürme hatası: {e}")
else:
    print("Fiyatlar bulunamadı.")

driver.quit()




