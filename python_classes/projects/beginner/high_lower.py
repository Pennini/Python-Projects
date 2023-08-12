from replit import clear
from biblio import logo_highorlower, vs
from biblio import data
import random

def compare(player_choose, other):
  if player_choose["follower_count"] > other["follower_count"]:
    return True
  else:
    return False


def game(first):
  score = 0
  is_over = False

  while not is_over:
    if len(data) == 0:
      clear()
      print("You guessed all of them right! Congratulations! :)")
      break
    second = random.choice(data)
    data.remove(second)
    
    print(f"Compare A: {first['name']}, a {first['description']}, from {first['country']}\n{vs}\nAgainst B: {second['name']}, a {second['description']}, from {second['country']}")
    
    player = input("Who has more followers? Type 'A' or 'B': ").upper()
    
    if player == "A":
      answer = compare(first, second)
    elif player == "B":
      answer = compare(second, first)
    else:
      answer = False
    
    if answer:
      first = second
      score += 1
      clear()
      print(f"{logo_highorlower}\nYou're right!Current score: {score}")
    elif not answer:
      clear()
      print(f"Sorry, that's wrong. Final score: {score}")
      is_over = True


print(logo_highorlower)

first = random.choice(data)
data.remove(first)

game(first)