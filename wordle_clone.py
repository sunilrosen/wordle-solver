import random
import tkinter as tk
from tkinter import messagebox
import threading

def processGuess(guess, answer, keyboard):
    global current_row
    position = 0
    clue = ""

    for col, letter in enumerate(guess):
        if letter == answer[position]:
            clue += "G"
            updateTile(current_row, col, letter, "green")
            updateKeyboard(keyboard, letter, "green")
        elif letter in answer:
            clue += "Y"
            updateTile(current_row, col, letter, "#8B8000")
            if keyboard[letter] != "green":
                updateKeyboard(keyboard, letter, "#8B8000")
        else:
            clue += "-"
            updateTile(current_row, col, letter, "gray")
            updateKeyboard(keyboard, letter, "black")
        position += 1

    current_row += 1
    return clue == "GGGGG"  # Return True if the guess is correct

def updateTile(row, col, letter, color):
    tile = tiles[row][col]
    tile.config(text=letter.upper(), bg=color, fg="white")

def updateKeyboard(keyboard, letter, color):
    current_color = keyboard[letter]
    # Priority: green > yellow > gray/black
    if (color == "green") or (color == "#8B8000" and current_color != "green") or (color == "black" and current_color not in ["green", "#8B8000"]):
        keyboard[letter] = color
        button = keyboard_buttons[letter]
        button.config(bg=color, fg="white" if color == "black" else "black")

def handleKeyPress(event):
    global current_guess
    if guessed_correctly:
        return  # Stop processing if the word has been guessed
    if event.keysym.lower() in "abcdefghijklmnopqrstuvwxyz" and len(current_guess) < 5:
        current_guess += event.keysym.lower()
        updateInputTiles(current_guess)
    elif event.keysym == "BackSpace" and current_guess:
        current_guess = current_guess[:-1]
        updateInputTiles(current_guess)
    elif event.keysym == "Return" and len(current_guess) == 5:
        handleGuess()


def updateInputTiles(guess):
    for i in range(5):
        if i < len(guess):
            input_tiles[i].config(text=guess[i].upper())
        else:
            input_tiles[i].config(text="")

def handleGuess():
    global num_guesses, guessed_correctly, current_guess

    guess = current_guess

    num_guesses += 1
    guessed_correctly = processGuess(guess, answer, keyboard)

    if guessed_correctly:
        displayCorrectMessage()
        # Schedule the window to close after 2 minutes
        threading.Timer(120, root.destroy).start()
    elif num_guesses == 6:
        displayGameOverMessage()  # Display a message instead of a pop-up
        # Schedule the window to close after 2 minutes
        threading.Timer(120, root.destroy).start()
    current_guess = ""
    updateInputTiles(current_guess)

def displayGameOverMessage():
    """Display the 'Game Over' message on the screen."""
    game_over_label = tk.Label(
        root, 
        text=f"Sorry, you did not guess the correct word. The word was: {answer}", 
        font=("Arial", 18), 
        fg="red"
    )
    game_over_label.pack(pady=10)

def handleKeyboardClick(letter):
    global current_guess
    if guessed_correctly:
        return  # Stop processing if the word has been guessed
    if len(current_guess) < 5:
        current_guess += letter
        updateInputTiles(current_guess)
    elif len(current_guess) == 5:
        handleGuess()


def displayCorrectMessage():
    correct_label = tk.Label(root, text="Congratulations! You guessed the word!", font=("Arial", 18), fg="green")
    correct_label.pack(pady=10)

# Read the list of words from a file
word_list = []
word_file = open("words.txt")

for word in word_file:
    word = word.strip().lower()
    if not word.endswith("s") or (word.endswith("ss") and len(word) > 2):  # Avoid plural words but allow "ss"
        word_list.append(word)

word_file.close()

# Pick a random word from the list
answer = random.choice(word_list)
num_guesses = 0
guessed_correctly = False
current_row = 0
current_guess = ""

# Initialize Tkinter root
root = tk.Tk()
root.title("Wordle Clone")

# Create a frame for the Wordle grid
grid_frame = tk.Frame(root)
grid_frame.pack(pady=10)

tiles = []
for row in range(6):
    row_tiles = []
    for col in range(5):
        tile = tk.Label(grid_frame, text="", width=4, height=2, font=("Arial", 18), bg="black", fg="white", relief="solid", borderwidth=1)
        tile.grid(row=row, column=col, padx=5, pady=5)
        row_tiles.append(tile)
    tiles.append(row_tiles)

# Create a frame for the input tiles
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

input_tiles = []
for i in range(5):
    tile = tk.Label(input_frame, text="", width=4, height=2, font=("Arial", 18), bg="black", fg="white", relief="solid", borderwidth=1)
    tile.grid(row=0, column=i, padx=5, pady=5)
    input_tiles.append(tile)

# Create a frame for the keyboard
keyboard_frame = tk.Frame(root)
keyboard_frame.pack(pady=10)

keyboard_buttons = {}
keyboard = {}

# Define keyboard layout
keys = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]

for row, key_row in enumerate(keys):
    row_frame = tk.Frame(keyboard_frame)
    row_frame.pack()
    for key in key_row:
        button = tk.Button(row_frame, text=key.upper(), width=4, height=2, bg="gray", fg="black", state="normal", command=lambda k=key: handleKeyboardClick(k))
        button.pack(side="left", padx=2, pady=2)
        keyboard_buttons[key] = button
        keyboard[key] = "gray"

# Bind keypress events
root.bind("<KeyPress>", handleKeyPress)

root.mainloop()
