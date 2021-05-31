#GuessingGame.py
#April 28 2020
#ARYA PEER
#Interactive guessing game to guess a random integer between 1 and 100

#import random module
import random

#define secret number, play again, and count
secretNumber = random.randint(1, 100)
playAgain=True
count = 0

#intro
print("Welcome to GuessingGame.py")
print("I'm thinking of a secret integer between 1 and 100 (No Decimal Numbers)")

#while loop
while playAgain == True: 

    #Ask for and get the integer guess of the user
    guess = int(input("What is your guess? "))
    

    #if statement regarding the guess and its relation to the secret number
    if (guess == secretNumber):
        count=count+1
        print("Dang, you got it!")
        print("It took you ", count, "guesses to get it right.")
        
        #If statement regarding the amount of guesses it took and an encouraging statement for their amount of guesses
        if count <= 5:
            print("\nImpressive")
        elif count >=5 and count <=7:
            print("\nYou did pretty well")
        elif count == 1:
            print("\nWOW THAT IS AMAZING")
        else:
            ("\nTry to guess by splitting the range in half every guess to get it within 7 guesses or less every time!")
        #end if

        #ask for and get whether user would like to play again
        playAgainPrompt=input("\nWould you like to play again? ('y' or 'n')")
        
        #if loop to determine if game restarts
        if playAgainPrompt == "y" or playAgainPrompt == "Y" or playAgainPrompt == "Yes" or playAgainPrompt == "yes":
            print("\nI'm thinking of a secret integer between 1 and 100 (No Decimal Numbers)")
            count = 0
            secretNumber = random.randint(1, 100)
            playAgain=True
        else:
            playAgain=False 
        #end if     

    elif (guess > secretNumber):
        count=count+1
        print("Sorry, your guess is too high.")
    elif (guess < secretNumber):
        count=count+1
        print("Sorry, your guess is too low.")
    #end if   
#end loop