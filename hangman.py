import sys
import random

import time
# from tkinter.tix import Form

Forms = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def start():
    restart=input('Would you like to play again? (y/n)\n')
    if restart == ('y' or 'Y'):
        main()
    elif restart == ('n' or 'N'):
        sys.exit('\nThank you for playing :)\n')
    else:
        print('\nSomething went wrong... Try again\n')
        start()

def findChars(str, ch):
    # return[i for i, letter in enumerate(str) if letter == ch]
    arr=[]
    for i, letter in enumerate(str):
        if letter == ch:
            arr.append(i)
    return arr

def arrToStr(arr, str=''):
    for index in arr:
        str+=f'{index.upper()}  '
    return str

def arrToStr2(arr, str=''):
    for index in arr:
        str+=f'{index.upper()}'
    return str


def hangPic(pic):
    print(f'{Forms[pic]}')

def displayUsedChars(arr):
    msg="Characters you've already guessed:\n["
    for index in arr:
        msg+=f'{index.upper()}, '
    msg+=']'
    print(msg)


def main():

    websters=[]

    with open('websters.txt') as file:
        while(line := file.readline().rstrip()):
            websters.append(line)

    answers=random.choice(websters)
    secret=[]
    for answer in answers:
        secret.append(answer)
    secretWord=tuple(secret)

    turns=6
    form=6-turns

    guesses=['_'] * len(secretWord)

    print("\n\nWELCOME TO HANGMAN!")
    print("\n(Type 'quit' to exit the program)")
    print(f"{Forms[0]}\n")

    usedChars=[]

    while turns > 0:
        guesses1=arrToStr(guesses)
        print(f'\n{guesses1}\n')
        displayUsedChars(usedChars)
        guess=input('\nGuess a character:\n')
        
        while True:
            if guess=='':
                guess=input('\nGuess a character:\n')
            elif len(guess) > 1:
                if guess.lower() == 'quit':
                    sys.exit('\nSad to see you go... Come back anytime!\n')
                else:
                    guess=input('\nGuess must be one character...\nGo again:\n')
            elif guess in usedChars:
                guess=input(f"\nYou've already guessed '{guess.upper()}'...\nTry again:\n")
            elif guess in guesses:
                guess=input(f"\n'{guess.upper()}' is already correct... We don't like smart alecks\nGuess again:\n")
            else:
                break

        if guess not in secretWord:
            usedChars.append(guess)
            turns-=1
            form=6-turns
            print('\WRONG!\n')
            hangPic(form)
            print(f"Guesses Left: {turns}\n")
            if turns == 0:
                print('YOU LOSE!\n')
                print(f'The correct word is: {arrToStr2(secretWord)}\n')
                start()
        elif guess in secretWord:
            hangPic(form)
            print(f"Guesses Left: {turns}\n")
            chIndex=findChars(secretWord, guess)
            for i in chIndex:
                guesses[i] = guess
        check=True
        for i in range(0, len(secretWord)):
            if(guesses[i] != secretWord[i]):
                check=False
                break
        if check == True:
            print('YOU WIN!')
            print(f'\nYou guessed the correct word: {arrToStr2(guesses)}\n')
            start()

if __name__ == "__main__":
    main()