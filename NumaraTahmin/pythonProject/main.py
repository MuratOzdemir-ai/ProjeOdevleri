import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Sayı Tahmin Oyunu")
        self.target_number = random.randint(1, 100)
        self.guess_count = 0
        self.guess_limit = 10
        self.guess_history = []
        self.time_limit = 20  # Süre limiti
        self.time_left = self.time_limit

        # Arka plan resmi
        self.background_image = ImageTk.PhotoImage(file="images/numara.jpg")
        self.background_label = tk.Label(master, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        self.instruction_label = tk.Label(master, text="1 ile 100 arasında bir sayı tahmin edin!", font=("Helvetica", 16))
        self.instruction_label.pack(pady=20)

        self.timer_label = tk.Label(master, text=f"Süre: {self.time_left} saniye", font=("Helvetica", 14))
        self.timer_label.pack(pady=10)

        self.guess_entry = tk.Entry(master, font=("Helvetica", 14))
        self.guess_entry.pack(pady=10)

        self.guess_button = tk.Button(master, text="Tahmin Et", command=self.check_guess, font=("Helvetica", 14))
        self.guess_button.pack(pady=10)

        self.result_label = tk.Label(master, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=20)

        self.history_label = tk.Label(master, text="", font=("Helvetica", 14))
        self.history_label.pack(pady=10)

        self.restart_button = tk.Button(master, text="Yeniden Başlat", command=self.restart_game, font=("Helvetica", 14))
        self.restart_button.pack(pady=10)

        self.guess_entry.bind("<Return>", lambda event: self.check_guess())
        self.update_timer()

    def update_timer(self):
        if self.time_left > 0:
            self.timer_label.config(text=f"Süre: {self.time_left} saniye")
            self.time_left -= 1
            self.master.after(1000, self.update_timer)  # Her 1000ms'de (1 saniye) çağır
        else:
            self.result_label.config(text=f"Süre doldu! Doğru cevap: {self.target_number}")
            self.disable_inputs()

    def check_guess(self):
        guess = self.guess_entry.get()
        if guess.isdigit():
            guess = int(guess)
            self.guess_count += 1
            self.guess_history.append(f"{self.guess_count}- {guess}")
            self.update_history_label()
            if guess < self.target_number:
                self.result_label.config(text="Daha YÜKSEK bir sayı tahmin edin.")
            elif guess > self.target_number:
                self.result_label.config(text="Daha DÜŞÜK bir sayı tahmin edin.")
            else:
                self.result_label.config(text="Tebrikler! Doğru tahmin ettiniz!")
                self.disable_inputs()
            if self.guess_count >= self.guess_limit:
                self.result_label.config(text=f"Tahmin hakkınız doldu! Oyun bitti. Doğru cevap: {self.target_number}")
                self.disable_inputs()
        else:
            messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin.")
        self.guess_entry.delete(0, tk.END)

    def update_history_label(self):
        self.history_label.config(text="\n".join(self.guess_history))

    def disable_inputs(self):
        self.guess_entry.config(state='disabled')
        self.guess_button.config(state='disabled')

    def restart_game(self):
        self.target_number = random.randint(1, 100)
        self.guess_count = 0
        self.guess_history = []
        self.result_label.config(text="")
        self.update_history_label()
        self.time_left = self.time_limit  # Süreyi sıfırla
        self.timer_label.config(text=f"Süre: {self.time_left} saniye")  # Süre etiketini güncelle
        self.guess_entry.config(state='normal')
        self.guess_button.config(state='normal')
        self.guess_entry.delete(0, tk.END)
        self.update_timer()  # Zamanlayıcıyı başlat

# Tkinter ana penceresini oluştur
root = tk.Tk()
game = NumberGuessingGame(root)

# Tkinter ana döngüsünü başlat
root.mainloop()
