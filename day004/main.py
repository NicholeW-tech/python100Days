rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random
computer_choice = random.randint(0, 2)
player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n") 

if player_choice == "0":
  print(rock + "\nplayer chooses rock")
  if computer_choice == 0:
    print(rock + "\nComputer chooses rock, it's a tie!")
  elif computer_choice == 1:
    print(paper + "\nComputer chooses paper, You lose. Better luck next time!")
  elif computer_choice == 2:
    print(scissors + "Computer chooses scissors, You win!")
elif player_choice == "1":
  print(paper + "\nplayer chooses paper")
  if computer_choice == 0:
    print(rock + "\nComputer chooses rock, You win!")
  elif computer_choice == 1:
    print(paper + "\nComputer chooses paper, it's a tie!")
  elif computer_choice == 2:
    print(scissors + "Computer chooses scissors, You lose. Better luck next time!")
elif player_choice == "2":
  print(scissors + "\nplayer chooses scissors")
  if computer_choice == 0:
    print(rock + "\nComputer chooses rock, You lose. Better luck nect time!")
  elif computer_choice == 1:
    print(paper + "\nComputer chooses paper, You win!")
  elif computer_choice == 2:
    print(scissors + "Computer chooses scissors, it's a tie!")
else:
  print("invalid selection choose a number between 0 -2")

