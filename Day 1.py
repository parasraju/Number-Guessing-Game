import random  

while True:  # Loop for replay option
    length = int(input("Enter the maximum number you want to guess: "))  

    # Generate a truly random number within range 0 to length
    random_number = random.randint(0, length)  

    attempts = 3
    print(f"You have {attempts} tries to guess the number between 0 and {length}.")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))  

        if guess == random_number:  
            print(f"🎉 Correct! You guessed it in {attempt} tries!")
            break  # Exits loop if guessed correctly
        else:  
            if guess < random_number:
                print("🔼 Too low! Try again.")
            else:
                print("🔽 Too high! Try again.")

            remaining_attempts = attempts - attempt
            if remaining_attempts > 0:
                print(f"⏳ You have {remaining_attempts} attempt(s) left.")
            else:
                print(f"❌ Out of attempts! The correct number was {random_number}.")

    # Asks user if they want to play again
    replay = input("🔄 Do you want to play again? (yes/no): ").strip().lower()
    if replay != "yes":
        print("👋 Thanks for playing! See you next time.")
        break  # Exits game loop
