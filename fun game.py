import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I have chosen a number between 1 and 100. Try to guess it!")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    attempts = 0
    while True:
        guess = input("Enter your guess (or 'exit' to quit): ")
        
        # Check if the user wants to exit the game
        if guess.lower() == 'exit':
            print("Exiting game...")
            break
        
        # Check if the input is a valid number
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)
        
        # Increment the number of attempts
        attempts += 1
        
        # Provide hints to the user
        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print("Congratulations! You've guessed the number {} in {} attempts!".format(secret_number, attempts))
            break

if __name__ == "__main__":
    guessing_game()
