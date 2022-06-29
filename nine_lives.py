"""Project No. 3 - Nine Lives"""
import random

lives = 9
words = ['syndrome','matrix','thriftless','galaxy','megahertz','luxury','brooklyn','curacao','xylophone']
secret_word = random.choice(words) # uses random module's choice() function
clue = list() # or you could write it as clue = list['?','?','?','?','?']
for i in secret_word:
    clue.append('?')




heart_symbol = u'\u2764'
guessed_word_correctly = False

def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter

        index += 1

print(secret_word)
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