from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests


def login_to_instagram(username, password):
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Görünür modda çalıştır
    chrome_service = Service("C:\\Users\\MURAT\\Desktop\\chromedriver-win64\\chromedriver.exe")

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.get('https://www.instagram.com/accounts/login/')

    time.sleep(2)

    user_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
    pass_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))

    user_input.send_keys(username)  # Kullanıcı adını buraya yaz
    pass_input.send_keys(password)  # Şifreyi buraya yaz

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    login_button.click()
    time.sleep(5)  # Girişin tamamlanması için bekle

    return driver


def download_photos(driver, target_username):
    driver.get(f'https://www.instagram.com/{target_username}/')
    time.sleep(5)  # Sayfanın yüklenmesini bekle

    # Fotoğraf URL'lerini bul
    photos = driver.find_elements(By.TAG_NAME, 'img')
    for index, photo in enumerate(photos):
        src = photo.get_attribute('src')
        if src:
            response = requests.get(src)
            if response.status_code == 200:  # İndirme işlemi başarılıysa
                with open(f'photo_{index}.jpg', 'wb') as file:
                    file.write(response.content)  # Fotoğrafı indir
                print(f'İndirilen fotoğraf: {src}')


# Kullanıcı bilgilerinizi ve hedef kullanıcı adını girin
username = ''  # Kendi kullanıcı adınızı buraya yazın
password = ''  # Kendi şifrenizi buraya yazın
target_username = ''  # Hedef kullanıcı adını buraya yazın

# Instagram'a giriş yap
driver = login_to_instagram(username, password)

# Fotoğrafları indir
download_photos(driver, target_username)

# Tarayıcıyı kapat
driver.quit()

