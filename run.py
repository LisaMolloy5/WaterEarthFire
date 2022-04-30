### Tutorial followed and changed for this project - 
import random

print("-------------------------------------------------------------------")
print("Welcome to Water Earth Fire!")
print("A rock, paper, scissors type game based on Avatar The Last Airbender.")
print("Use your bender abilities to defeat your oponent.")
print("--------------------------------------------------------------------")


def hasWon(playerChoice, computerChoice):
    """
    """      
    if (playerChoice == "Water" and computerChoice == "Fire") or (playerChoice == "Fire" and computerChoice == "Earth") or (playerChoice == "Earth" and computerChoice == "Water"):
        print("YOU WON! :D")
    elif (playerChoice == "Fire" and computerChoice == "Water") or (playerChoice == "Earth" and computerChoice == "Fire") or (playerChoice == "Water" and computerChoice == "Earth"):
        print("YOU LOST :(")
    elif (playerChoice == computerChoice):
        print("TIE!")
    else:
        print("Invalid input. Try again.")

while True:
    playerChoice = input("Enter your choice. Water Earth or Fire: ")

    computerChoice = random.choice(["Water", "Earth", "Fire"])

    print("Your choice: ", playerChoice)
    print("Computer choice: ", computerChoice)

    hasWon(playerChoice, computerChoice)

    play_again = input("Play again? yes/no: ").lower()

    if play_again != "yes":
        break

print("Bye, Thanks for playing")


                



