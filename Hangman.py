#!python3

'''
Hangman
chra94
'''

import random


def main():
    win = False
    wordList = ['money', 'snow', 'lime', 'citron', 'police', 'computer', 'ambulance', 'tower', 'education',] #List of words for Hangman
    secretWord = wordList[random.randint(0, (len(wordList)-1))] #Selects random word from list
    correctGuess = ''
    for i in secretWord:
        correctGuess += '_ '
    wrongGuess = ''
    wrongGuesses = 0
    print('Welcome to hangman. You are going to figure out what the secret word is by guessing letters. You can guess wrong 10 times.')
    print('Secret word: ' + str(correctGuess))
    while wrongGuesses <= 9: #and '-' in correctGuess: #Until 10 wrong guesses by user or word guessed
        guess = input('Guess a letter.\n') #Makes the user guess a letter.
        n = -2
        if guess == secretWord:
            win = True
            break
        
        for i in secretWord:
            n += 2
            if guess == i:
                correctGuess = correctGuess[:n] + guess + correctGuess[n+1:]
        print(correctGuess)

        if guess in wrongGuess or guess == correctGuess:
            print('Already guessed.')
        elif guess not in secretWord:
            print('Wrong')
            wrongGuess += guess
            
            print('Letters not in the word: ' + str(wrongGuess))
            wrongGuesses += 1
            print('Guesses left: ' + str(10 - wrongGuesses))

        if '_' not in correctGuess:
            break

    if '_' not in correctGuess or win:
        print('You won!')
    else:
        print('You lost :( \n'
              'The word was: ' + str(secretWord) + '.')
    while True:
        replay = input('Replay? yes/no')
        if replay == 'yes':
            print('')
            main()
        elif replay == 'no':
            print('Goodbye')
            break
    
main()
