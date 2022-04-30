### Tutorial followed and changed for this project - https://www.youtube.com/watch?v=xRlN8CFJwAM&t=175s
import random

print("-------------------------------------------------------------------")
print("Welcome to Water Earth Fire")
print("A rock, paper, scissors type game based on Avatar The Last Airbender.\n Use your abilities to defeat your oponent.")
print("--------------------------------------------------------------------")

playerScore = 0
computerScore = 0
tieScore = 0

def playGame():
    """
    Function to create game combinations and playr input.
    """
    playerChoice = input("Make your choice,  Water Earth or Fire: ")
    if (playerChoice != "Water" or playerChoice != "Earth" or playerChoice != "Fire"):
        return False
        print("Invalid choice. Please try again.")

    computerChoice = random.choice(['Water', 'Earth', 'Fire'])

    if playerChoice == computerChoice:
        print("You and computer have both chosen", playerChoice "It,s a tie.")


    


