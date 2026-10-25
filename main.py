import random

# Hangman ASCII Art for Visual Stages (0 to 6 mistakes)
HANGMAN_PICS = [
    '''
     +---+
         |
         |
         |
        ===''' , '''
     +---+
     O   |
         |
         |
        ===''' , '''
     +---+
     O   |

     |   |
         |
        ===''' , '''
     +---+
     O   |
    /|   |
         |
        ===''' , '''
     +---+
     O   |
    /|\\  |
         |
        ===''' , '''
     +---+
     O   |
    /|\\  |
    /    |
        ===''' , '''
     +---+
     O   |
    /|\\  |
    / \\  |
        ==='''
]

# Words Pool (You can also download and read from the .txt file provided)
WORDS = ['PYTHON', 'DATHEON', 'DEVELOPER', 'ENGINEER', 'SOFTWARE', 'PROGRAMMING', 'INTERFACE', 'VARIABLE']

def play_hangman():
    # 1. Select a random secret word
    secret_word = random.choice(WORDS).upper()
    guessed_letters = set()
    mistakes = 0
    max_attempts = 6

    print("====================================")
    print("  WELCOME TO DATHEON HANGMAN GAME!  ")
    print("====================================\n")

    while mistakes < max_attempts:
        # Display the corresponding ASCII stage
        print(HANGMAN_PICS[mistakes])
        
        # 2. Build and display the masked string (e.g., _ A _ H E O N)
        masked_word = [letter if letter in guessed_letters else '_' for letter in secret_word]
        print("\nWord to guess: " + " ".join(masked_word))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Remaining attempts: {max_attempts - mistakes}")

        # Check Win Condition
        if '_' not in masked_word:
            print("\n====================================")
            print(f"🎉 VICTORY! You guessed the word: {secret_word}")
            print("====================================")
            break

        # 3. Take User Input
        guess = input("\nEnter a letter: ").upper().strip()

        # Input Validations
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input! Please enter a single alphabetical letter.")
            continue
        
        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'. Penalty prevented!")
            continue

        # Add to guessed list
        guessed_letters.add(guess)

        # 4. Check if letter is in word
        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.")
        else:
            print(f"❌ Wrong guess! '{guess}' is not in the word.")
            mistakes += 1

    # Check Defeat Condition
    if mistakes == max_attempts:
        print(HANGMAN_PICS[mistakes])
        print("\n====================================")
        print(f"💀 DEFEAT! You ran out of attempts.")
        print(f"The correct word was: {secret_word}")
        print("====================================")

if __name__ == "__main__":
    play_hangman()
