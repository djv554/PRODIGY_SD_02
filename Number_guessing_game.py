import random

def number_guessing_game():
    guess_number = random.randint(1,100)
    count = 0
    guessed = False

    print("\nWelcome to the Number Guessing Game!\n")
    print("I am thinking of a number between 1 to 100. Can you try guessing it?")

    while not guessed:
        try:
            guess = int(input("\nEnter you guess:"))
            count+=1

            if guess < guess_number:
                print("Too low! Try again.")
            elif guess > guess_number:
                print("Too high! Try again.")
            else:
                print(f"\nCongratulations! You've guessed the number right. The number was {guess_number}.")
                print(f"You guessed it in {count} attempts.")
                guessed = True
        except ValueError:
            print("Please enter a valid integer.")

number_guessing_game()
        


