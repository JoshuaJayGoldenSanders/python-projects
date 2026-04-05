import random # Used to generate a random number 

def play_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0 # Track number of guesses

    print(" Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100.")

    while True:
        guess = input("Enter your guess: ")

        # Check if Input is a number
        if not guess.isdigit():
            print(" Please enter a valid number.")
            continue
        guess = int(guess)
        attempts += 1
      
        # Check if guess is in valid range
        if guess < 1 or guess > 100:
            print(" Guess must be between 1 and 100.")
        elif guess < secret_number:
            print(" Too low!")
        elif guess > secret_number: 
            print(" Too high!")
        else: 
            # Correct guess
            print(f" Correct! You guessed it in {attempts} tries.")
            break

# Main game loop
while True: 
    play_game()
    replay = input("Play again? (y/n): ").lower()
    if replay != 'y':
        print(" Thanks for playing!")
        break
