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
    playerChoice = input("Enter your choice. Water Earth or Fire:\n")

    computerChoice = random.choice(["Water", "Earth", "Fire"])

    print("Your choice: ", playerChoice)
    print("Computer choice: ", computerChoice)

    hasWon(playerChoice, computerChoice)

    play_again = input("Play again? yes/no:\n").lower()

    if play_again != "yes":
        break

print("Bye, Thanks for playing")


                



