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
score_x = 0  # Score for player X
score_o = 0  # Score for player O

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

def update_score():
    score_label_x.config(text=f"Player X: {score_x}")
    score_label_o.config(text=f"Player O: {score_o}")

def button_click(row, col):
    global current_player, score_x, score_o
    if board[row][col] == "":
        # Mark the board and update button text
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, fg="red" if current_player == "X" else "blue")

        # Check for a win or draw
        winner = check_winner()
        if winner:
            if winner == "X":
                score_x += 1
            else:
                score_o += 1
            update_score()
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
            root.after(500, ai_move)  # Delay AI move by 500 ms

def ai_move():
    global current_player, score_o
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ""]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = "O"
        buttons[row][col].config(text="O", fg="blue")

        # Check for win or draw after AI move
        winner = check_winner()
        if winner:
            score_o += 1
            update_score()
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
            buttons[row][col].config(text="", bg="#A3D5FF")  # Pale yellow buttons

def go_home():
    # Clear the game grid and show the main menu again
    for widget in root.winfo_children():
        widget.destroy()
    create_main_menu()

def start_game(mode):
    global game_mode
    game_mode = mode
    for widget in root.winfo_children():
        widget.destroy()
    create_game_grid()

def create_game_grid():
    global buttons, score_label_x, score_label_o
    buttons = [[None for _ in range(3)] for _ in range(3)]

    # Score frame with a card-like style and shadow effect
    score_frame = tk.Frame(root, bg="#D3D3D3", padx=20, pady=10, relief="solid", bd=2)

    score_frame.grid(row=0, column=0, columnspan=3, pady=(10, 0), padx=10, ipadx=5, ipady=5)
    score_label_x = tk.Label(score_frame, text=f"Player X: {score_x}", font=("Gill Sans MT", 16, "bold"), bg="#FFDDC1", fg="darkred", padx=10, pady=5)
    score_label_x.grid(row=0, column=0, padx=10)

    score_label_o = tk.Label(score_frame, text=f"Player O: {score_o}", font=("Gill Sans MT", 16, "bold"), bg="#C1D7FF", fg="darkblue", padx=10, pady=5)
    score_label_o.grid(row=0, column=1, padx=10)

    # Create game grid
    for row in range(3):
        for col in range(3):
            button = tk.Button(root, text="", font=("Gill Sans MT", 40), width=5, height=2,
                               command=lambda r=row, c=col: button_click(r, c),
                               bg="#A3D5FF")  # Pale yellow button background
            button.grid(row=row+1, column=col, padx=5, pady=5)
            buttons[row][col] = button

    # Reset button
    reset_button = tk.Button(root, text="Reset", font=("Gill Sans MT", 20), command=reset_board, bg="#FF6347", fg="white")  # Tomato color
    reset_button.grid(row=4, column=0, columnspan=1, pady=10)

    # Home button
    home_button = tk.Button(root, text="Home", font=("Gill Sans MT", 20), command=go_home, bg="#4682B4", fg="white")  # Steel blue color
    home_button.grid(row=4, column=2, columnspan=1, pady=10)

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


