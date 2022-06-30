"""Project No. 3 - Nine Lives"""
import random

lives = 9
words = ['cat','syndrome','matrix','thriftless','galaxy','megahertz','luxury','brooklyn','curacao','xylophone']
secret_word = random.choice(words) # uses random module's choice() function
clue = list() # or you could write it as clue = list['?','?','?','?','?']


heart_symbol = u'\u2764'
guessed_word_correctly = False

def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter

        index += 1
#############################################################################################################
difficulty = input('Choose your level of difficulty: Enter 1 (beginner), 2 (intermediate) and 3 (expert)')
new_words = list()

for x in words:
    if difficulty=='1' and len(x)<6:
        new_words.append(x)
    if difficulty=='2'and len(x)>5 and len(x)<9:
        new_words.append(x)
    if difficulty=='3' and len(x)>8:
        new_words.append(x)

secret_word = random.choice(new_words)

for i in secret_word: ##move this
    clue.append('?')

while lives > 0:
    print(clue)
    print('Lives left: ' + heart_symbol * lives)
    guess = input('Guess a letter or the whole word ')

    if guess == secret_word:
        guessed_word_correctly = True
        break

    if guess in secret_word:
        update_clue(guess,secret_word,clue)
    else:
        print('Incorrect. You lose a life')
        lives -= 1

if guessed_word_correctly:  # if boolean is true
    print('You won! The secret word was ' + secret_word)
else:
    print('You lost! The secret words was ' + secret_word)