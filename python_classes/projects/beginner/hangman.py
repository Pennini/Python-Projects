from biblio import stages, hangman_logo, word_list
import random

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_logo)
# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"
guesses = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    while len(guess) != 1:
        guess = input("Guess only one letter: ").lower()

    while guess in guesses:
        guess = input(f"You have already guessed letter {guess}: ").lower()

    guesses.append(guess)
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"Letter {guess} is not in the word")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lost, the word was {chosen_word}")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
