from random import choice

from configuration import Configuration
from csv_module import CsvModule
from hangman import Hangman
from word import Word


class GameManager:
    def __init__(self, csv_module: 'CsvModule', configuration: Configuration) -> None:
        self.__csv_module = csv_module
        self.__configuration = configuration

    def play(self) -> None:
        hangman_instance = self.__initialize_hangman()
        has_won = hangman_instance.play()
        print()

        if has_won:
            self.__win()
        else:
            self.__loss(hangman_instance.word)

    def __win(self) -> None:
        print('A Deus Gamer has come to the Earth 😎')

    def __loss(self, word: Word) -> None:
        print(f'Too bad... the word was "{word.get("word")}"')

    def __initialize_hangman(self) -> 'Hangman':
        secret_word = self.__decide_word()
        return Hangman(secret_word, self.__configuration)

    def __decide_word(self) -> Word:
        words = self.__csv_module.read_csv()
        word_chosen: Word = choice(words)

        return word_chosen
