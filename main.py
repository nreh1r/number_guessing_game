import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

random_number = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

lives = 0

if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5

while lives > 0:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess > random_number:
        print("Too high")
        lives -= 1
    elif guess < random_number:
        print("Too low.")
        lives -= 1
    else:
        print(f"You got it! The answer was {random_number}")
        break
    if lives > 0:
        print("Guess again.")

if lives == 0:
    print("Out of lives.")
