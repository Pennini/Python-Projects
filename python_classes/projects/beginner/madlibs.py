sentence = "After giving %s to my %s mother. I'm going to the %s and then I'm going to buy %s before I get home, but I need to withdraw %s dollars from the bank for that"
things = ["food","adjective", "place", "object", "number"]
food, adj, place, obj, num =  [input(f"Give me a(n) {i}: ") for i in things]
print(sentence % (food, adj, place, obj, num))