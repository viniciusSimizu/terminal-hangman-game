import re
from math import floor

from configuration import Configuration
from word import Word


class Hangman:
    def __init__(self, word: Word, configuration: Configuration) -> None:
        self.__attempts_history: list[str] = []

        self.word: Word = word
        self.__configuration: Configuration = configuration

    def play(self) -> bool:
        attempts = self.__configuration.attempts

        while attempts:
            self.__print_hangman(attempts)
            print()

            user_input = input('Guess: ').lower()
            print()

            valid_input = self.__valid_input(user_input)
            if not valid_input:
                continue

            self.__attempts_history.append(user_input)

            if not self.__correct_guess(user_input):
                attempts -= 1
                continue

            if self.__has_won():
                self.__print_hangman(attempts)
                return True

        self.__print_hangman(attempts)
        return False

    def __word_with_only_correct_letters(self) -> str:
        characters = []

        for letter in self.word['word'].lower():
            if letter in self.__attempts_history:
                characters.append(letter)
            elif letter.isspace():
                characters.append(' ')
            else:
                characters.append('_')

        word_with_only_correct_letters = ' '.join(characters)
        return word_with_only_correct_letters

    def __has_won(self) -> bool:
        for letter in self.word['word'].lower():
            correct_letter = letter in self.__attempts_history or letter.isspace()

            if not correct_letter:
                return False

        return True

    def __correct_guess(self, user_input: str) -> bool:
        correct_character = user_input in self.word['word'].lower()
        return correct_character

    def __valid_input(self, user_input: str) -> bool:
        already_tried = self.__already_tried(user_input)
        regex_patter_match = bool(re.search(r'^[a-z]{1}$', user_input))

        valid_input = regex_patter_match and not already_tried

        if valid_input:
            return True

        return False

    def __already_tried(self, user_input: str) -> bool:
        return user_input in self.__attempts_history

    def __print_hangman(self, attempts_left: int) -> None:
        print_levels = 6
        current_print_level = floor(
            print_levels - (attempts_left * 6) / self.__configuration.attempts)

        print(f'Hint: {self.word["hint"]}', end='')
        match current_print_level:
            case 0:
                print(
                    """
 ________
 |      |
 |
 |
 |
 |
 |""", end='')
            case 1:
                print(
                    """
 ________
 |      |
 |    (>_<)
 |
 |
 |
 |""", end='')
            case 2:
                print(
                    """
 ________
 |      |
 |    (>_<)
 |     _|_
 |      | 
 |      |  
 |""", end='')
            case 3:
                print(
                    """
 ________
 |      |
 |    (>_<)
 |     _|_
 |    / |
 |      |  
 |""", end='')
            case 4:
                print(
                    """
 ________
 |      |
 |    (>_<)
 |     _|_
 |    / | \\
 |      |  
 |""", end='')
            case 5:
                print(
                    """
 ________
 |      |
 |    (>_<)
 |     _|_
 |    / | \\
 |      |  
 |     /""", end='')
            case 6:
                print(
                    """
 ________
 |      |
 |    (x-x)
 |     _|_
 |    / | \\
 |      |  
 |     / \\""", end='')

        correct_letters = self.__word_with_only_correct_letters()

        print(
            f"""
 |    --{'-' * len(correct_letters)}--
 |    | {correct_letters} |
_|_   --{'-' * len(correct_letters)}--

[{', '.join(self.__attempts_history)}]""")
