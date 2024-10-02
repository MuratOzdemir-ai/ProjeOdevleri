import tkinter as tk
import random
from PIL import Image, ImageTk

# Oyun seçenekleri
options = ["Taş", "Kağıt", "Makas"]

# Skor
user_score = 0
computer_score = 0

# Tkinter penceresi
window = tk.Tk()
window.title("Taş Kağıt Makas Oyunu")

# Pencere boyutu
window.geometry("600x400")

# Seçim görselleri
rock_img = ImageTk.PhotoImage(Image.open("tas.png").resize((100, 100)))
paper_img = ImageTk.PhotoImage(Image.open("kagit.png").resize((100, 100)))
scissors_img = ImageTk.PhotoImage(Image.open("makas.png").resize((100, 100)))

# Skor Label'ları
score_label = tk.Label(window, text="Kullanıcı: 0 | Bilgisayar: 0", font=("Helvetica", 16))
score_label.pack(pady=10)

# Kullanıcı ve bilgisayar seçimleri için label'lar
user_choice_label = tk.Label(window, text="Kullanıcı Seçimi:", font=("Helvetica", 14))
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(window, text="Bilgisayar Seçimi:", font=("Helvetica", 14))
computer_choice_label.pack(pady=5)

# Oyun sonucu gösterimi
result_label = tk.Label(window, text="", font=("Helvetica", 16))
result_label.pack(pady=10)


# Kazananı belirleme
def check_winner():
    if user_score == 10:
        result_label.config(text="Kazandınız! Oyun Bitti!")
        disable_buttons()
    elif computer_score == 10:
        result_label.config(text="Kaybettiniz! Oyun Bitti!")
        disable_buttons()


# Seçim fonksiyonu
def user_choice(choice):
    global user_score, computer_score

    computer_choice = random.choice(options)

    # Bilgisayar seçimini güncelle
    computer_choice_label.config(text=f"Bilgisayar Seçimi: {computer_choice}")

    # Oyun sonucunu belirle
    if choice == computer_choice:
        result_label.config(text="Beraberlik!")
    elif (choice == "Taş" and computer_choice == "Makas") or \
            (choice == "Kağıt" and computer_choice == "Taş") or \
            (choice == "Makas" and computer_choice == "Kağıt"):
        result_label.config(text="Kazandın!")
        user_score += 1
    else:
        result_label.config(text="Kaybettin!")
        computer_score += 1

    # Skor güncelle
    score_label.config(text=f"Kullanıcı: {user_score} | Bilgisayar: {computer_score}")

    # Kazananı kontrol et
    check_winner()


# Butonları devre dışı bırak
def disable_buttons():
    rock_button.config(state=tk.DISABLED)
    paper_button.config(state=tk.DISABLED)
    scissors_button.config(state=tk.DISABLED)


# Yeniden başlatma fonksiyonu
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text="Kullanıcı: 0 | Bilgisayar: 0")
    result_label.config(text="")
    computer_choice_label.config(text="Bilgisayar Seçimi:")
    enable_buttons()


# Butonları etkinleştir
def enable_buttons():
    rock_button.config(state=tk.NORMAL)
    paper_button.config(state=tk.NORMAL)
    scissors_button.config(state=tk.NORMAL)


# Butonlar
rock_button = tk.Button(window, image=rock_img, command=lambda: user_choice("Taş"))
rock_button.pack(side=tk.LEFT, padx=20)

paper_button = tk.Button(window, image=paper_img, command=lambda: user_choice("Kağıt"))
paper_button.pack(side=tk.LEFT, padx=20)

scissors_button = tk.Button(window, image=scissors_img, command=lambda: user_choice("Makas"))
scissors_button.pack(side=tk.LEFT, padx=20)

# Yeniden Başlat butonu
reset_button = tk.Button(window, text="Yeniden Başlat", command=reset_game, font=("Helvetica", 14))
reset_button.pack(pady=20)

# Oyunu başlat
window.mainloop()
