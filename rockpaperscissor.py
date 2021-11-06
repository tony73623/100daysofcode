import random
user_option=int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 For Scissors: "))
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

if user_option==0:
    print(rock)
elif user_option==1:
    print(paper)
else:
    print(scissors)

computer_choice=random.randint(0,2)
if computer_choice==0:
    print(rock)
elif computer_choice==1:
    print(paper)
else:
    print(scissors)

if (user_option == computer_choice):
    print("it's a draw")
elif (computer_choice>user_option):
    print("computer wins")
elif (user_option==0 and computer_choice==2 ):
    print("You Win")