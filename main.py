import random

def hangman_game():
    # List of words to choose from
    words = ["python", "hangman", "challenge", "coding", "programming", "developer"]
    
    # Randomly select a word
    word_to_guess = random.choice(words)
    guessed_word = ["_"] * len(word_to_guess)  # Initialize with underscores
    attempts_left = 6  # Set the number of incorrect guesses allowed
    guessed_letters = set()  # To keep track of guessed letters

    print("Welcome to Hangman!")
    print("Guess the word letter by letter.")
    print("You have", attempts_left, "incorrect guesses allowed.")
    print("Word: ", " ".join(guessed_word))

    while attempts_left > 0 and "_" in guessed_word:
        guess = input("Enter a letter: ").lower()

        # Check if input is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        # Check if letter was already guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)  # Add the letter to guessed letters

        if guess in word_to_guess:
            print("Good job! The letter is in the word.")
            # Update guessed_word with the correct guess
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts_left -= 1
            print("Incorrect guess. You have", attempts_left, "attempts left.")

        print("Word: ", " ".join(guessed_word))

    # Check if the user won or lost
    if "_" not in guessed_word:
        print("Congratulations! You guessed the word:", word_to_guess)
    else:
        print("You lost. The word was:", word_to_guess)

if __name__ == "__main__":
    hangman_game()
