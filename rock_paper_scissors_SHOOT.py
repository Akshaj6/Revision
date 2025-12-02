import tkinter as tk
import random
from tkinter import messagebox
def determine_winner(user_choice, computer_choice):
    """Determines the winner based on Rock, Paper, Scissors rules."""
    if user_choice == computer_choice:
        return "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You Win!"
    else:
        return "Computer Wins!"
def play_game(user_choice):
    """Plays a round of Rock, Paper, Scissors and displays the result."""
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    user_choice_label.config(text=f"Your Choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Result: {result}", font=("Arial", 16, "bold"), fg="blue")
app = tk.Tk()
app.title("Rock, Paper, Scissors SHOOT")
app.geometry("400x400")
instruction_label = tk.Label(app, text="Choose your weapon!", font=("Arial", 14))
instruction_label.pack(pady=10)
rock_button = tk.Button(app, text="Rock", width=15, height=2, command=lambda: play_game("Rock"))
rock_button.pack(pady=5)
paper_button = tk.Button(app, text="Paper", width=15, height=2, command=lambda: play_game("Paper"))
paper_button.pack(pady=5)
scissors_button = tk.Button(app, text="Scissors", width=15, height=2, command=lambda: play_game("Scissors"))
scissors_button.pack(pady=5)
user_choice_label = tk.Label(app, text="Your Choice: ", font=("Arial", 12))
user_choice_label.pack(pady=10)
computer_choice_label = tk.Label(app, text="Computer's Choice: ", font=("Arial", 12))
computer_choice_label.pack(pady=5)
result_label = tk.Label(app, text="Result: ", font=("Arial", 16, "bold"), fg="blue")
result_label.pack(pady=20)
app.mainloop()