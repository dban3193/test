#Here we provide a list of names separated by commas, which is passed to a list. Then a random person is chosen out of the list who pays the hotel bill.
import random
names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")
#split function splits incoming data based on a delimiter
print(names)
#prints the list created

random_person_no=random.randint(0,len(names)-1)
#using randint() get a random index number chosen from names list and pass it to random_person_no. Subtracting len(names) by 1 since counting starts from 0
random_person=names[random_person_no]
#get the corresponding index value and store it in random_person
print(f"{random_person} is going to buy the meal today.")

#Alternatively
#using choice() directly which chooses a random item from alist.
#steps 9,11 wont be needed
#random_person=random.choice(names)

