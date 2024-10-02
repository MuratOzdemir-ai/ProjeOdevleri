import tkinter as tk
from tkinter import messagebox
import json
import os


class NoteApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Post-it Note Uygulaması")
        self.master.geometry("400x800")  # Yüksekliği 800 olarak ayarlandı
        self.master.configure(bg="#f0f0f0")  # Arka plan rengini ayarla
        self.notes = {}  # Notları saklamak için bir sözlük
        self.hidden_notes = {}  # Gizli notları saklamak için bir sözlük

        # Arayüz elemanları
        self.note_name_label = tk.Label(master, text="Not Adı:", font=("Arial", 14))
        self.note_name_label.pack(pady=5)

        self.note_name_entry = tk.Entry(master, font=("Arial", 14))
        self.note_name_entry.pack(pady=5)

        self.text_area = tk.Text(master, font=("Arial", 14), wrap=tk.WORD, height=10)
        self.text_area.pack(pady=10, padx=10, fill=tk.BOTH)

        self.save_button = tk.Button(master, text="Kaydet", command=self.save_note, bg="lightgreen", width=15, height=2)
        self.save_button.pack(pady=5)

        self.delete_button = tk.Button(master, text="Notu Sil", command=self.delete_selected_note, bg="lightcoral", width=15, height=2)
        self.delete_button.pack(pady=5)

        self.clear_button = tk.Button(master, text="Ekranı Temizle", command=self.clear_text_area, bg="lightyellow", width=15, height=2)
        self.clear_button.pack(pady=5)

        self.hide_button = tk.Button(master, text="Gizle", command=self.hide_note, bg="lightblue", width=15, height=2)
        self.hide_button.pack(pady=5)

        self.unhide_button = tk.Button(master, text="Gizlemeyi Kaldır", command=self.unhide_note, bg="lightblue", width=15, height=2)
        self.unhide_button.pack(pady=5)

        self.note_list = tk.Listbox(master, font=("Arial", 12), selectmode=tk.SINGLE)
        self.note_list.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.note_list.bind("<<ListboxSelect>>", self.on_note_select)

        self.load_notes()  # Başlangıçta notları yükle

    def save_note(self):
        note_text = self.text_area.get("1.0", tk.END).strip()
        note_name = self.note_name_entry.get().strip()  # Not adı buradan alınıyor
        if not note_text or not note_name:
            messagebox.showwarning("Uyarı", "Boş not kaydedemezsiniz!")
            return

        self.notes[note_name] = note_text
        self.text_area.delete("1.0", tk.END)  # Metin kutusunu temizle
        self.note_name_entry.delete(0, tk.END)  # Not adı giriş alanını temizle
        self.update_note_list()  # Not listesini güncelle
        self.save_notes_to_file()  # Notları dosyaya kaydet

    def load_selected_note(self, event=None):
        selected_note = self.note_list.curselection()
        if selected_note:
            note_name = self.note_list.get(selected_note)
            if note_name in self.hidden_notes:
                messagebox.showwarning("Uyarı", "Bu not gizli. Önce gizlemeyi kaldırın!")
                return
            self.text_area.delete("1.0", tk.END)  # Metin kutusunu temizle
            self.text_area.insert(tk.END, self.notes[note_name])  # Seçilen notu yükle
            self.note_name_entry.delete(0, tk.END)  # Not adı giriş alanını temizle
            self.note_name_entry.insert(0, note_name)  # Seçilen not adını giriş alanına yerleştir

    def delete_selected_note(self):
        selected_note = self.note_list.curselection()
        if selected_note:
            note_name = self.note_list.get(selected_note)
            if note_name in self.notes:
                del self.notes[note_name]  # Notu sil
            elif note_name in self.hidden_notes:
                del self.hidden_notes[note_name]  # Gizli notu sil
            self.update_note_list()  # Listeyi güncelle
            self.save_notes_to_file()  # Notları dosyaya kaydet
            self.clear_text_area()  # Metin kutusunu temizle
        else:
            messagebox.showwarning("Uyarı", "Silmek için bir not seçin!")

    def clear_text_area(self):
        self.text_area.delete("1.0", tk.END)  # Metin kutusunu temizle
        self.note_name_entry.delete(0, tk.END)  # Not adı giriş alanını temizle

    def on_note_select(self, event):
        self.load_selected_note()

    def update_note_list(self):
        self.note_list.delete(0, tk.END)  # Listeyi temizle
        for note_name in sorted(self.notes.keys()):  # Not adlarını alfabetik sıraya göre sırala
            self.note_list.insert(tk.END, note_name)  # Not adını listeye ekle
        for note_name in sorted(self.hidden_notes.keys()):  # Gizli notları da listeye ekle
            self.note_list.insert(tk.END, f"{note_name} (Gizli)")  # Gizli not adını listeye ekle

    def save_notes_to_file(self):
        with open("notes.json", "w") as file:
            json.dump({"notes": self.notes, "hidden_notes": self.hidden_notes}, file)

    def load_notes(self):
        if os.path.exists("notes.json"):
            with open("notes.json", "r") as file:
                data = json.load(file)
                self.notes = data.get("notes", {})
                self.hidden_notes = data.get("hidden_notes", {})
                self.update_note_list()  # Listeyi güncelle

    def hide_note(self):
        selected_note = self.note_list.curselection()
        if not selected_note:
            messagebox.showwarning("Uyarı", "Gizlemek için bir not seçin!")
            return

        note_name = self.note_list.get(selected_note)
        if note_name in self.notes:
            self.hidden_notes[note_name] = self.notes[note_name]  # Notu gizle
            del self.notes[note_name]  # Notu normal notlardan sil
            self.update_note_list()
            self.save_notes_to_file()  # Notları güncelle

    def unhide_note(self):
        selected_note = self.note_list.curselection()
        if not selected_note:
            messagebox.showwarning("Uyarı", "Gizlemeyi kaldırmak için bir not seçin!")
            return

        note_name = self.note_list.get(selected_note).replace(" (Gizli)", "")  # Gizli notun adını al
        if note_name in self.hidden_notes:
            self.notes[note_name] = self.hidden_notes[note_name]  # Notu aç
            del self.hidden_notes[note_name]  # Gizli notlardan sil
            self.update_note_list()
            self.save_notes_to_file()  # Notları güncelle


if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()
