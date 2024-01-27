import random
import os
import hangman as hman

STATUS_MISS = 0
STATUS_HIT = 1
STATUS_REPEATED_LETTER = -1

MAX_LIVES = 6

def get_random_word(word_list):  #
    return random.choice(word_list)
#

def check_letter_in_word(letter, word):  #
    return sum([1 for lt in word if letter == lt])
#

def clear_terminal():  #
    os.system('cls||clear')
#

def get_mistery_word(word, letters_revealed):  #
    m_word = ""
    for letter in word:
        m_word += (letter + "  ") if (letter in letters_revealed) else ("_  ")

    return m_word
#

def print_game_status(word, letters_revealed, player_live, status, last_letter):  #
    clear_terminal()
    print(f"{hman.LOGO}\n\nMistery Word:\n\n{get_mistery_word(word, letters_revealed)}\n\n{hman.HANGMANPICS[MAX_LIVES - player_live]}\nAttempts remaining: {player_live}")

    if status == STATUS_REPEATED_LETTER:
        print(f"You've already guessed \'{letter}\'! Try again.\n")
#

def reveal_a_letter(word, letters_revealed): #
    letters_list = list(word)
    while True:
        letter = random.choice(letters_list)
        if letter not in letters_revealed:
          letters_revealed.append(letter)
          return letter
#

player_live = MAX_LIVES
word = get_random_word(hman.WORD_LIST)
word_length = len(word)
hits = 0
letters_revealed = []
letters_used = []
last_status = STATUS_HIT
letter = ''
used_tip = False

while (player_live > 0 and hits < word_length):
    print_game_status(word, letters_revealed, player_live, last_status, letter)

    tip = " (tip = 0)" if (not used_tip) else ""
    letter = input(f"Guess a letter{tip}: ").lower()
    last_status = STATUS_HIT
    
  
    if str(letter).isalpha():
        if letter not in letters_used:
            check = check_letter_in_word(letter, word)
            if check > 0:
                hits += check
                letters_revealed.append(letter)
            else:
                last_status = STATUS_MISS
                player_live -= 1
        
            letters_used.append(letter)
        else:
          last_status = STATUS_REPEATED_LETTER
    elif letter == '0' and not used_tip:
      used_tip = True
      hits += check_letter_in_word(
                    reveal_a_letter(word, letters_revealed),
                    word)

print_game_status(word, letters_revealed, player_live, last_status, letter)
if player_live > 0:
  print("\nCongratulations! YOU WIN!\n\n")
else:
  print(f"\nYOU LOSE!\nThe mystery word was \"{word}\".\n")