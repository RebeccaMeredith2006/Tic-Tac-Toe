
import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Noughts and Crosses")

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, text="", width=10, height=5, command=lambda i=i, j=j: self.click(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.turn = "X"
        self.game_over = False

        self.window.mainloop()

    def click(self, i, j):
        if not self.game_over and self.buttons[i][j]["text"] == "":
            self.buttons[i][j]["text"] = self.turn
            self.check_winner()
            self.turn = "O" if self.turn == "X" else "X"

    def check_winner(self):
        # Check rows
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                self.game_over = True
                self.show_winner(self.buttons[i][0]["text"])

        # Check columns
        for j in range(3):
            if self.buttons[0][j]["text"] == self.buttons[1][j]["text"] == self.buttons[2][j]["text"] != "":
                self.game_over = True
                self.show_winner(self.buttons[0][j]["text"])

        # Check diagonals
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            self.game_over = True
            self.show_winner(self.buttons[0][0]["text"])
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            self.game_over = True
            self.show_winner(self.buttons[0][2]["text"])

        # Check for a draw
        if not self.game_over and all(all(button["text"] != "" for button in row) for row in self.buttons):
            self.game_over = True
            self.show_winner("Draw")

    def show_winner(self, winner):
        tk.messagebox.showinfo("Game Over", f"{winner} wins!")
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["state"] = tk.DISABLED

if __name__ == "__main__":
    game = TicTacToe()