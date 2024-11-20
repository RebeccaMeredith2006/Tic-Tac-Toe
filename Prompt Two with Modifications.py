import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Noughts and Crosses")
root.configure(bg="#ADD8E6")  # Light blue background

# Variables
current_player = "X"  # Player X starts
board = [["" for _ in range(3)] for _ in range(3)]  # 3x3 board

# Helper functions
def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

def check_draw():
    for row in board:
        if "" in row:
            return False
    return True

def button_click(row, col):
    global current_player
    if board[row][col] == "":
        board[row][col] = current_player
        if current_player == "X":
            buttons[row][col].config(text="X", fg="red")  # X in red
        else:
            buttons[row][col].config(text="O", fg="blue")  # O in blue

        winner = check_winner()
        if winner:
            messagebox.showinfo("Noughts and Crosses", f"Player {winner} wins!")
            reset_board()
            return
        elif check_draw():
            messagebox.showinfo("Noughts and Crosses", "It's a draw!")
            reset_board()
            return

        # Switch player
        current_player = "O" if current_player == "X" else "X"

def reset_board():
    global current_player, board
    current_player = "X"
    board = [["" for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg="#A3D5FF")  # Pale yellow buttons

# Create buttons for the grid with colors
buttons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        button = tk.Button(root, text="", font=("Gill Sans MT", 40), width=5, height=2,
                           command=lambda r=row, c=col: button_click(r, c),
                           bg="#A3D5FF")  # Pale yellow button background
        button.grid(row=row, column=col, padx=5, pady=5)
        buttons[row][col] = button

# Start main loop
root.mainloop()

