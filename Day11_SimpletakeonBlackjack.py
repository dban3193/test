import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#sumofcards=0
def add_a_card_for_user():
    new_card=random.choice(cards)
    user_cards.append(new_card)
    return new_card

def add_a_card_for_computer():
    new_card=random.choice(cards)
    computer_cards.append(new_card)
    return new_card

def print_stuff():
  print(f"Your cards: {user_cards},current score: {sum_for_user}")
  print(f"Computer's first card :{computer_cards[0]}")

def final_print():
  print(f"Your final hand :{user_cards}, final score :{sum_for_user}")
  print(f"Computer's final hand :{computer_cards}, final score :{sum_for_computer}")

def compare(sum_for_user,sum_for_computer):
  final_print()
  if sum_for_user < sum_for_computer and sum_for_computer <=21:
      return print("You lose!")
  elif sum_for_computer < sum_for_user and sum_for_user <=21:
      return print("You win!")
  elif sum_for_computer > 21:
       return print("Computer went over! You win!")
  elif sum_for_user > 21:
       return print("You went over! You Lose!")
  elif sum_for_computer == sum_for_user:
       return print("This game is a Draw!")
  elif sum_for_computer >21 and sum_for_user >21:
       return print("This match is a Draw")

want_to_play=input("Do you want to play a game of Blackjack? Type 'y' or 'n' :" )
if want_to_play == "y":
  user_cards = []
  computer_cards = []
  sum_for_user=0
  sum_for_computer=0
  sum_for_user=add_a_card_for_user()+add_a_card_for_user()
  sum_for_computer=add_a_card_for_computer()+add_a_card_for_computer()
  print_stuff()
  if sum_for_user > 20 and sum_for_user < 22:
    final_print()
    print("Blackjack won by user!")
  elif sum_for_computer > 20 and sum_for_computer < 22:
    final_print()
    print("Blackjack won by computer!")
  elif sum_for_computer ==21 or sum_for_user == 21 or sum_for_computer ==22 or sum_for_user ==22:
    final_print()
    print("The game is a DRAW!")
  else:    
   should_continue=input("do you want to play another hand? Type 'y' for yes and 'n' for no :")
   if should_continue == "y":
    sum_for_user+=add_a_card_for_user()
    if sum_for_computer < 16:
      sum_for_computer+=add_a_card_for_computer()
    if sum_for_user < 16:
      # print_stuff()
      # should_continue = "y"
      sum_for_user+=add_a_card_for_user()
      # final_print()
    # if sum_for_computer >= 21 or sum_for_user >=21:
    #   final_print()

    compare(sum_for_user,sum_for_computer)    
      
   elif should_continue == "n":
    if sum_for_computer < 16:
      sum_for_computer+=add_a_card_for_computer()
    print(f"Your final hand :{user_cards}, final score :{sum_for_user}")
    print(f"Computer's final hand :{computer_cards}, final score :{sum_for_computer}")
    compare(sum_for_user,sum_for_computer) 
else:
  print("That's all from the Game!")     
