import tkinter as tk
from tkinter import messagebox
import random

# Generate a random number between 1 and 100
target_number = random.randint(1, 100)
attempts = 0

# Function to handle the guess
def check_guess():
    global attempts
    try:
        guess = int(entry.get())
        attempts += 1

        # Check the guess
        if guess < target_number:
            result_label.config(text="Too low! Try again.", fg="blue")
        elif guess > target_number:
            result_label.config(text="Too high! Try again.", fg="red")
        else:
            result_label.config(text=f"Congratulations! You guessed it in {attempts} attempts.", fg="green")
            messagebox.showinfo("Game Over", f"You guessed the number in {attempts} attempts!")
            reset_game()
    except ValueError:
        result_label.config(text="Please enter a valid integer.", fg="purple")

# Function to reset the game
def reset_game():
    global target_number, attempts
    target_number = random.randint(1, 100)
    attempts = 0
    entry.delete(0, tk.END)
    result_label.config(text="I'm thinking of a number between 1 and 100.")

# Set up the main window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")
root.config(bg="#FFF8DE")

# Add widgets
title_label = tk.Label(root, text="Number Guessing Game", font=("Helvetica", 18, "bold"), bg="#FFF8DE")
title_label.pack(pady=10)

instruction_label = tk.Label(root, text="Guess the number between 1 and 100", font=("Helvetica", 12), bg="#FFF8DE")
instruction_label.pack(pady=5)

entry = tk.Entry(root, font=("Helvetica", 14), width=10, justify="center")
entry.pack(pady=10)

guess_button = tk.Button(root, text="Guess", font=("Helvetica", 14), command=check_guess, bg="#87ceeb", fg="white")
guess_button.pack(pady=5)

result_label = tk.Label(root, text="I'm thinking of a number between 1 and 100.", font=("Helvetica", 12), bg="#FFF8DE")
result_label.pack(pady=10)

reset_button = tk.Button(root, text="Reset Game", font=("Helvetica", 12), command=reset_game, bg="#ff6347", fg="white")
reset_button.pack(pady=5)

# Run the GUI loop
root.mainloop()