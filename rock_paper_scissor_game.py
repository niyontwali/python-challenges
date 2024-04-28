import random

def get_choices(): 
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissor"]
  computer_choice = random.choice(options)
  choices = {
    "player": player_choice,
    "computer": computer_choice
  }
  return choices

def check_win(player, computer):
  print(f"You chose: {player} and computer chose: {computer}")
  if player == computer:
    return "It is a tier"
  elif player == "rock":
    if computer == "scissor": 
      return "Rock smashed scissor, You win"
    else: 
      return "Paper covers rock, You lose"
  elif player == "scissor":
    if computer == "rock": 
      return "Rock smashed scissor, You lose"
    else: 
      return "Scissor cuts paper, You win"
  elif player == "paper":
    if computer == "rock": 
      return "Paper covers rock, You win"
    else: 
      return "Scissors cuts paper, You lose"
    
choices = get_choices()
  
result = check_win(choices["player"], choices["computer"])

print(result)
    
