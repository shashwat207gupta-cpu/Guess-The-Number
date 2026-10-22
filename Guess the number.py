import random

secret = random.randint(1, 1000)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 1000.")

while True:
    try:
        guess = int(input("Guess the number: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    attempts += 1

    if guess < secret:
        print("Too Low")
    elif guess > secret:
        print("Too High")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
