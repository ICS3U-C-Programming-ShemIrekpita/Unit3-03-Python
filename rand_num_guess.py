#!/usr/bin/env python3
# Created by: Shem
# Created on: 10/19/2025
# This program asks the user to guess a number between 0 and 5
# and tells them if they guessed correctly or not.

import random  # This imports the random module to generate random numbers

def main():
# This generate a random number between 0 and 5
    correct_answer = random.randint(0, 5)

# Input: This ask's the user to guess a number
    guess = int(input("Guess a number between 0 and 5: "))

# Process and Output: Check if the guess matches the random number
    if guess == correct_answer:
        print("You guessed correctly!")
    else:
        print("You guessed wrong. The correct answer was:", correct_answer)

# This ensures the program starts
if __name__ == "__main__":
    main()
