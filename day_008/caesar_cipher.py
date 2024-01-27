alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#e.g.
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"

##HINT: How do you get the index of an item in a list:
#https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛


def get_encypted_letter(letter: str, shift: int):
    index = alphabet.index(letter)
    index += shift

    alphabet_size = len(alphabet)

    while index > alphabet_size:
        index -= alphabet_size
    while index < 0:
        index += alphabet_size

    return index


def aply_caesar_cipher(text: str, shift: int, encript = True):
    text = text.lower()
    encrypted_text = ""

    if not encript:
        shift = -shift

    for letter in text:
        if letter.isalpha():
            encrypted_text += alphabet[get_encypted_letter(letter.lower(), shift)]
        else:
            encrypted_text += letter

    print(encrypted_text)


def encrypt(text: str, shift: int):
    aply_caesar_cipher(text, shift)


def decrypt(text: str, shift: int):
    aply_caesar_cipher(text, shift, False)


#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

if direction == "encode":
    encrypt(text, shift)
else:
    decrypt(text, shift)
