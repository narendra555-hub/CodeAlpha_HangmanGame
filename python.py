import random

def play_hangman():
    # Predefined list of 5 words
    words = ["python", "script", "engine", "syntax", "matrix"]
    secret_word = random.choice(words)
    guessed_letters = set()
    incorrect_guesses = 0
    max_attempts = 6

    print("=== Welcome to CodeAlpha Hangman! ===")
    
    while incorrect_guesses < max_attempts:
        # Display the word with underscores for unguessed letters
        display_word = [letter if letter in guessed_letters else "_" for letter in secret_word]
        print("\nWord to guess: " + " ".join(display_word))
        print(f"Incorrect attempts: {incorrect_guesses}/{max_attempts}")
        
        if "_" not in display_word:
            print(f"\n🎉 Congratulations! You guessed the word: '{secret_word}'!")
            return

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input! Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'. Try another one.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"✅ Correct! '{guess}' is in the word.")
        else:
            print(f"❌ Wrong guess! '{guess}' is not in the word.")
            incorrect_guesses += 1

    print(f"\n💀 Game Over! You ran out of attempts. The word was: '{secret_word}'.")

if __name__ == "__main__":
    play_hangman()
