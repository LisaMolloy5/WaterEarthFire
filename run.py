### Tutorial followed and changed for this project - 
import random

print("-------------------------------------------------------------------")
print("Welcome to Water Earth Fire!")
print("A rock, paper, scissors type game based on Avatar The Last Airbender.")
print("Use your bender abilities to defeat your oponent.")
print("--------------------------------------------------------------------")

### Game score variables

gameChoices = ["Water", "Earth", "Fire"]

def hasWon(playerChoice, computerChoice):
    """
    """      
    if (playerChoice == "Water" and computerChoice == "Fire") or (playerChoice == "Fire" and computerChoice == "Earth") or (playerChoice == "Earth" and computerChoice == "Water"):
        print("Yay! You won :D")
        return "Player"
    elif (playerChoice == "Fire" and computerChoice == "Water") or (playerChoice == "Earth" and computerChoice == "Fire") or (playerChoice == "Water" and computerChoice == "Earth"):
        print("Sorry, you lost. :(")
        return "Computer"
    elif (playerChoice == computerChoice):
        print("It's a Tie")
        return "Tie"
    else:
        print("Invalid input. Try again.")

while True:
    playerChoice = input("\n Enter your choice. Water Earth or Fire: ")

    computerChoice = random.choice(gameChoices)

    print("Your choice: ", playerChoice)
    print("Computer choice: ", computerChoice)

    result = hasWon(playerChoice, computerChoice)

    if(result == "Player"):
        playerScore += 1
    elif(result == "Computer"):
        computerScore += 1
    elif(result == "Tie"):
        tieScore += 1



                



