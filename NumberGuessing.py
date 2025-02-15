import random
import os
import sys
import time

os.system('clear')
def guess_the_number():
    print("Welcome to Guess the Number Game!")

    rounds = int(input("Enter the number of rounds you want to play: "))
    total_score = 0

    for round in range(1, rounds + 1):
        print(f"\nRound {round}")
        number_to_guess = random.randint(1, 100)
        attempts = 0
        max_attempts = 10
        score = 0

        while attempts < max_attempts:
            try:
                user_guess = int(input("Enter your guess (between 1 and 100): "))
                attempts += 1

                if user_guess < 1 or user_guess > 100:
                    print("Please enter a number between 1 and 100.")
                    continue

                if user_guess < number_to_guess:
                    print("Higher!")
                elif user_guess > number_to_guess:
                    print("Lower!")
                else:
                    print("Congratulations! You've guessed the number.")

                    score = max(0, 100 - (attempts - 1) * 10)
                    total_score += score
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        if attempts == max_attempts:
            print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")
            print("Your Score is 0")

        print(f"Round {round} score: {score}")

    print(f"\nGame Over! Your total score is: {total_score}")

if __name__ == "__main__":
    guess_the_number()