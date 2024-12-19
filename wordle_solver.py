def badLetters(result, guess):
    """Finds incorrect letters in the word based on the result."""
    bad_letters = []
    for i in range(5):
        if result[i] == "w":
            bad_letters.append(guess[i])
    return bad_letters

def partialLetters(result, guess):
    """Finds correct letters that are misplaced in the word based on the result."""
    partial_letters = []
    for i in range(5):
        if result[i] == "y":
            partial_letters.append([guess[i], i])
    return partial_letters

def correctLetters(result, guess):
    """Finds fully correct letters in the word based on the result."""
    correct_letters = []
    for i in range(5):
        if result[i] == "g":
            correct_letters.append([guess[i], i])
    return correct_letters

def word_remover(result, guess, possible_words):
    """Filters out words that are not possible based on the guess and result."""
    bad_letters = badLetters(result, guess)
    correct_letters = correctLetters(result, guess)
    partial_letters = partialLetters(result, guess)
    good_letters = [g[0] for g in correct_letters] + [p[0] for p in partial_letters]

    acceptable_words1 = [w for w in possible_words if all(b not in w or b in good_letters for b in bad_letters)]

    acceptable_words2 = [w for w in acceptable_words1 if all(w[g[1]] == g[0] for g in correct_letters)]

    acceptable_words3 = [w for w in acceptable_words2 if all(w[p[1]] != p[0] for p in partial_letters)]

    acceptable_words4 = [w for w in acceptable_words3 if all(g in w for g in good_letters)]

    acceptable_words5 = [
        w for w in acceptable_words4
        if all(b not in good_letters or w.count(b) == good_letters.count(b) for b in bad_letters)
    ]

    return acceptable_words5

def letterFreq(possible_words):
    """Calculates the frequency of each letter at each position across possible words."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    arr = {c: [0] * 5 for c in alphabet}
    for w in possible_words:
        for i, c in enumerate(w):
            arr[c][i] += 1
    return arr

def wordScore(possible_words, frequencies):
    """Calculates a score for each word based on letter frequencies."""
    max_freq = [max(frequencies[c][i] for c in frequencies) for i in range(5)]

    words = {}
    for w in possible_words:
        score = 1
        for i, c in enumerate(w):
            score *= 1 + (frequencies[c][i] - max_freq[i]) ** 2
        words[w] = score
    return words

def bestWord(possible_words, frequencies):
    """Finds the best word to guess next based on scores."""
    scores = wordScore(possible_words, frequencies)
    return min(scores, key=scores.get)

def wordleSolver():
    """Interactive Wordle Solver that suggests optimal guesses."""
    print("Welcome to the Wordle Solver!")

    # Load words from words.txt and filter out plural words (ending in 's')
    with open("words.txt", "r") as file:
        possible_words = [line.strip() for line in file.readlines() if not line.strip().endswith("s")]

    # Initial guess suggestion
    print("The suggested starting word is:", bestWord(possible_words, letterFreq(possible_words)))

    print("\nHow to play:")
    print("- Enter a 5-letter guess word.")
    print("- Enter the result as a string of 5 characters, using the following codes:")
    print("  g - The letter is correct and in the correct position.")
    print("  y - The letter is correct but in the wrong position.")
    print("  w - The letter is incorrect.")

    guess = input("Enter your first guess: ")
    while len(guess) != 5:
        print("Error: Your guess must be exactly 5 letters long.")
        guess = input("Enter your first guess: ")

    result = input("Enter the result for your guess: ")
    while len(result) != 5:
        print("Error: The result must be exactly 5 characters long.")
        result = input("Enter the result for your guess: ")

    counter = 1
    while result != "ggggg" and counter < 6:
        possible_words = word_remover(result, guess, possible_words)

        if not possible_words:
            print("Oh no! No possible words left. There might be a mistake in your inputs.")
            return

        suggestion = bestWord(possible_words, letterFreq(possible_words))
        print("The suggested word is:", suggestion)

        guess = input("Enter your next guess: ")
        while len(guess) != 5:
            print("Error: Your guess must be exactly 5 letters long.")
            guess = input("Enter your next guess: ")

        result = input("Enter the result for your guess: ")
        while len(result) != 5:
            print("Error: The result must be exactly 5 characters long.")
            result = input("Enter the result for your guess: ")

        counter += 1

    if result == "ggggg":
        print(f"Congratulations! The Wordle was solved in {counter} guesses.")
    else:
        print("Number of guesses exceeded. Better luck next time!")

# Run the Wordle Solver
wordleSolver()
