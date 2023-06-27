from functools import partial
from threading import Thread

from configuration import Configuration
from csv_module import CsvModule
from game_manager import GameManager
from menu_option import MenuOption


class Manager:
    def __init__(self) -> None:
        self.__name: str = ''
        self.__csv_module = CsvModule()
        self.__configuration = Configuration()

    def start(self) -> None:
        self.__interactive_menu(self.__get_lobby_options,
                                title='Lobby', exit_message='Exit')

    def __interactive_menu(self, get_options: 'function', title: str, exit_message: str) -> None:
        while True:
            options = get_options()

            self.__print_options(options, title=title,
                                 exit_message=exit_message)
            user_input = input('Enter: ')
            print()

            if not self.__valid_user_input(user_input, options):
                continue

            user_input = int(user_input)

            if user_input == 0:
                break

            options[user_input - 1].get('activation_function')()

            print()

    def __valid_user_input(self, user_input: str, options: list[MenuOption]) -> bool:
        try:
            user_input_number = int(user_input)
        except ValueError:
            return False

        if user_input_number not in range(len(options) + 1):
            return False

        return True

    def set_name(self) -> None:
        name = input('Name: ').strip()
        self.__name = name

    def __create_word(self) -> None:
        word = input('Word: ')
        hint = input('Hint: ')

        Thread(target=self.__register_word(word, hint)).start()

    def update_attempts(self) -> None:
        new_attempts = int(input('New Attempts: '))
        self.__configuration.set_attempts(new_attempts)

    def __print_options(self, options_dict: list[MenuOption], title: str, exit_message: str) -> None:
        print(f'{title}:')
        for i, option in enumerate(options_dict):
            print(f"{i+1} - {option.get('description')}")

        print(f'0 - {exit_message}')

    def __get_configuration_options(self) -> list[MenuOption]:
        options: list['MenuOption'] = []

        if True:
            menu_option = MenuOption(description=f'Attempts [ {self.__configuration.attempts} ]',
                                     activation_function=self.update_attempts)
            options.append(menu_option)

        return options

    def __get_lobby_options(self) -> list[MenuOption]:
        options: list['MenuOption'] = []

        if True:
            menu_option = MenuOption(description='Play',
                                     activation_function=GameManager(
                                         self.__csv_module, self.__configuration).play)
            options.append(menu_option)

        if self.__name:
            menu_option = MenuOption(
                description='Register a Word', activation_function=self.__create_word)
            options.append(menu_option)

        if True:
            username_print = f'[ "{self.__name}" ]' if self.__name else ''

            menu_option = MenuOption(
                description=f'Set Name {username_print}', activation_function=self.set_name)
            options.append(menu_option)

        if True:
            menu_option = MenuOption(
                description='Configuration', activation_function=partial(
                    self.__interactive_menu, self.__get_configuration_options, title='Configuration', exit_message='Go Back'))
            options.append(menu_option)

        return options

    def __register_word(self, word: str, hint: str) -> None:
        self.__csv_module.write_csv(
            {'word': word, 'hint': hint, 'creator': self.__name})
