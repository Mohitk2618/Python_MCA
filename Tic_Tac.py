import tkinter as tk

# Initialize the main application window
root = tk.Tk()
root.resizable(False, False)
root.title("Tic Tac Toe")

# Game state variables
current_chr = "X"
board = [[None for _ in range(3)] for _ in range(3)]  # 3x3 board to track cell values

# Functions
    
def reset_game():  # Reset the game board and status.
    global current_chr, board
    current_chr = "X"
    board = [[None for _ in range(3)] for _ in range(3)]  # Reset board state
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", state=tk.NORMAL, bg='lightgray')  # Reset button state
    status_label.config(text="X's turn")  # Reset status label
    play_again_button.grid_remove()  # Hide play again button

def check_winner():    # Check if there's a winner or a draw.
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0]:  # Row
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i]:  # Column
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0]:  # Diagonal
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2]:  # Reverse diagonal
        return board[0][2]

    # Check for a draw (all cells filled)
    if all(board[row][col] for row in range(3) for col in range(3)):
        return "Draw"
    return None

def on_button_click(row, col):
    # Handle button clicks.
    global current_chr
    if not board[row][col]:  # Only allow changes to empty cells
        board[row][col] = current_chr  # Set current player's mark on the board
        buttons[row][col].config(text=current_chr, bg='white')  # Update button appearance
        winner = check_winner()
        if winner:  # If there's a winner or draw
            status_label.config(text=f"{winner} wins!" if winner != "Draw" else "It's a draw!")
            disable_board()
            play_again_button.grid(row=4, column=0, columnspan=3)  # Show play again button
        else:
            current_chr = "O" if current_chr == "X" else "X"  # Switch turn
            status_label.config(text=f"{current_chr}'s turn")  # Update status label

def disable_board():
    # Disable all buttons on the board.
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(state=tk.DISABLED)

# UI Components
status_label = tk.Label(root, text="X's turn", font=('Ariel', 15), bg='green', fg='white')
status_label.grid(row=0, column=0, columnspan=3, sticky="ew")  # Use grid for the status label

# Board buttons
buttons = [[tk.Button(root, text="", width=10, height=5, bg='lightgray',
                      command=lambda r=row, c=col: on_button_click(r, c))
            for col in range(3)] for row in range(3)]

# Pack buttons into a grid
for row in range(3):
    for col in range(3):
        buttons[row][col].grid(row=row + 1, column=col, padx=5, pady=5)

# Play Again button
play_again_button = tk.Button(root, text="Play Again", font=('Ariel', 15), command=reset_game)
play_again_button.grid(row=4, column=0, columnspan=3)
play_again_button.grid_remove()  # Hide play again button initially

# Start the application
root.mainloop()