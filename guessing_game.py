####################################### 
## Python Web Development Techdegree ##
## Project 1 - Number Guessing Game  ##
#######################################

import random

border_line = "=" * 100
dash_line = "-" * 100
low_number = 1
high_number = 10
hint_number = 5
random_number = random.randint(low_number, high_number)    

    
def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    how_many_guesses = 0

    print()
    print(border_line)
    print("Hello!  Welcome to the Number Guessing Game of Glory!")
    print(border_line)

    print(random_number)
    print("\nGo ahead -- guess a number between {} and {}.  It's FUN!  I promise...".format(low_number, high_number))
    print(dash_line)
    while True:
        
        how_many_guesses += 1
        
        guessed_number = int(input("\nGuess #{} | \n_________|: ".format(how_many_guesses)))
        
        if guessed_number < low_number or guessed_number > high_number:
            print("\nThat's out-of-bounds \N{TACO}!  Try guessing a number between {} and {}.".format(low_number, high_number))

        elif how_many_guesses == hint_number:
            wanna_hint = input("\nThat's {} guesses already!  Do you want a hint? (Y/N)".format(how_many_guesses))
            print("\nYou didn't actually think choosing '{}' would work did you?  Try guessing the number between {} and {}!".format(wanna_hint, low_number, high_number))

        elif guessed_number > random_number:
            print("\nSo close, but the correct number is lower!")
        elif guessed_number < random_number:
            print("\nSo close, but the correct number is higher!")
        #elif guessed_number == random_number:
        else:
            print()
            print(border_line)
            print("Congratulations -- YOU WIN!  You guessed the right number!")
            print("-- Tell them what they win, Johnny... A chance to play again!  Woohoo!")
            print(border_line)
            print("\nIt only took you {} times to guess the right number!".format(how_many_guesses))
            print()
            print(dash_line)
            break
        
            

    
    

# Kick off the program by calling the start_game function.
start_game()