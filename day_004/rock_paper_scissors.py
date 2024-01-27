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

options = [rock, paper, scissors]

while True:
  player_choice = int(input(f"What do you choose? Type {options.index(rock)} for Rock, {options.index(paper)} for paper or {options.index(scissors)} for Scissors.\n"))
  if player_choice < 0 or player_choice >= len(options):
      print("\nInvalid option! Tre again.")
  else: 
    break

print(options[player_choice])

computer_choice = random.randint(0, len(options) - 1)
print(f"\nComputer chose:\n{options[computer_choice]}")

result = player_choice - computer_choice
if result == 0:
  print("There was a draw!")
elif result == 1 or result == -2:
  print("You won!")
else:
  print("You lose!")
