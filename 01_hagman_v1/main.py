import random

words = ['python', 'css', 'javascript', 'ruby', 'rust', 'java', 'flask', 'html'] # vocabulary tech

# function to select a random word
def select_word() -> str:
    return random.choice(words)


# function to play the game
def play() -> None:
    word = select_word()
    guessed_letters = ["_"] * len(word)
    attempts = 6
    wrong_guesses = []

    print("\n----Welcome to Hagman----\n")


    while attempts > 0 and "_" in guessed_letters:
        print("\nWord: " + " ".join(guessed_letters))
        print(f"Wrong guesses: {', '.join(wrong_guesses)}")
        print(f"You have {attempts} attempts left.")
        
        # Ask the player to guess a letter
        guess = input("Guess a letter: ").lower()
        
        # Check if the letter has already been guessed
        if guess in guessed_letters or guess in wrong_guesses:
            print("You've already guessed that letter. Try another one.")
            continue
        
        # If the letter is in the word
        if guess in word:
            print(f"Correct! The letter '{guess}' is in the word.")
            # Replace the underscores with the correctly guessed letter
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_letters[i] = guess
        else:
            print(f"The letter '{guess}' is not in the word.")
            wrong_guesses.append(guess)
            attempts -= 1  # Decrease the number of attempts


        if "_" not in guessed_letters:
            print(f"\nCongratulations! You guessed the word: {word}")
        else:
            print(f"\nGame Over! The word was: {word}")


play()
