import random
import hangman_words
import hangman_art
print(hangman_art.logo)
display=[]
game_end=False
lives=6
choosen_word=random.choice(hangman_words.words_list)
print(f'You Choosen Solution is : {choosen_word}')
for _ in range(len(choosen_word)):
    display+="_"
while not game_end:
    guess_word=input("Guess a Letter:").lower()
    if guess_word in display:
        print(f'The Letter {guess_word} Already Selected')
    for location in range(len(choosen_word)):
        letter=choosen_word[location]
        if letter==guess_word:
            display[location]=letter
            print(display)

    if guess_word not in choosen_word:
        print(f'Your Guess Letter Not Match! You Loose a life')
        lives-=1
        print(hangman_art.stages[lives])    

    if lives==0:
        game_end=True
        print("You Loose")
    if "_" not in display:
        game_end=True
        print("You Win")