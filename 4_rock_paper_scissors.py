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

game_options = [rock, paper, scissors]
computer_choice_logic = random.randint(0, 2)
computer_choice = game_options[computer_choice_logic]

human_choice = int(input("What do you choose? \nType 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))

# Display choices
print(f"You chose:\n{game_options[human_choice]}")
print(f"Computer chose:\n{computer_choice}")

# Game logic
if human_choice < 0 or human_choice > 2:
    print("Invalid choice. You lose!")
else:
    if human_choice == computer_choice_logic:
        print("It's a draw!")
    elif human_choice == 0 and computer_choice_logic == 2 or \
         human_choice == 1 and computer_choice_logic == 0 or \
         human_choice == 2 and computer_choice_logic == 1:
        print("You win!")
    else:
        print("You lose!")
