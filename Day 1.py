import random  
length = int(input("Enter the maximum number you want to guess:"))  
random_number = random.randint(0, length)   
guess = int(input(f"Guess the number between 0 and {length}: "))  
if guess == random_number:  
    print("🎉 Number Guessed Correctly!")  
else:  
    print(f"❌ Incorrect guess! The number was {random_number}.")  