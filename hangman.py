import sys
import random

Form0=("""
    ________
    |       
    |   
    |       
    |  
    |
    |______________

        """)

Form1=("""
    ________
    |       O
    |   
    |       
    |      
    |      
    |______________

        """)

Form2=("""
    ________
    |       O
    |       |
    |       |
    |      
    |     
    |______________

        """)

Form3=("""
    ________
    |       O
    |   ----|
    |       |
    |      
    |      
    |______________

        """)

Form4=("""
    ________
    |       O
    |   ----|----
    |       |
    |      
    |      
    |______________

        """)

Form5=("""
    ________
    |       O
    |   ----|----
    |       |
    |      | 
    |      | 
    |______________

        """)

Form6=("""
    ________
    |       O
    |   ----|----
    |       |
    |      | |
    |      | |
    |______________

        """)


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

def hangPic(form):
    if form == 0:
        print(Form0)
    elif form == 1:
        print(Form1)
    elif form == 2:
        print(Form2)
    elif form == 3:
        print(Form3)
    elif form == 4:
        print(Form4)
    elif form == 5:
        print(Form5)
    elif form == 6:
        print(Form6)

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
    print(f"{Form0}\n")

    usedChars=[]

    while turns > 0:
        guesses1=arrToStr(guesses)
        print(f'\n{guesses1}\n')
        displayUsedChars(usedChars)
        guess=input('\nGuess a character:\n')
        
        while guess=='':
            guess=input('\nGuess a character:\n')

        while len(guess) > 1:
            guess=input('\nGuess must be one character...\nGo again:\n')

        while guess in usedChars:
            guess=input(f"\nYou've already guessed '{guess.upper()}'...\nTry again:\n")

        while guess in guesses:
            guess=input(f"\n'{guess.upper()}' is already correct... We don't like smart alecks\nGuess again:\n")

        if guess not in secretWord:
            usedChars.append(guess)
            turns-=1
            form=6-turns
            print('\nWrong!\n')
            hangPic(form)
            print(f"You have {turns} more guesses\n")
            if turns == 0:
                print('YOU LOSE!\n')
                print(f'The correct word is: {arrToStr2(secretWord)}\n')
                start()
        elif guess in secretWord:
            hangPic(form)
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