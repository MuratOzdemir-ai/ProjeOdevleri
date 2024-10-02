import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")

        # Arka plan resmi ayarları
        self.background_image = Image.open("background.jpg")  # Görsel dosyanızın ismini girin
        self.bg_image = ImageTk.PhotoImage(self.background_image)

        # Arka plan resmi için label
        self.bg_label = tk.Label(self.master, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        # Pencere boyutu değiştiğinde arka planı yeniden boyutlandır
        self.master.bind("<Configure>", self.resize_background)

        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()

    def resize_background(self, event):
        # Arka plan resmini yeniden boyutlandır
        resized_image = self.background_image.resize((event.width, event.height), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(resized_image)
        self.bg_label.config(image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

    def create_buttons(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.master, text=" ", font=("Arial", 24), width=5, height=2,
                                   command=lambda r=row, c=col: self.make_move(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            winner = self.check_winner()

            if winner:
                messagebox.showinfo("Oyun Bitti", f"{winner} kazandı!")
                self.reset_board()
            elif self.is_board_full():
                messagebox.showinfo("Oyun Bitti", "Oyun berabere!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Satırlar ve sütunlar için kazanan kontrolü
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                return row[0]

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return self.board[0][col]

        # Çaprazlar için kazanan kontrolü
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]

        return None

    def is_board_full(self):
        return all(cell != " " for row in self.board for cell in row)

    def reset_board(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=" ")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400")  # Başlangıç boyutu
    game = TicTacToe(root)
    root.mainloop()
