import tkinter as tk
from tkinter import messagebox

class Totito:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Totito")
        self.turn = "X"  # Empieza el jugador X
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    self.window, text="", font=("Arial", 24), width=5, height=2,
                    command=lambda r=row, c=col: self.make_move(r, c)
                )
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.turn
            self.buttons[row][col].config(text=self.turn)
            if self.check_winner():
                messagebox.showinfo("Fin del juego", f"¡El jugador {self.turn} ganó!")
                self.reset_board()
            elif self.is_draw():
                messagebox.showinfo("Fin del juego", "¡Es un empate!")
                self.reset_board()
            else:
                self.turn = "O" if self.turn == "X" else "X"

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def is_draw(self):
        return all(self.board[row][col] != "" for row in range(3) for col in range(3))

    def reset_board(self):
        self.turn = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = Totito()
    game.run()
