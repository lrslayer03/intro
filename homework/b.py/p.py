
import tkinter as tk
import random

def play(player):
    computer = random.choice(["Rock", "Paper", "Scissors"])

    player_label.config(text="You chose: " + player)
    computer_label.config(text="Computer chose: " + computer)

    if player == computer:
        result_label.config(text="It's a draw!")
    elif player == "Rock" and computer == "Scissors":
        result_label.config(text="You win!")
    elif player == "Paper" and computer == "Rock":
        result_label.config(text="You win!")
    elif player == "Scissors" and computer == "Paper":
        result_label.config(text="You win!")
    else:
        result_label.config(text="Computer wins!")

def reset():
    player_label.config(text="You chose: ")
    computer_label.config(text="Computer chose: ")
    result_label.config(text="Choose Rock, Paper or Scissors!")

window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("400x300")

title_label = tk.Label(window, text="Rock Paper Scissors", font=("Arial", 16))
title_label.pack(pady=10)

player_label = tk.Label(window, text="You chose: ")
player_label.pack()

computer_label = tk.Label(window, text="Computer chose: ")
computer_label.pack()

result_label = tk.Label(window, text="Choose Rock, Paper or Scissors!")
result_label.pack(pady=10)

rock_button = tk.Button(window, text="Rock", command=lambda: play("Rock"))
rock_button.pack()

paper_button = tk.Button(window, text="Paper", command=lambda: play("Paper"))
paper_button.pack()

scissors_button = tk.Button(window, text="Scissors", command=lambda: play("Scissors"))
scissors_button.pack()

reset_button = tk.Button(window, text="Restart Game", command=reset)
reset_button.pack(pady=10)

window.mainloop()
