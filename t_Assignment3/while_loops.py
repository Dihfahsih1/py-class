'''Write a Python program that asks the user to guess a secret number between 1 and 100.
Keep prompting the user for guesses until they correctly guess the number.
Provide feedback (higher/lower) after each incorrect guess. 
When the user guesses correctly, 
print a congratulatory message along with the number of attempts it took them.'''

import random

# Generate a random secret number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

# Ask the user to guess the secret number
while True:
    guess = int(input("Guess the secret number (1-100): "))
    attempts += 1

    if guess < secret_number:
        print("Higher! Try again.")
    elif guess > secret_number:
        print("Lower! Try again.")
    else:
        print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
        break
