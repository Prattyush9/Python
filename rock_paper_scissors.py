
import random

print("Welcome to Rock Paper Scissors Game!")

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

player = input("Enter rock, paper or scissors: ").lower()

print("Computer chose:", computer)

if player not in choices:
    print("Invalid choice!")

elif player == computer:
    print("It's a tie!")

elif player == "rock" and computer == "scissors":
    print("Congratulations! You win!")

elif player == "paper" and computer == "rock":
    print("Congratulations! You win!")

elif player == "scissors" and computer == "paper":
    print("Congratulations! You win!")

else:
    print("Computer wins! Better luck next time.")
