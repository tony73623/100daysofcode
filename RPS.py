import random
user_choice=int(input("What do you choose? type 0 for rock, type 1 for paper and type 3 for scissor: "))


rock=print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper=print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissor=print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

computer_choice=random.randint(0,2)
print(f"computer chose{computer_choice}")

if (user_choice ==0 and computer_choice==1):
    print("you lose")
