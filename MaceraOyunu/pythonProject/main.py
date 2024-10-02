import tkinter as tk
from itertools import cycle
from PIL import Image, ImageTk

class AdventureGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Macera Oyunu")
        self.root.geometry("800x600")

        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        # Yürüme animasyonu için resim serisi
        self.walking_images = cycle([ImageTk.PhotoImage(Image.open(f'walk{i}.png')) for i in range(1,2)])
        self.current_image = self.canvas.create_image(300,400, image=next(self.walking_images))

        # Arka plan resimleri
        self.background_images = {
            0: ImageTk.PhotoImage(Image.open("forest.png")),  # Orman arka planı
            1: ImageTk.PhotoImage(Image.open("river.png")),   # Nehir arka planı
            2: ImageTk.PhotoImage(Image.open("mountain.png"))  # Dağ arka planı
        }
        self.background_image = self.canvas.create_image(400, 300, image=self.background_images[0])  # Başlangıç arka planı

        # Oyun sahneleri
        self.scene_text = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.scene_text.pack()

        # Seçenek butonları (Boyutları büyüttük ve işlevleri ters çevirdik)
        self.option1_button = tk.Button(self.root, text="", command=self.option2, font=("Helvetica", 14), width=15, height=2, padx=10, pady=10)
        self.option2_button = tk.Button(self.root, text="", command=self.option1, font=("Helvetica", 14), width=15, height=2, padx=10, pady=10)
        self.option1_button.pack(side="left", padx=50)
        self.option2_button.pack(side="right", padx=50)

        self.current_scene = 0
        self.scenes = {
            0: {"text": "Bir ormanda yürüyorsun. Nereye gitmek istersin?", "options": ["Sağa git", "Sola git"], "bg": 0},
            1: {"text": "Bir nehir buldun. Ne yapmak istersin?", "options": ["Yüzerek geç", "Köprüden geç"], "bg": 1},
            2: {"text": "Bir dağ ile karşılaştın. Tırmanmak mı istersin?", "options": ["Evet", "Hayır"], "bg": 2}
        }

        self.update_scene()

    def update_scene(self):
        # Sahneye göre görselleri ve seçenekleri güncelle
        self.scene_text.config(text=self.scenes[self.current_scene]["text"])
        self.option1_button.config(text=self.scenes[self.current_scene]["options"][1])  # Ters seçenek
        self.option2_button.config(text=self.scenes[self.current_scene]["options"][0])  # Ters seçenek

        # Arka planı değiştir
        bg_index = self.scenes[self.current_scene]["bg"]
        self.canvas.itemconfig(self.background_image, image=self.background_images[bg_index])

        # Yürüme animasyonu başlat (Hız yavaşlatıldı: 500 ms)
        self.animate_walking()

    def option1(self):
        # 1. seçenek seçildiğinde yeni sahneye geç
        self.current_scene = (self.current_scene + 1) % len(self.scenes)
        self.update_scene()

    def option2(self):
        # 2. seçenek seçildiğinde yeni sahneye geç
        self.current_scene = (self.current_scene + 2) % len(self.scenes)
        self.update_scene()

    def animate_walking(self):
        # Yürüme animasyonu (Hız yavaşlatıldı: 500 ms)
        self.canvas.itemconfig(self.current_image, image=next(self.walking_images))
        self.root.after(500, self.animate_walking)  # 500 ms'de bir animasyon

# Ana program
root = tk.Tk()
game = AdventureGame(root)
root.mainloop()
