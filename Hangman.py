#!python3

'''
Hangman
chra94
'''

import random


def main():
    win = False
    wordList = ['money', 'snow', 'lime', 'citron', 'police', 'computer', 
                'ambulance', 'tower', 'education', 'window'] #List of words for Hangman
    secretWord = wordList[random.randint(0, (len(wordList)-1))] #Selects random word from list
    correctGuess = ''
    for i in secretWord:
        correctGuess += '_ '
    wrongGuess = ''
    wrongGuesses = 0
    print('Welcome.')
    print('Secret word: ' + str(correctGuess))
    while wrongGuesses <= 9 and not win:
        guess = input('Guess a letter.\n')
        n = -2
        if guess == secretWord:
            win = True
            break
        
        for i in secretWord:
            # +2 because it has to jump over the whitespaces in correctGuess
            n += 2
            if guess == i:
                # this replaces the correct letters (correctGuess[i] = guess is prettier but impossible)
                correctGuess = correctGuess[:n] + guess + correctGuess[n+1:]
        print(correctGuess)

        if guess in wrongGuess:
            print('Already guessed.')
        elif guess not in secretWord:
            print('Wrong')
            wrongGuess += guess
            
            print('Letters not in the word: ' + str(wrongGuess))
            wrongGuesses += 1
            print('Guesses left: ' + str(10 - wrongGuesses))
        if '_' not in correctGuess:
            win = True
            break

    if win:
        print('You won!')
    else:
        print('You lost :( \n'
              'The word was: ' + str(secretWord))
    while True:
        replay = input('Replay? yes/no')
        if replay.startswith('y'):
            print('')
            main()
        elif replay.startswith('n'):
            print('BOB-BIP')
            break
        else:
            print('Try again')
main()
