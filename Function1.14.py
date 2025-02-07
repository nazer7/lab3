import random
import math
def from_g_to_ounce(g):
    return g * 28.3495231
def from_F_to_C(F):
    return (5 / 9) * (F - 32)
def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]
def histogram(lst):
    for num in lst:
        print('*' * num)
def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    secret_number = random.randint(1, 20)
    attempts = 0
    while True:
        attempts += 1
        guess = int(input("\nTake a guess.\n"))
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break