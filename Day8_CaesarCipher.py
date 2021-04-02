alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# from art import logo
# print(logo)
 
 
def caesar(text, shift, direction):
  encrypted_text = ""
  if shift > len(alphabet):
    shift = shift % len(alphabet)
  if direction == "decode":
    shift *= -1
  for char in text:
    if char not in alphabet:
      encrypted_text += char
    else:
      shifted_postion = alphabet.index(char) + shift
      shifted_postion_r = alphabet.index(char) + shift - len(alphabet)
      if shifted_postion < len(alphabet):
        encrypted_text += alphabet[shifted_postion]
      else:
        encrypted_text += alphabet[shifted_postion_r]
  print(f"The {direction}ed text is: {encrypted_text}")
 
 
while True:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    repeat = input(
        "Type 'yes' if you want to go again. Type 'no' if you don't want to go again\n").lower()
    if(repeat == "no"):
        print("Thanks for using Caesar Cipher!")
        break
