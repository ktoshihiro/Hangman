import random

languages = ['python', 'java', 'kotlin', 'javascript']
random.seed()


def hangman():
    language: str = random.choice(languages)
    remains = set(language)
    inputs = set()
    lives = 8
    while lives > 0 and len(remains) > 0:
        print()
        lang = ''
        for i in language:
            if i in remains:
                lang += '-'
            else:
                lang += i
        print(lang)

        letter = input('Input a letter:')

        if len(letter) != 1:
            print('You should input a single letter')
            continue

        if letter in inputs:
            print("You've already guessed this letter")
            continue

        if not letter.islower():
            print('Please enter a lowercase English letter')
            continue

        inputs.add(letter)

        if language.count(letter):
            remains.discard(letter)
        else:
            print("That letter doesn't appear in the word")
            lives -= 1

    if len(remains) > 0:
        print('You lost!')
    else:
        print(language)
        print('You guessed the word!')
        print('You survived!')

    print()
    print()


print('H A N G M A N')
command = input('Type "play" to play the game, "exit" to quit:')
if command == 'play':
    hangman()
