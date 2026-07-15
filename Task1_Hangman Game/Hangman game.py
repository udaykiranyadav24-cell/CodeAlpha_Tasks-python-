import random

#List of words to guess
words = ["python", "hangman", "challenge", "keyboard", "codealpha", "programming"]

#Pick a random word
word_to_guess = random.choice(words)
guessed_letters = []
attempts_left = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.\n")

#Game loop
while attempts_left > 0:
    # Display current word state
    display_word = [letter if letter in guessed_letters else "_" for letter in word_to_guess]
    print("Word:", " ".join(display_word))

    # Check for win
    if "_" not in display_word:
        print("\nYou won! The word was:", word_to_guess)
        break

    # Take input
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("Correct guess!\n")
    else:
        attempts_left -= 1
        print(f"Wrong guess! Attempts left: {attempts_left}\n")

# If loop ends without winning
if attempts_left == 0:
    print("Game Over! The word was:", word_to_guess)