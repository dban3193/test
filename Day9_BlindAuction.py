bids_made = {}
from art import logo
print(logo)
print("Welcome to Yearly Blind Auction!")
bid_switch = True
while bid_switch is True:
  name = input("What is your name? :")
  bid_amount = input("What is the amount you would like to bid? $")
  bids_made[name] = bid_amount
  should_continue= input("Is there anyone else who would like to bid, answer yes or no :").lower()
  if should_continue == "yes":
#      clear()
      bid_switch = True
  else:
    bid_switch = False
    #print(" The auction has ended")
#    clear()
    initial_amount = 0
    for winner in bids_made:
      
      bid_amount_int=int(bids_made[winner])
      if bid_amount_int > initial_amount:
         initial_amount = bid_amount_int
         winner_blind = winner
    print(f"The winner is {winner_blind} and the bid amount is $ {initial_amount}")    
