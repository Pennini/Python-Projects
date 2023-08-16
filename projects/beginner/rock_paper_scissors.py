from biblio import rock, paper, scissors
import random

images = [rock, paper, scissors]

player = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors. ")
)
if player >= 3 or player < 0:
    print("You typed an invalid number, you lose!")
else:
    print(f"You chose: {images[player]}")
    computer = random.randint(0, 2)
    print(f"Computer chose:\n{images[computer]}")
    result = player - computer

    if result == -1 or result == 2:
        print("You lose")
    elif result == 1 or result == -2:
        print("You win!")
    else:
        print("You draw")
