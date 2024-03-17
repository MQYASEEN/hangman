import random
import hangman_words
import hangman_art
print(hangman_art.logo)
display=[]
choosen_word=random.choice(hangman_words.words_list)
print(f'You Choosen Solution is : {choosen_word}')
for _ in range(len(choosen_word)):
    display+="_"
print(display)
game_end=False
while not game_end:
    guess_word=input("Guess a Letter:").lower()
    for location in range(len(choosen_word)):
        letter=choosen_word[location]
        if letter==guess_word:
            display[location]=letter
            print(display)
if "_" not in display:
    game_end=True
    print("You Win")
