import random
word_list = ["yemen", "apple", "orange"]
lives = 6
# Using the random module to choose a word
chosen_word = random.choice(word_list)
print(chosen_word)

# generate blanks to the blank list
blank_list = []
for i in range(len(chosen_word)):
    blank_list += '_'
print(blank_list)
game_over = False
# Asking the user to guess a letter
while not game_over:
    guessed_letter = input("Guess a letter: ")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            blank_list[position] = guessed_letter
    print(blank_list)
    if guessed_letter not in chosen_word:
        lives -= 1
    if lives == 0:
        game_over = True
        print("You Lost!")
    if '_' not in blank_list:
        game_over = True
        print("You Won")




