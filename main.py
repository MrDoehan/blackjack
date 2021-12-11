import random
king = 10
queen = 10
jack = 10
ace = 1
cards = ["no", ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, jack]
card1 = random.randint(1, 11)
card2 = random.randint(1, 11)

global pcard
pcard = card1 + card2
print(f"This is a game of blackjack where the goal is to get as close to 21 as possible without going over 21.")
print(f"You got a {cards[card1]} and a {cards[card2]}. Your total is {pcard}")

card3 = random.randint(1, 11)
card4 = random.randint(1, 11)
ccard = card3 + card4
card10 = random.randint(1, 11)
card11 = random.randint(1, 11)
card12 = random.randint(1, 11)
card13 = random.randint(1, 11)
card20 = random.randint(1, 11)
player = [card10, card11, card12, card13]
move = input("hit/stand? ")
while move != "stand":
  
  if move == "hit":
    
    pcard = pcard + cards[random.randint(1, 11)]
    print(f"Your new total is {pcard}")  
    move = input("hit/stand? ")
    if ccard < 17:
      ccard = ccard + card20
if move == "stand":
  print(f"Your total is {pcard}")
  if pcard > 21:
    print("You got over 21, you busted.")  
  elif ccard > 21:
    print(f"Your opponent got a score of {ccard} and busted.")
  elif ccard > pcard:
    print(f"The opponent got a total of {ccard}. Your opponent beat you.")
  elif pcard > ccard:
    print(f"The opponent got a total of {ccard}. You won")
  else:
    print("no")   