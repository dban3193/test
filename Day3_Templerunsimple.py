print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

print("This is a take on Temple run game")
print("You are being followed by a Huge orangutan in a jungle!!!!")
choice1=input("You have a crossroad, what do you choose:left or right?").lower()
if choice1 == "right":
  print(" You are cornered in front of a steep mountain! Dude you are dead. orangutan tears you too pieces!GAME OVER!-_-")
elif choice1 == "left":
  print("You come across a fast flowing stream.")
  choice2=input("You have 2 alternatives, you can either swim or find a woodlog?").lower()
  if choice2 == "wood":
   print("Excellent, you cross the stream slowly leaving the orangutan howl in anger!!")
   print("After going for sometime you spot a castle, almost a torn building now")
   choice3=input("You see 3 doors in front of you!Red, Yellow and Green, you gotta choose one!").lower()
   if choice3 == "yellow":
     print("You got the pot of Gold. You win the treasure! Congratulations!!!")
   elif choice3 == "green":
     print("An angry rhinoceros comes in and blends you like a paste under it's hooves! GAME OVER!")
   elif choice3 =="red":
     print(" Red hot fire engulfs you not leaving even a shred of your existence.GAME OVER!")
   else:
     print("Incorrect option chosen, please choose either red, yellow or green door")
  elif choice2 == "swim":
    print("Dude you drowned, you cannot swim in such fast paced water even if you were Phelps!GAME OVER!")
  else:
    print("Incorrect option chosen, you can either swim or grab a wooden branch")
else:
  print("Incorrect option chosen, you can only go left or right")
