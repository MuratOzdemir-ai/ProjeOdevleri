import requests
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk  # Görsel işleme için ek kütüphane

# Tüm para birimleri
currencies = [
    "Avustralya Doları (AUD)",
    "Kanada Doları (CAD)",
    "İsviçre Frangı (CHF)",
    "Çin Yuanı (CNY)",
    "Çek Korunası (CZK)",
    "Danimarka Kronu (DKK)",
    "Euro (EUR)",
    "İngiliz Sterlini (GBP)",
    "Hong Kong Doları (HKD)",
    "Macar Forinti (HUF)",
    "Endonezya Rupiah'ı (IDR)",
    "İsrail Şekeli (ILS)",
    "Hindistan Rupisi (INR)",
    "Japon Yeni (JPY)",
    "Güney Kore Wonu (KRW)",
    "Meksika Pesosu (MXN)",
    "Norveç Kronu (NOK)",
    "Yeni Zelanda Doları (NZD)",
    "Polonya Zloty’si (PLN)",
    "Romanya Leu (RON)",
    "Rus Rublesi (RUB)",
    "İsveç Kronu (SEK)",
    "Singapur Doları (SGD)",
    "Tayland Bahtı (THB)",
    "Türk Lirası (TRY)",
    "Amerikan Doları (USD)",
    "Güney Afrika Randı (ZAR)"
]

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rates = data.get("rates", {})
        if target_currency in rates:
            return rates[target_currency]
        else:
            messagebox.showerror("Hata", f"Para birimi '{target_currency}' bulunamadı.")
            return None
    else:
        messagebox.showerror("Hata", f"Veri alınamadı: {response.status_code}")
        return None

def format_result(amount, base_currency, converted_amount, target_currency):
    return f"{amount} {base_currency} ≈ {converted_amount:.2f} {target_currency}"

def convert_currency():
    try:
        base_currency = base_currency_combobox.get().upper()
        target_currency = target_currency_combobox.get().upper()
        amount = float(amount_entry.get())

        rate = get_exchange_rate(base_currency, target_currency)
        if rate:
            converted_amount = amount * rate
            result = format_result(amount, base_currency, converted_amount, target_currency)
            result_label.config(text=result)
        else:
            result_label.config(text="Dönüştürme başarısız.")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir miktar girin!")

# Tkinter arayüzünü oluştur
window = tk.Tk()
window.title("Döviz Çevirici")
window.geometry("400x300")

# Arka plan resmini yükle
background_image = Image.open("background.jpg")  # Görsel dosyanızın ismini girin
background_image = background_image.resize((400, 300), Image.LANCZOS)  # Resmi boyutlandır
bg_photo = ImageTk.PhotoImage(background_image)

# Arka plan etiketi oluştur
bg_label = tk.Label(window, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)  # Arka planı tüm pencereye yay

# Kullanıcıdan giriş almak için etiketler ve giriş alanları
amount_label = tk.Label(window, text="Miktar:", font=("Arial", 12), bg="lightblue")
amount_label.pack(pady=10)

amount_entry = tk.Entry(window, font=("Arial", 12))
amount_entry.pack(pady=5)

base_currency_label = tk.Label(window, text="Ana para birimi:", font=("Arial", 12), bg="lightblue")
base_currency_label.pack(pady=10)

base_currency_combobox = ttk.Combobox(window, values=currencies, font=("Arial", 12))
base_currency_combobox.pack(pady=5)

target_currency_label = tk.Label(window, text="Hedef para birimi:", font=("Arial", 12), bg="lightblue")
target_currency_label.pack(pady=10)

target_currency_combobox = ttk.Combobox(window, values=currencies, font=("Arial", 12))
target_currency_combobox.pack(pady=5)

# Çevirme butonu
convert_button = tk.Button(window, text="Çevir", command=convert_currency, bg="lightblue", font=("Arial", 12))
convert_button.pack(pady=20)

# Sonuç etiketi
result_label = tk.Label(window, text="", font=("Arial", 12), bg="lightblue")
result_label.pack(pady=10)

# Arayüzü başlat
window.mainloop()
