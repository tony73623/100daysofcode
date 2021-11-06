import random
word_list=["Malli","Geetha","Mamatha sri","Rishi","Medha"]
chosen_word=random.choice(word_list)
print(f'choosen word is:{chosen_word}')

display=[]
word_length=len(chosen_word)
for _ in range(word_length):
    display+="_"

guess=input("guess a letter: ").lower()

for position in range(word_length):
    letter=chosen_word[position]
    if letter==guess:
        display[position]=letter
print(display)