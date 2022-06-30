"""Project No. 3 - Nine Lives

adding levels of difficult
level 1 - word length 5 and less
level 2 - word length 6 -9
level 3 -word length 10 and up

making the game smarter
the game will end once the last letter is typed in

"""
import random

lives = 9
words = ['cat','syndrome','matrix','thriftless','galaxy','megahertz','luxury','brooklyn','curacao','xylophone','mississippi']
secret_word = random.choice(words) # uses random module's choice() function
clue = list() # or you could write it as clue = list['?','?','?','?','?']
heart_symbol = u'\u2764'
guessed_word_correctly = False
difficulty = input('Choose your level of difficulty: Enter 1 (beginner), 2 (intermediate) and 3 (expert)')
new_words = list()

for x in words:
    if difficulty=='1' and len(x)<6:
        new_words.append(x)
        lives = 5
    if difficulty=='2'and len(x)>5 and len(x)<9:
        new_words.append(x)
        lives = 9
    if difficulty=='3' and len(x)>8:
        new_words.append(x)
        lives = 13
secret_word = random.choice(new_words)

remaining_letters = len(secret_word)


def update_clue(guessed_letter, secret_word, clue, hidden_letters):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
            hidden_letters -= 1 ## one less hidden letter remains
        index += 1
    return hidden_letters # returns an integer when function is called3
#############################################################################################################



for i in secret_word: ##populate clue list with question mark
    clue.append('?')

while lives > 0:
    print(clue)
    print('Lives left: ' + heart_symbol * lives)
    guess = input('Guess a letter or the whole word ')

    if guess == secret_word:
        guessed_word_correctly = True
        break

    if guess in secret_word:
        remaining_letters=update_clue(guess,secret_word,clue,remaining_letters)
    else:
        print('Incorrect. You lose a life')
        lives -= 1

    if remaining_letters == 0:
        guessed_word_correctly=True
        break

if guessed_word_correctly:  # if boolean is true
    print('You won! The secret word was ' + secret_word)
else:
    print('You lost! The secret words was ' + secret_word)