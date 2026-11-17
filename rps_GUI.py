
import tkinter as tk
import random

# Main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x450")
root.config(bg="lightblue")

player_score = 0
computer_score = 0

# Game logic
def play(choice):
    global player_score, computer_score

    computer = random.choice(["Rock", "Paper", "Scissors"])

    result_label.config(
        text=f"You: {choice} | Computer: {computer}"
    )

    if choice == computer:
        message = "It's a Tie!"

    elif (choice == "Rock" and computer == "Scissors") or \
         (choice == "Paper" and computer == "Rock") or \
         (choice == "Scissors" and computer == "Paper"):

        message = "You Win!"
        player_score += 1

    else:
        message = "Computer Wins!"
        computer_score += 1

    winner_label.config(text=message)

    score_label.config(
        text=f"Player: {player_score}   Computer: {computer_score}"
    )

# Heading
title_label = tk.Label(
    root,
    text="Rock Paper Scissors",
    font=("Arial", 20, "bold"),
    bg="lightblue"
)
title_label.pack(pady=20)

# Instructions
instruction = tk.Label(
    root,
    text="Choose your move:",
    font=("Arial", 14),
    bg="lightblue"
)
instruction.pack(pady=10)

# Buttons
tk.Button(root, text="Rock", width=15,
          command=lambda: play("Rock")).pack(pady=5)

tk.Button(root, text="Paper", width=15,
          command=lambda: play("Paper")).pack(pady=5)

tk.Button(root, text="Scissors", width=15,
          command=lambda: play("Scissors")).pack(pady=5)

# Result display
result_label = tk.Label(
    root, text="Make your first move!",
    font=("Arial", 12), bg="lightblue"
)
result_label.pack(pady=15)

winner_label = tk.Label(
    root, text="",
    font=("Arial", 16, "bold"), bg="lightblue"
)
winner_label.pack(pady=10)

# Score
score_label = tk.Label(
    root,
    text="Player: 0   Computer: 0",
    font=("Arial", 14, "bold"),
    bg="lightblue"
)
score_label.pack(pady=15)

# Reset function
def reset():
    global player_score, computer_score

    player_score = 0
    computer_score = 0

    score_label.config(text="Player: 0   Computer: 0")
    result_label.config(text="Make your first move!")
    winner_label.config(text="")

tk.Button(root, text="Reset Game",
          command=reset).pack(pady=10)

root.mainloop()
