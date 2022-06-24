import random
from art import logo
from art import vs
from game_data import data
import replit

def random_choice(data_list):
  choice = random.choice(data_list)
  return choice


def a_or_b(choice1, choice2):
  if choice1["follower_count"] > choice2["follower_count"]:
    return choice1
  elif choice2["follower_count"] > choice1["follower_count"]:
    return choice2
  


def play_game():
  print(logo)
  score = 0
  game_end = False
  choiceA = random_choice(data)
  choiceB = random_choice(data)
  
 
  while game_end == False:
    answer = a_or_b(choiceA, choiceB)
    print(f"Choice A: {choiceA['name']} a {choiceA['description']} from {choiceA['country']}")
    print(vs)
    print(f"Choice B: {choiceB['name']} a {choiceB['description']} from {choiceB['country']}")
    user_guess = input("Who has more followers? type 'A' or 'B':\n")
    if user_guess == 'A' or user_guess == 'a':
      user_guess = choiceA["follower_count"]
    elif user_guess == 'B' or user_guess == 'b':
      user_guess = choiceB["follower_count"]
    replit.clear()
    print(logo)
         
    if user_guess == answer["follower_count"]:
      score += 1
      print(f"You are correct! your current score is {score}")
      choiceA = choiceB
      choiceB = random_choice(data)
      game_end = False
      
  
    else:
      should_restart = input(f"Thats incorrect, would you like to play again? Your final score is {score} type 'y' or 'n':\n")
      game_end = True
      if should_restart == 'y':
        replit.clear()
        play_game()
      else:
        replit.clear()
        print("Thanks for playing!")

play_game()
