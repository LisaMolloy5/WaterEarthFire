### Tutorial followed and changed for this project - 
import random

print("-------------------------------------------------------------------")
print("Welcome to Water Earth Fire!")
print("A rock, paper, scissors type game based on Avatar The Last Airbender.")
print("Use your bender abilities to defeat your oponent.")
print("--------------------------------------------------------------------")

### Game score variables

computerScore = 0
playerScore = 0
tieScore = 0

def playGame():
    """
    Function to create game combinations and playr input.
    """
    playerChoice = input("Make your choice,  Water Earth or Fire: ")
    if (playerChoice != "Water" or playerChoice != "Earth" or playerChoice != "Fire"):
        print("Invalid choice. Please try again.")

    computerChoice = random.choice(['Water', 'Earth', 'Fire'])

    if playerChoice == computerChoice:
        print("You and computer have both chosen", playerChoice, "It,s a tie.")
    
    print("Your choice: ", playerChoice, "Computer choice: ", computerChoice, "You Lost :(")

def win(player, computer):
    """
    Function to return true if the player beats the computer.
    The combinations 
    """
    if (player == "Water" and computer == "Fire") or (player == "Fire" and computer == "Earth") or (player == "Earth" and computer == "water"):
        return True
    return False

playGame()
