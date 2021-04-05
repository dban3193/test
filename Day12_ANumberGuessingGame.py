import random
from art import logo
print(logo)

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 to 100")
level=input("Choose a difficulty? 'easy','medium' or 'hard'? ").lower()
number= random.randint(1,100)


def game_play(level):
  if level == "easy":
   LIFE_ASSIGNED = 10
  elif level == "medium":
   LIFE_ASSIGNED = 7
  elif level == "hard":
   LIFE_ASSIGNED = 5
  
  for i in range(LIFE_ASSIGNED):
    print(f"You have {LIFE_ASSIGNED} attempts remaining to guess the number.")
    number_guess=int(input("Make a guess: "))
    if number_guess < number:
     print("Too Low!\nGuess Again!")
     LIFE_ASSIGNED-=1
    elif number_guess > number:
     print("Too High!\nGuess Again!")
     LIFE_ASSIGNED-=1
    else:
     print(f"You got it! The answer was {number}.")
     break
  if LIFE_ASSIGNED ==0 and number_guess!=number:
    print(f"You've run out of guesses, you lose. The actual number was {number}")

game_play(level)
