#
# File: rock paperr scissor.py
# Author: Andrew Sheppard 
# Email Id: aksheppard@bigpond.com 
# Date: 31/7/22
# Description: game rock paper scissor
#
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

import random

### Get Player Choice
choice = input("Rock(1), Paper(2), Scissors(3)?")
#Validate
while choice != "1" and choice != "2" and choice != "3":
    #test validation
    print("Invalid Choice! Enter 1, 2, or 3.\n")
    choice = input("Rock(1), Paper(2), Scissors(3)?")

#display choice
print("\n")
player = "you"
# possible function replace
if choice == (1):
    print(player, "Chose Rock.")
elif choice == (2):
    print(player, "Chose Paper.")
elif choice == (3):
    print(player, "Chose Scissors.")
player_choice = choice

#display random choice
choice = str(random.randint(1,3))
player = "The Computer"

if choice == (1):
    print(player, "Chose Rock.")
elif choice == (2):
    print(player, "Chose Paper.")
elif choice == (3):
    print(player, "Chose Scissors.")
computer_choice = choice

# determin winner
if player_choice == computer_choice:
    print("\nNobody Wins. The Game is Drawn.")
elif player_choice == "1":
    if computer_choice == "2":
        print("\nThe Computer Wins - Paper covers Rock.")
    elif computer_choice == "3":
        print("\nYou Win!! - Rock crushes Scissors")
elif player_choice == "2":
    if computer_choice == "1":
        print("\nYou Win!! - paper covers Rock")
    elif computer_choice == "3":
        print ("\nThe Computer Wins - Scissors cut Paper")
elif player_choice == "3":
    if computer_choice == "1":
        print("\nThe Computer Wins - Rock crushes Scissors")
    elif computer_choice == "2":
        print("\nYou Win!! - Scissors cut Paper")

