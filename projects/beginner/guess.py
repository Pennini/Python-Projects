import random

range_game = int(input("What it's the range of the game?"))

computer = random.randint(1, range_game)
print(computer)


def compare(guess, answer):
    if guess > answer:
        return "Too high."
    elif guess < answer:
        return "Too low."
    else:
        return 0


difficulty = input(
    f"I'm thinking of a number between 1 and {range_game}.\nChoose a difficulty. Type 'easy' or 'hard': "
).lower()
while difficulty != "easy" and difficulty != "hard":
    difficulty = input("Please choose a difficulty. 'easy' or 'hard': ")

if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number")
    guess_player = int(input("Make a guess: "))

    result = compare(guess_player, computer)

    if result == 0:
        break
    else:
        print(result)
        attempts -= 1

if result == 0:
    print(f"You got it! The number was {computer}")
else:
    print(f"You've run out of guesses, you lose. The number was {computer}")
