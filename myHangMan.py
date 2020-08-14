# Import
import random

# Board
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

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


class Hangman:

    def __init__(self, word):
        self.word = word
        self.guessed_letters = []
        self.missed_letters = []

    def guess(self, letter):
        if letter in self.word and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
        elif letter not in self.word and letter not in self.missed_letters:
            self.missed_letters.append(letter)
        else:
            return False
        return True

    def hangman_over(self):
        return self.hangman_won() or (len(self.missed_letters) == 6)

    def hangman_won(self):
        if '-' not in self.hide_word():
            return True
        else:
            return False

    def hide_word(self):
        temporaryLetter = ''
        for letter in self.word:
            if letter not in self.guessed_letters:
                temporaryLetter += '-'
            else:
                temporaryLetter += letter
        return temporaryLetter

    def print_game_status(self):
        print (board[len(self.missed_letters)])
        print('Word: %s' % (self.hide_word()))
        print()
        print('Guessed Letter: ')
        for x in self.guessed_letters:
            print(x)
        print()
        print('Missed Letters: ')
        for y in self.missed_letters:
            print(y)


def rand_word():
    with open("words.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


def main():

    game = Hangman(rand_word())

    while not game.hangman_over():
        game.print_game_status()
        l = input('Give it a try: ')
        game.guess(l)

    game.print_game_status()

    if game.hangman_won():
        print('\nYou win!!')
    else:
        print('\nGame over! You lost.')
        print('The word was ' + game.word)

if __name__ == "__main__":
    main()
