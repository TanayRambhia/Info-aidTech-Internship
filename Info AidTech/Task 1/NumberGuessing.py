import random

def play_game():
    # generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # initialize variables
    num_guesses = 0
    player_name = input("Enter your name: ")
    
    # loop for 10 attempts
    while num_guesses < 10:
        # get user input for their guess
        guess = int(input("Guess a number between 1 and 100: "))
        num_guesses += 1
        
        # check if the guess is correct
        if guess == secret_number:
            print("Congratulations, " + player_name + "! You guessed the number in " + str(num_guesses) + " attempts.")
            return
        # provide feedback if the guess is too high
        elif guess > secret_number:
            print("Too high!")
        # provide feedback if the guess is too low
        else:
            print("Too low!")
    
    # if the player has used up all of their guesses
    print("Sorry, " + player_name + ", you didn't guess the number in time. The number was " + str(secret_number) + ".")

def main():
    # loop to allow players to play multiple times
    while True:
        play_game()
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            break

if __name__ == "__main__":
    main()
