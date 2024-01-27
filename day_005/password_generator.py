#Password Generator Project
import random

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\nWelcome to the PyPassword Generator!")
nr_letters= int(input("\nHow many letters would you like in your password?\n")) 
nr_symbols = int(input("\nHow many symbols would you like?\n"))
nr_numbers = int(input("\nHow many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = []

for i in range(nr_letters) :
  password += random.choice(LETTERS)

for i in range(nr_symbols) :
  password += random.choice(SYMBOLS)
  
for i in range(nr_numbers) :
  password += random.choice(NUMBERS)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random.shuffle(password)
password = "".join(password)

print(f"\nNew password: {password}\n")