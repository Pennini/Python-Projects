from replit import clear

auction = {}

should_end = False
while not should_end:
  
  bidder = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))

  auction[bidder] = bid

  repeat = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if repeat == 'no':
    should_end = True
  
  clear()

higher = 0
for key, value in auction.items():
  if value > higher:
    higher = value
    person = key

print(f"The winner is {person} with a bid of ${higher}.")