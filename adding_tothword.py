chosen_word=input("choose a word:")
print(f"Psst, the solution is {chosen_word}")
display=[]
for letter in chosen_word:
    display+="_"
print(display)
end_of_game=False
while end_of_game==False:
    guess=input("guess the letter:").lower()
    for position in range (len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter

    print(display)
if "_" not in display:
    end_of_game-True
    print("You Win")

