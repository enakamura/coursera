import simplegui
import random
import math

secret_number = None
range = None
allowed_guess = None

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global allowed_guess
    if range == 1000:
        secret_number = random.randrange(0,1000)
        allowed_guess = 10
        print 'New Game. Range is from 0 to 1000'
    else:
        secret_number = random.randrange(0,100)
        allowed_guess = 7
        print 'New Game. Range is from 0 to 100'
    print 'Number of remaining guesses is', allowed_guess, '\n'

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range
    range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range
    range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global allowed_guess
    
    guessInt = int(guess)
    print 'Guess was ',guessInt
    
    allowed_guess -= 1
    print 'Number of remaining guesses is', allowed_guess
    
    if allowed_guess > 0:
        if guessInt < secret_number:
            print 'Higher\n'
        elif guessInt > secret_number:
            print 'Lower\n'
        else:
            print 'Correct\n'
            new_game()
    else:
        print 'You ran out of guesses. The number was',secret_number,'\n'
        new_game()
        
# create frame
f = simplegui.create_frame('Guess the Number',300,300)

# register event handlers for control elements and start frame
f.add_button('Range is [0, 100)',range100)
f.add_button('Range is [0, 1000)',range1000)
f.add_input('Enter a guess',input_guess,100)

# call new_game 
new_game()
