# ******************************************
# Guess the number -- Coursera Mini-project
# ******************************************

# Copy this link to run in browser: http://www.codeskulptor.org/#user38_ljKsijJlwTYdxUT.py

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# initialize global variables used in your code here
new_guess = 0
secret_number = 0
limit = 100
attempts = 7

# helper function to start and restart the game

def new_game():
    global secret_number
    global attempts
    global limit
    secret_number = random.randrange(0, limit)
    if limit == 100:
        attempts = 7
    elif limit == 1000:
        attempts = 10   
    
    print
    print "New game initialized"    
    print "Range is 0 -", limit
    print "Number of guesses left is", attempts

# define event handlers for control panel

def range100():
    # button that changes the range to [0,100) and starts a new game 
    global limit
    global attempts
    limit = 100
    attempts = 7
    new_game()
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global limit
    global attempts
    limit = 1000
    attempts = 10
    new_game()
    
def input_guess(guess):     
    # main game logic goes here
    global new_guess
    global attempts
            
    new_guess = int(guess)
    print
    print "Guess was", new_guess
    
    if new_guess == secret_number:
        print "Correct"
        print
        new_game()	
    
    elif attempts == 0:
        print
        print "Guess was", new_guess
        print "Game over. The secret number was", secret_number
        print 
        new_game()
    
    else:
        if new_guess > secret_number:
            attempts = attempts - 1
            if attempts == 0:
                print "Game over. The secret number was", secret_number
            else: 
                print "Lower"
                print "Number of guesses left is", attempts

        else: #new_guess < secret_number
            
            attempts = attempts - 1
            if attempts == 0:
                print "Game over. The secret number was", secret_number
            else: 
                print "Higher"
                print "Number of guesses left is", attempts
     
# create frame
frame = simplegui.create_frame("Guess the number", 100, 200)

# register event handlers for control elements and start frame
frame.start()
frame.add_input("Your guess:", input_guess, 100)
frame.add_button("Range: 0 - 100", range100, 150)
frame.add_button("Range: 0 - 1000", range1000, 150)

# call new_game 
new_game()
