# user has 7 guesses to get a word correct. For incorrect guess, hangman loses a life.For correct guesses, game proceeds, FOR REPEATED guesses, game reminds you to try something else.


import random

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

import hangman_words
#else write as "from hangman_words import word_list" and chosen_word becomes random.choice(word_list)
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 7

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
import hangman_art
# else write above as "from hangman_arts import logo",then the next print function could be print(logo)
print(hangman_art.logo)
#Testing code
print(f"The chosen word has {word_length} letters")
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"


while end_of_game is False:
  guess = input("Guess a letter: ").lower()

#     #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
  if guess in display:
   
   print("This has already been guessed, please try again")
  else:
    #Check guessed letter
    for position in range(word_length):
      letter = chosen_word[position]

      if letter == guess:
        display[position] = letter
       
#     #Check if user is wrong.
#     if guess not in chosen_word:
 

#         #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
  if guess not in chosen_word:
     print(f"{guess} is not there in our word.Please try again")
     lives -= 1
     print(hangman_art.stages[lives])
     if lives == 0:
       end_of_game = True
       print(f"You lose.The actual word was {chosen_word}")


#     #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")

#     #Check if user has got all letters.
  if "_" not in display:
    end_of_game = True
    print("You win.")

#     #TODO-2: - Import the stages from hangman_art.py and make this error go away.
