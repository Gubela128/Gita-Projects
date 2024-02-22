import random

def guess_the_number():
    lower_limit = 1
    upper_limit = 100
    number_to_guess = random.randint(lower_limit, upper_limit)

    print("Welcome to Guess the Number!")
    print(f"I'm thinking of a number between {lower_limit} and {upper_limit}.")

    attempts = 0
    while True:
        guess = input("Guess the number: ")

        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if guess < lower_limit or guess > upper_limit:
            print(f"Please guess a number between {lower_limit} and {upper_limit}.")
            continue

        attempts += 1

        if guess == number_to_guess:
            print("Congratulations! You guessed the number correctly:", number_to_guess)
            print("Number of attempts:", attempts)
            return

        if guess < number_to_guess:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

guess_the_number()
