import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "kiwi", "melon", "pear"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while True:
        print("\n" + display_word(word_to_guess, guessed_letters))
        print("Attempts left:", attempts)
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        elif guess in word_to_guess:
            print("Correct!")
            guessed_letters.append(guess)
            if set(word_to_guess) == set(guessed_letters):
                print("\nCongratulations! You guessed the word:", word_to_guess)
                return  # Terminate the function immediately after correct guess
        else:
            print("Incorrect!")
            guessed_letters.append(guess)
            if guess not in word_to_guess:
                attempts -= 1
            if attempts == 0:
                print("\nYou ran out of attempts! The word was:", word_to_guess)
                break

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()
    else:
        print("Thank you for playing Hangman!")

hangman()
