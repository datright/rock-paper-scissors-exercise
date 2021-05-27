# game.py

import random

print("Rock, Paper, Scissors, Shoot!")

user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")

#print(user_choice)
print("User Choice: ", user_choice)



# valudate the input such that only if it is one of the expected values
# ... will we continute with the rest of the program
# ... otherwise we'll stop the program before it tries to do anything else
# ... and we'll ask the user to run the program again

if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print ("Valid. Keep going")
else:
    print("OPPS. Invalid input. Try it again.")
    exit()


valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("Computer Choice: ", computer_choice)

if (user_choice == computer_choice):
    print ("The game is tied. Try one more time!")
    exit()

elif (user_choice == "rock"): 
    if (computer_choice == "paper"):
        print ("Oh, the computer won. It's ok.")
    else:
        print ("Congrats! You won!")

elif (user_choice == "paper"): 
    if (computer_choice == "scissors"):
        print ("Oh, the computer won. It's ok.")
    else:
        print ("Congrats! You won!")

elif (user_choice == "scissors"): 
    if (computer_choice == "rock"):
        print ("Oh, the computer won. It's ok.")
    else:
        print ("Congrats! You won!")        

print("This is the end of our game. Play again!")