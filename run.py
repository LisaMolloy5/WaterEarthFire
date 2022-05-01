### Tutorial followed and changed for this project - 
import random

print("-------------------------------------------------------------------")
print("Welcome to Water Earth Fire!")
print("A rock, paper, scissors type game based on Avatar The Last Airbender.")
print("--------------------------------------------------------------------")
print("HOW TO PLAY:")
print("Can you use your bending abilities to defeat your opponent?")
print("Water Beats Fire")
print("Fire Beats Earth")
print("Earth Beats Water")
print("Good Luck :D")

computerScore = 0
playerScore = 0
tieScore = 0


def hasWon(playerChoice, computerChoice):
    """
    """      
    if (playerChoice == "Water" and computerChoice == "Fire") or (playerChoice == "Fire" and computerChoice == "Earth") or (playerChoice == "Earth" and computerChoice == "Water"):
        print("YOU WON! :D")
        return "Player"
    elif (playerChoice == "Fire" and computerChoice == "Water") or (playerChoice == "Earth" and computerChoice == "Fire") or (playerChoice == "Water" and computerChoice == "Earth"):
        print("YOU LOST :(")
        return "Computer"
    elif (playerChoice == computerChoice):
        print("TIE!")
        return "Tie"
    
def newGame():
    while (playerScore != 3 and computerScore != 3):

        while True:
            playerChoice = input("Make your choice: Water, Fire or Earth...")
            if (playerChoice == "Water" or playerChoice == "Fire" or playerChoice == "Earth"):
                break
            else:
                print("Invalid Input. Try Again...")
        
        computerChoice = random.choice(["Water", "Fire", "Earth"])

        print("Your Choice: ", playerChoice)
        print("Computer choice: ", computerChoice)
        result = hasWon(playerChoice, computerChoice)

        if (result == "Player"):
            playerScore += 1
        elif (result == "Computer"):
            computerScore += 1
        else:
            tieScore += 1

        print("Your Score:", playerScore, "...Computer Score:", computerScore, "...Tie Score:", tieScore)  

def endGame():
    if (playerScore == 3):
        print("CONGRATULATIONS! You Won The Game")
    elif (computerScore == 3):
        print("Sorry! You Lost The Game.")

    playAgain = input("Play Again? yes/no...")

    if (playAgain == yes):
        hasWon(playerChoice, computerChoice)
        resetGame()

def resetGame():
    computerScore = 0
    playerScore = 0
    tieScore = 0

    newGame()


endGame()
      



