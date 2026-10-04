import random

word_list = ["goat", "money", "camel"]

word_list = random.choice(word_list)
print(word_list)

guess = input("Guess a letter:").lower()
print(guess)

display = ""

for letter in word_list:
   if letter == guess:
       display += letter
   else:
       display += "-"
       
display

placeholder = ""
for positions in range(1,6):
    placeholder += "-"
    
print(placeholder)

game_over = False

while not game_over:
    guess = input("Guess a letter:"). lower

display += "-"

if "-" not in display:
    game_over = True
    print("You win.")


