from art import logo
import random
import replit

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
  card = random.choice(cards)
  return card

def calculate_score(list_of_cards):
  score = sum(list_of_cards)
  if score == 11 + 10:
    score = 0
  elif score >= 21:
    if 11 in list_of_cards: 
      list_of_cards.remove(11)
      list_of_cards.append(1)
  return score


def compare(score_computer, score_user):
  if score_computer == score_user:
    result = "Its a draw!"
    return result
  elif score_computer == 0:
    result = "computer has blackjack, you lose."
    return result
  elif score_computer != 0 and score_user == 0:
    result = "user has blackjack, you win"
    return result
  elif score_user > 21:
    result = "Youre over 21, you lose"
    return result
  elif score_computer > 21:
    result = "computer has over 21, you win."
    return result
  elif score_computer > score_user:
    result = "computer has higher score, you lose"
    return result
  elif score_user > score_computer:
    result = "Your score is higher, you win!"
    return result



def play_game():
  print(logo)
  user_cards = []
  computer_cards = []

  user_card1 = int(deal_card())
  user_card2 = int(deal_card())
  user_cards.extend([user_card1, user_card2])
  print(f"users cards: {user_cards}")



  computer_card1 = int(deal_card())
  computer_card2 = int(deal_card())
  computer_cards.extend([computer_card1, computer_card2])
  print(f"computers first card: {computer_cards[0]}")
  
  game_not_ended = True

  while game_not_ended:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your score is: {user_score}")   


    if game_not_ended == True:
      draw_again = input("Would you like to draw another card? Type 'yes' or 'no'\n")
      if draw_again == "yes":
        user_card3 = int(deal_card())
        user_cards.append(user_card3)
        user_score = calculate_score(user_cards)
      elif draw_again == "no":
        user_score = calculate_score(user_cards)
        game_not_ended = False
        if computer_score != 0 and computer_score < 17:
          computer_card = deal_card()
          computer_cards.append(computer_card)
        computer_score = calculate_score(computer_cards)
        comparison = compare(computer_score, user_score)
        print(computer_score)
        print(comparison)
        play_again = input("would you like to play again? type 'yes' or 'no'\n")
        if play_again == "yes":
          replit.clear()
          play_game()


    



play_game()
