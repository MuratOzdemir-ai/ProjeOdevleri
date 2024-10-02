import tkinter as tk
from PIL import Image, ImageTk
import random

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Çift Zar Atma Oyunu")
root.geometry("500x400")

# Zar yüzleri için resimler
zar_gorselleri = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png']
zar_resimleri = []

# Resimleri yükleme
for gorsel in zar_gorselleri:
    img = Image.open(gorsel)
    img = img.resize((100, 100))
    zar_resimleri.append(ImageTk.PhotoImage(img))

# Oyuncu skorları
oyuncu_1_skor = 0
oyuncu_2_skor = 0
oyuncu_tur = 1


# Zar atma fonksiyonu
def zar_at():
    global oyuncu_1_skor, oyuncu_2_skor, oyuncu_tur
    gorsel_label.config(image=zar_resimleri[0])  # İlk önce zarları boş göster
    gorsel_label2.config(image=zar_resimleri[0])  # İkinci zar için de boş göster

    # Animasyon döngüsü
    for _ in range(10):  # 10 kez döndür
        zar1_sonucu = random.randint(1, 6)
        zar2_sonucu = random.randint(1, 6)
        gorsel_label.config(image=zar_resimleri[zar1_sonucu - 1])
        gorsel_label2.config(image=zar_resimleri[zar2_sonucu - 1])
        root.update()
        root.after(100)  # Her 100ms'de bir yeni zar göster

    # Nihai zar atışı
    zar1 = random.randint(1, 6)
    zar2 = random.randint(1, 6)
    gorsel_label.config(image=zar_resimleri[zar1 - 1])  # İlk zar
    gorsel_label2.config(image=zar_resimleri[zar2 - 1])  # İkinci zar

    toplam_zar = zar1 + zar2  # Toplamı hesapla
    toplam_label.config(text=f"Toplam: {toplam_zar}")  # Toplamı göster

    if oyuncu_tur == 1:
        oyuncu_1_skor += toplam_zar
        oyuncu_1_skor_label.config(text=f"1. Oyuncu Skor: {oyuncu_1_skor}")
        oyuncu_tur = 2
    else:
        oyuncu_2_skor += toplam_zar
        oyuncu_2_skor_label.config(text=f"2. Oyuncu Skor: {oyuncu_2_skor}")
        oyuncu_tur = 1

    if oyuncu_1_skor >= 30:
        kazanan_label.config(text="1. Oyuncu Kazandı!")
    elif oyuncu_2_skor >= 30:
        kazanan_label.config(text="2. Oyuncu Kazandı!")


# Başlangıç mesajı
baslangic_label = tk.Label(root, text="Çift Zar Atma Oyunu", font=("Arial", 20))
baslangic_label.pack(pady=20)

# Zarın görselini gösterecek etiketler
frame = tk.Frame(root)
frame.pack()

gorsel_label = tk.Label(frame)
gorsel_label.pack(side=tk.LEFT, padx=20)

gorsel_label2 = tk.Label(frame)
gorsel_label2.pack(side=tk.LEFT, padx=20)  # Yanyana yerleştirildi

# Toplam zar etiketini oluştur
toplam_label = tk.Label(root, text="Toplam: 0", font=("Arial", 16))
toplam_label.pack(pady=10)  # Toplam label'ı zarların altında

# Oyuncu 1 ve Oyuncu 2 skorlarını gösterecek etiketler
oyuncu_1_skor_label = tk.Label(root, text="1. Oyuncu Skor: 0", font=("Arial", 14))
oyuncu_1_skor_label.pack()

oyuncu_2_skor_label = tk.Label(root, text="2. Oyuncu Skor: 0", font=("Arial", 14))
oyuncu_2_skor_label.pack()

# Zar atma butonu
zar_at_button = tk.Button(root, text="Zar At", command=zar_at, font=("Arial", 16), width=10)
zar_at_button.pack(pady=20)

# Kazananı gösteren etiket
kazanan_label = tk.Label(root, text="", font=("Arial", 16))
kazanan_label.pack(pady=20)

# Pencereyi çalıştır
root.mainloop()
