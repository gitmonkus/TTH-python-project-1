# Python Web Development Techdegree 
# Project 1 - Number Guessing Game 

############################################################################################################
## This program is a guessing game that has the user guessing a random number between
## two numbers until correct, displaying a congratulatory message
## Then the program will ask the user if they wish to play again
## If yes, then the game will begin again and display the [HIGH SCORE], which is the lower number of guesses 
## needed to guess the random number
## If no or anything else, then the game will exit with a goodbye
############################################################################################################

## import random, so we can use it to generate random numbers
import random

## Variables to use throughout the program
border_line = "=" * 100
dash_line = "-" * 100
## You can use different values for low_number and high_number to make the game easier or harder
low_number = 1
high_number = 10
high_score = []

## This function loops through the guessed numbers until you find the correct number
def loop_through_game():
    how_many_guesses = 0

 ## Creates a random number between low_number and high_number variables each time the function is called
    random_number = random.randint(low_number, high_number)  

    while True:
        how_many_guesses += 1

## This try/except is to catch any input that is not an integer, so the game can continue
        try:
            guessed_number = int(input("\n[Guess #{}]: ".format(how_many_guesses)))
        except ValueError:
            print("\n-- That was not even close to being a whole number between {} through {}... Try again!".format(low_number, high_number))
        else:
            if guessed_number < low_number or guessed_number > high_number:
                print("\n-- That's out-of-bounds!  Try guessing a whole number between {} and {}.".format(low_number, high_number))

            elif guessed_number > random_number:
                print("\n-- It's lower!")
            elif guessed_number < random_number:
                print("\n-- It's higher!")

## Number guessed correctly, so we want the least amount of guesses to use as the [HIGH SCORE]
## This appends the how_many_guesses count into a list called, high_score
## Then if how_many_guesses is less than what's first of the list
## replace what's in the first of the list with the lower score to be called later
## Display some congratulation and exit the function with 'break'
            else:
                high_score.append(how_many_guesses)
                if how_many_guesses <= high_score[0]:
                    high_score[0] = how_many_guesses
                print()
                print(border_line)
                print("Congratulations!  YOU WIN!  YES, {} is the correct number!".format(random_number))
                print("\n-- Tell them what they win... A chance to start over and play again!  Woohoo!")
                print(border_line)
                print("\n-- It only took you {} time(s) to guess the correct number!".format(how_many_guesses))
                print()
                print(dash_line)
                break


def start_game():

##  This is where it all starts.  Welcome to the game!
    print()
    print(border_line)
    print("Hello!  Welcome to the Number Guessing Game of Glory!")
    print(border_line)
    print("\nGo ahead -- guess a whole number between {} and {}.  It's FUN!  I promise...".format(low_number, high_number))
    print(" -- NOTE: Anything entered will count as a guess!")
    print(dash_line)

## Call the loop_through_game() function to loop through the number guesses until a guess is correct
    loop_through_game()

## This starts After the loop_through_game function exits with a correct guess
## We ask the user if they wish to continue
## If 'Y' or 'y' we start the game again and print out the [HIGH SCORE]
## Then call the loop_through_game() function to loop through the number guesses until a guess is correct
## If 'N' or 'n' or anything else is entered, we exit the game program with a note and a taco

    while True:
        play_again = input("Would you like to play again? (Y/N): ")
        if play_again.lower() == "y":
            print()
            print(border_line)
            print("Alright!  Let's DO THIS!  You know how to play -- whole number {} through {} -- easy!".format(low_number, high_number))
            if high_score[0] == 1:
                print("\n-- The [HIGH SCORE] to beat is {}.  ROCK STAR!  You can't get any better than that!".format(high_score[0]))
                loop_through_game()
            else:
                print("\n-- The [HIGH SCORE] to beat is {}.  Good luck!".format(high_score[0]))
                print(border_line)
                loop_through_game()
        else:
            print()
            print(border_line)
            print("Sorry to see you go!  Let's play again soon!")
            print(border_line)
            break
            
# Kick off the program by calling the start_game function
start_game()