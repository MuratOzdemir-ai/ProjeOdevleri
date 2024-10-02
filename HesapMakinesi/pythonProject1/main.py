import tkinter as tk

# Hesap Makinesi sınıfı
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Hesap Makinesi")

        # Görsel öğeler
        self.display = tk.Entry(master, width=30, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Tuşları tanımlama
        self.create_buttons()

    def create_buttons(self):
        # Tuşlar
        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]
        row_value = 1
        col_value = 0

        for text in button_texts:
            button = tk.Button(self.master, text=text, padx=20, pady=20, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row_value, column=col_value)

            col_value += 1
            if col_value > 3:  # 4 sütun olduğunda bir alt satıra geç
                col_value = 0
                row_value += 1

    def on_button_click(self, char):
        if char == 'C':
            self.display.delete(0, tk.END)  # Girişi temizle
        elif char == '=':
            try:
                result = eval(self.display.get())  # Girişi hesapla
                self.display.delete(0, tk.END)  # Girişi temizle
                self.display.insert(0, str(result))  # Sonucu göster
            except Exception as e:
                self.display.delete(0, tk.END)  # Girişi temizle
                self.display.insert(0, "Hata")  # Hata mesajı göster
        else:
            self.display.insert(tk.END, char)  # Tuş değerini ekle

# Tkinter penceresi
root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
