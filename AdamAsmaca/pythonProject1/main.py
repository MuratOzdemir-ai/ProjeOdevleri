import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Oyun için kelimeler
kelimeler = [
    "accept", "achieve", "admire", "admit", "advise", "agree", "allow", "answer", "apologize", "appear",
    "apply", "approve", "argue", "arrive", "ask", "attack", "avoid", "become", "begin", "believe",
    "belong", "break", "bring", "build", "buy", "call", "cancel", "change", "choose", "clean",
    "close", "collect", "compare", "complain", "complete", "consider", "continue", "copy", "correct", "create",
    "cut", "decide", "deliver", "depend", "describe", "design", "destroy", "develop", "discuss", "discover",
    "draw", "drive", "eat", "encourage", "enjoy", "enter", "explain", "fall", "feel", "find",
    "finish", "fit", "fly", "follow", "forget", "forgive", "give", "go", "grow", "happen",
    "hate", "hear", "help", "hope", "imagine", "improve", "include", "inform", "invite", "join",
    "keep", "know", "learn", "leave", "lend", "like", "listen", "live", "look", "lose",
    "make", "move", "need", "offer", "open", "order", "pay", "play", "prepare", "promise",
    "provide", "reach", "read", "receive", "remember", "return", "run", "say", "see", "send"
]

# Oyun verileri
kelime = random.choice(kelimeler)
tahmin_edilenler = ["_"] * len(kelime)
yanlis_tahmin = 0
maks_hata = 6  # Adam resim sayısına göre ayarlayın
dogru_tahminler = set()
yanlis_harfler = set()

# Tkinter Penceresi
window = tk.Tk()
window.title("Adam Asmaca Oyunu")

# Pencere boyutu ve arka plan resmi
window.geometry("800x400")  # Boyutu büyüttük
canvas = tk.Canvas(window, width=800, height=400)
canvas.pack()

# Arka plan resmini ekleme
bg_image = Image.open("background.png")
bg_image = bg_image.resize((800, 400), Image.Resampling.LANCZOS)
bg_image = ImageTk.PhotoImage(bg_image)
canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)

# Kelime Label'ı (Büyütüldü)
kelime_label = tk.Label(window, text=" ".join(tahmin_edilenler), font=("Helvetica", 24), bg="lightgray")
kelime_label_window = canvas.create_window(300, 50, window=kelime_label)

# Adam resimlerini yükleme
adam_resimler = []
for i in range(7):  # 0'dan 6'ya kadar resimleri yükleyin
    img = Image.open(f"adam_{i}.png").resize((150, 250), Image.Resampling.LANCZOS)
    adam_resimler.append(ImageTk.PhotoImage(img))

# Adam resmini sağ tarafa yerleştirme
adam_label = tk.Label(window, image=adam_resimler[yanlis_tahmin], bg="lightgray")
adam_label_window = canvas.create_window(700, 150, window=adam_label)  # x = 700

# Tahmin girişi
tahmin_entry = tk.Entry(window, font=("Helvetica", 18))
tahmin_entry_window = canvas.create_window(300, 250, window=tahmin_entry)

# Yanlış tahminler label'ı (Büyütüldü)
yanlis_tahmin_label = tk.Label(window, text=f"Yanlış tahminler: {', '.join(yanlis_harfler)}", bg="lightgray", font=("Helvetica", 14))
yanlis_tahmin_label_window = canvas.create_window(300, 300, window=yanlis_tahmin_label)

# Harf tahmin fonksiyonu
def harf_tahmin_et(event=None):
    global yanlis_tahmin
    tahmin = tahmin_entry.get().lower()

    if tahmin in dogru_tahminler or tahmin in yanlis_harfler:
        messagebox.showinfo("Hata", "Bu harfi zaten tahmin ettiniz.")
        return

    if tahmin in kelime:
        dogru_tahminler.add(tahmin)
        for i, harf in enumerate(kelime):
            if harf == tahmin:
                tahmin_edilenler[i] = tahmin
        kelime_label.config(text=" ".join(tahmin_edilenler))

        # Eğer tüm harfler doğruysa, kazanma durumu
        if set(kelime) == dogru_tahminler:
            messagebox.showinfo("Tebrikler!", "Kelimeyi buldunuz!")
            window.quit()
    else:
        yanlis_tahmin += 1
        yanlis_harfler.add(tahmin)
        adam_label.config(image=adam_resimler[yanlis_tahmin])  # Görseli güncelle
        yanlis_tahmin_label.config(text=f"Yanlış tahminler: {', '.join(yanlis_harfler)}")

        # Yanlış tahminler dolduysa, kaybetme durumu
        if yanlis_tahmin == maks_hata:
            messagebox.showinfo("Kaybettiniz", f"Oyun bitti! Doğru kelime: {kelime}")
            window.quit()

    # Giriş kutusunu temizle
    tahmin_entry.delete(0, tk.END)

# Tahmin butonu
tahmin_button = tk.Button(window, text="Tahmin Et", command=harf_tahmin_et, font=("Helvetica", 14))
tahmin_button_window = canvas.create_window(300, 350, window=tahmin_button)

# Enter tuşuna basıldığında tahmin işlemi
window.bind('<Return>', harf_tahmin_et)

# Oyunu çalıştır
window.mainloop()





