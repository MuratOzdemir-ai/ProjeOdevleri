import random
import string
import tkinter as tk
from tkinter import messagebox


def generate_password():
    try:
        # Kullanıcının girdiği uzunluğu al
        length = int(entry.get())
        if length < 1:
            raise ValueError("Şifre uzunluğu 1'den küçük olamaz!")

        # Harfler, sayılar ve semboller
        letters = string.ascii_letters  # Büyük ve küçük harfler
        digits = string.digits  # Sayılar
        symbols = string.punctuation  # Semboller

        # Karakter havuzunu birleştir
        all_characters = letters + digits + symbols

        # Rastgele bir şifre oluştur
        password = ''.join(random.choice(all_characters) for i in range(length))

        # Sonucu ekrana yazdır
        result_label.config(text=f"Oluşturulan Parola: {password}")
        copy_button.config(state="normal")  # Parola oluşturulunca kopyala butonunu aktif et
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir uzunluk girin!")


def copy_password():
    # Panoya şifreyi kopyala
    window.clipboard_clear()  # Panoyu temizle
    window.clipboard_append(result_label.cget("text").split(": ")[1])  # Panoya şifreyi ekle
    messagebox.showinfo("Bilgi", "Parola kopyalandı!")


# Tkinter pencere oluştur
window = tk.Tk()
window.title("Rastgele Parola Üretici")
window.geometry("400x250")

# Giriş alanı
label = tk.Label(window, text="Parola uzunluğunu girin:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 12))
entry.pack(pady=5)

# Parola oluştur butonu
generate_button = tk.Button(window, text="Parola Oluştur", command=generate_password, bg="lightblue",
                            font=("Arial", 12))
generate_button.pack(pady=10)

# Sonuç gösterme etiketi
result_label = tk.Label(window, text="", font=("Arial", 12), fg="green")
result_label.pack(pady=10)

# Parola kopyala butonu (başlangıçta devre dışı)
copy_button = tk.Button(window, text="Parolayı Kopyala", command=copy_password, bg="lightgreen", font=("Arial", 12),
                        state="disabled")
copy_button.pack(pady=10)

# Uygulamayı çalıştır
window.mainloop()

