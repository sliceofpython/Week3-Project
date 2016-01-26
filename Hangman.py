#!python3

'''
Hangman
chra94
'''

import random

wordList = ['money', 'england', 'snow', 'lime', 'citron', 'police', 'washington', 'pc', 'computer', 'ambulance', 'tower', 'python', 'education'] #List of words for Hangman
secretWord = wordList[random.randint(0, (len(wordList)-1))] #Selects random word from list
correctGuess = []
for i in secretWord:
    correctGuess.append('_')
wrongGuess = []
wrongGuesses = 0
print('Welcome to hangman. You are going to figure out what the secret word is by guessing letters. You can guess wrong 10 times.')
print('The word has this many letters : ' + str(correctGuess))
print(correctGuess)
while wrongGuesses <= 9: #and '-' in correctGuess: #Until 10 wrong guesses by user or word guessed
    guess = input('Guess a letter.\n') #Makes the user guess a letter.
    n = -1
    for i in secretWord:
        n += 1
        if guess == i:
            correctGuess[n] = guess
            print(correctGuess)

    if guess in wrongGuess:
        print('Already guessed.')
    elif guess not in secretWord:
        print('Wrong')
        wrongGuess.append(guess)

        print('Letters not in the word: ' + str(wrongGuess))
        wrongGuesses += 1
        print('Guesses left: ' + str(10 - wrongGuesses))

    if '_' not in correctGuess:
        break

if '_' not in correctGuess:
    print('You won!')
else:
    print('You lost :( \n'
          'The word was: ' + str(secretWord) + '.')
