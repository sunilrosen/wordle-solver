# Wordle Clone

A Python-based interactive clone of the popular word game "Wordle," complete with a graphical user interface (GUI) created using `Tkinter` and an additional word suggestion solver for strategic guessing.

---

## Features

### Wordle Clone (wordle_clone.py):
- **Interactive GUI**: Play Wordle with a visual grid and on-screen keyboard.
- **Dynamic Feedback**: Tiles and keyboard keys update dynamically to reflect correct guesses (green), misplaced letters (yellow), and incorrect guesses (gray).
- **Smart Input Handling**:
  - Supports typing guesses using the keyboard.
  - On-screen clickable keyboard for convenience.

### Wordle Solver (wordle_solver.py):
- **Optimal Word Suggestions**: Recommends the best word to guess based on letter frequencies and previous guesses.
- **Interactive Prompt**: Guides users through the game, processing guesses and results to filter potential solutions.
- **Smart Filtering**:
  - Eliminates impossible words based on incorrect, misplaced, and correct letters.
  - Adapts dynamically to user feedback for precise suggestions.
- **Advanced Scoring System**: Calculates word scores based on letter frequencies for optimal decision-making.


## Usage

### Wordle Clone:
1. Run the game:
   ```bash
   python wordle_clone.py
   ```
2. Use your keyboard or click the on-screen keyboard to type guesses.
3. Try to guess the correct 5-letter word in 6 attempts or fewer.
4. Observe the color-coded feedback:
   - **Green**: Correct letter in the correct position.
   - **Yellow**: Correct letter in the wrong position.
   - **Gray**: Incorrect letter.
5. The game ends when:
   - You guess the correct word.
   - You use all 6 attempts.
6. The game window closes automatically after 2 minutes.

### Wordle Solver:
1. Run the solver:
   ```bash
   python wordle_solver.py
   ```
2. Follow the interactive prompts to enter guesses and feedback.
   - **Feedback Codes**:
     - `g`: Letter is correct and in the correct position.
     - `y`: Letter is correct but in the wrong position.
     - `w`: Letter is incorrect.
3. Observe the suggested next guess.
4. Continue until the word is solved or all attempts are used.

---

## How It Works

### Wordle Clone:
- Reads valid 5-letter words from `words.txt`.
- Randomly selects a word for each game session.
- Dynamically updates the UI to reflect player guesses and feedback.

### Wordle Solver:
- Filters possible words using advanced logic based on user feedback.
- Calculates letter frequencies to optimize the next guess.
- Continuously refines the solution space until the correct word is found.