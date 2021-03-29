import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#this is easy password generation step where occurence knd is predictable
# password=''

# for n in range(1,nr_letters+1):
#   password+=random.choice(letters)

# for n in range(1,nr_symbols+1):
#   password+=random.choice(symbols)

# for n in range(1,nr_numbers+1):
#   password+=random.choice(numbers)    

# print(f"Your password could be: {password}")  



# this is the practical one, where occurence could be random
password1=[]

for n in range(1,nr_letters+1):
  password1.append(random.choice(letters))

for n in range(1,nr_symbols+1):
  password1.append(random.choice(symbols))

for n in range(1,nr_numbers+1):
  password1.append(random.choice(numbers))


pass1 = ''
print(password1)
random.shuffle(password1)  
for n in password1:
  pass1 +=n
print(f"A random password based on choices would be: {pass1}")
