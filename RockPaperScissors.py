import random

BotScore = 0
PlayerScore = 0

player = input("rock, paper, scissors or quit?")

Options = ["rock","paper","scissors"]


while player != 'quit':

  choice = random.choice(Options)
  if player == "rock":
    print (choice)
    if choice == "paper":
      BotScore = BotScore + 1
      print ("I win this round!")
    if choice == "scissors":
      PlayerScore = PlayerScore + 1
      print ("You win this round!")
    if choice == "rock":
      print ("This round is a tie!")

  if player == "paper":
    print (choice)
    if choice == "paper":
      print ("This round is a tie!")
    if choice == "scissors":
      BotScore = BotScore + 1
      print ("I win this round!")
    if choice == "rock":
      PlayerScore = PlayerScore + 1
      print ("You win this round!")

  if player == "scissors":
    print (choice)
    if choice == "scissors":
      print ("This round is a tie!")
    if choice == "rock":
      BotScore = BotScore + 1
      print ("I win this round!")
    if choice == "paper":
      PlayerScore = PlayerScore + 1
      print ("You win this round!")
  player = input("rock, paper, scissors or quit?")

print("Player score = "+str(PlayerScore))
print("Bot score = "+ str(BotScore))
if PlayerScore > BotScore:
  print("You win!")
elif BotScore > PlayerScore:
  print("I win!")
else :
  print("It's a tie!")