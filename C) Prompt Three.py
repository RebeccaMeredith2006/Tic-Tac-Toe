import tkinter as tk
import random
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Noughts and Crosses")
root.configure(bg="#ADD8E6")  # Light blue background

# Variables
current_player = "X"  # Player X starts
board = [["" for _ in range(3)] for _ in range(3)]  # 3x3 board
game_mode = "Multiplayer"  # Default mode

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
        # Mark the board and update button text
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, fg="red" if current_player == "X" else "blue")

        # Check for a win or draw
        winner = check_winner()
        if winner:
            messagebox.showinfo("Noughts and Crosses", f"Player {winner} wins!")
            reset_board()
            return
        elif check_draw():
            messagebox.showinfo("Noughts and Crosses", "It's a draw!")
            reset_board()
            return

        # Switch player or call AI move
        if game_mode == "Multiplayer":
            current_player = "O" if current_player == "X" else "X"
        elif game_mode == "Single Player":
            current_player = "O"
            root.after(200, ai_move)  # Delay AI move by 250 ms

def ai_move():
    global current_player
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ""]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = "O"
        buttons[row][col].config(text="O", fg="blue")

        # Check for win or draw after AI move
        winner = check_winner()
        if winner:
            messagebox.showinfo("Noughts and Crosses", "Player O (AI) wins!")
            reset_board()
            return
        elif check_draw():
            messagebox.showinfo("Noughts and Crosses", "It's a draw!")
            reset_board()
            return

        current_player = "X"

def reset_board():
    global current_player, board
    current_player = "X"
    board = [["" for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg="#A3D5FF")  # Pale blue buttons

def start_game(mode):
    global game_mode
    game_mode = mode
    for widget in root.winfo_children():
        widget.destroy()
    create_game_grid()

def create_game_grid():
    global buttons
    buttons = [[None for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            button = tk.Button(root, text="", font=("Gill Sans MT", 40), width=5, height=2,
                               command=lambda r=row, c=col: button_click(r, c),
                               bg="#A3D5FF")  # Pale blue button background
            button.grid(row=row, column=col, padx=5, pady=5)
            buttons[row][col] = button

    # Reset button
    reset_button = tk.Button(root, text="Reset", font=("Gill Sans MT", 20), command=reset_board, bg="#FF6347", fg="white")  # Tomato color
    reset_button.grid(row=3, column=0, columnspan=3, pady=10)

# Main menu
def create_main_menu():
    menu_label = tk.Label(root, text="Choose Game Mode", font=("Gill Sans MT", 24), bg="#ADD8E6")
    menu_label.pack(padx=100, pady=200)

    single_player_button = tk.Button(root, text="Single Player", font=("Gill Sans MT", 20),
                                     command=lambda: start_game("Single Player"), bg="#20B2AA", fg="white")
    single_player_button.pack(pady=10)

    multiplayer_button = tk.Button(root, text="Multiplayer", font=("Gill Sans MT", 20),
                                   command=lambda: start_game("Multiplayer"), bg="#FF6347", fg="white")
    multiplayer_button.pack(pady=10)

# Start with main menu
create_main_menu()
root.mainloop()
