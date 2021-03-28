#here user enters an option between 0-2 and computer enters between 0-2 randomly.We have a nested list containing variables rock paper and scissors with their ascii images.Based on
#user input and computer input its decided if you win or lose.

import random
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

code=int(input("What do you choose?Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))

if code > 2 or code < 0:
  print("Incorrect Option chosen, please choose 0/1/2") 
else:
  options=[rock,paper,scissors]
  print(options[code])
  comp=random.randint(0,2)
  if comp==0:
    print(f"Computer chose:{rock}")
 # comp_choice=rock
  elif comp==1:
    print(f"Computer chose:{paper}")
 # comp_choice=paper
  elif comp==2:
    print(f"Computer chose:{scissors}")
  #comp_choice=scissors
#deciding on fate
# print(code)
# print(comp)
  if code == comp:
   print("It's a draw.Play again!")
  if code ==1 and comp == 0:
   print("You Win.Paper beats rock")
  elif code == 1 and comp ==2:
   print("You Lose.Scissors cut paper")
  elif code == 0 and comp ==1:
   print("You Lose.Paper beats rock")
  elif code ==0 and comp==2:
   print("You win.Rock wins over scissors!")
  elif code==2 and comp==0:
   print("You Lose.Rock wins over scissors!")
  elif code==2 and comp==1:
   print("You Win.Scissors cut paper")
