import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"

# Function to handle user choice
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(["rock", "paper", "scissors"])
    result_label.config(text=f"Computer chose: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)
    if winner == "user":
        user_score += 1
        messagebox.showinfo("Result", "You win this round!")
    elif winner == "computer":
        computer_score += 1
        messagebox.showinfo("Result", "Computer wins this round!")
    else:
        messagebox.showinfo("Result", "It's a draw!")

    update_score()

# Function to update the score
def update_score():
    score_label.config(text=f"Score: You {user_score} - {computer_score} Computer")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    update_score()
    result_label.config(text="Make your choice!")

# Initialize scores
user_score = 0
computer_score = 0

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.configure(bg="#f0f8ff")  # Light blue background

# Create widgets
title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 20, "bold"), bg="#4682b4", fg="white")
title_label.pack(pady=10, fill=tk.X)

result_label = tk.Label(root, text="Make your choice!", font=("Arial", 16), bg="#f0f8ff", fg="#2f4f4f")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score: You 0 - 0 Computer", font=("Arial", 14), bg="#f0f8ff", fg="#2f4f4f")
score_label.pack(pady=10)

button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=10, bg="#ff6347", fg="white", font=("Arial", 12), command=lambda: play("rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=10, bg="#32cd32", fg="white", font=("Arial", 12), command=lambda: play("paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, bg="#1e90ff", fg="white", font=("Arial", 12), command=lambda: play("scissors"))
scissors_button.grid(row=0, column=2, padx=5)

reset_button = tk.Button(root, text="Reset Game", bg="#ffa500", fg="white", font=("Arial", 12), command=reset_game)
reset_button.pack(pady=10)

# Run the application
root.mainloop()