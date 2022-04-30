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

gameChoices = ["Water", "Earth", "Fires"]

def hasWon(playerChoice, computerChoice):
    """
    """      
    if (playerChoice == "Water" and computerChoice == "Fire") or (playerChoice == "Fire" and computerChoice == "Earth") or (playerChoice == "Earth" and computerChoice == "Water"):
        print("Yay! You won :D")
        return "Player"
    elif (playerChoice == "Fire" and computerChoice == "Water") or (playerChoice == "Earth" and computerChoice == "Fire") or (playerChoice == "Water" and computerChoice == "Earth"):
        print("Sorry, you lost. :(")
        return "Computer"
    else:
        print("It's a tie.")
        return "Tie"

while (playerScore != 3 and computerScore != 3):

    while True:
        playerChoice =  input("\n Choose Water, Earth of Fire: ")
        if (playerChoice == "Water" or playerChoice == "Earth" or playerChoice == "Fire"):
            break
        else:
            print("Invalid input. Try again")
    
    computerChoice = random.choice(gameChoices)

    print("Your choice: ", playerChoice)
    print("Computer choice: ", computerChoice)
    result = hasWon(playerChoice, computerChoice)
    if(result == "Player"):
        playerScore += 1
    elif(result == "Computer"):
        computerScore += 1
    else:
        tieScore += 1
    print("Your score: ", playerScore, "Computer: ", computerScore, "Ties: ", tieScore)


