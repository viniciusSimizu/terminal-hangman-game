import csv
from datetime import datetime

from pytz import timezone

from word import Word


class CsvModule:
    def __init__(self) -> None:
        self.__file_path = 'words.csv'
        self.__header = ['word', 'hint', 'creator', 'created_at']

        self.__initialize_file()

    def read_csv(self) -> list:
        with open(self.__file_path, 'r', newline='\n') as csv_file:
            data = csv.DictReader(csv_file)

            words: list[Word] = [word for word in data]

            return words

    def write_csv(self, word: Word) -> None:
        with open(self.__file_path, 'a', newline='\n') as csv_file:
            word['created_at'] = datetime.now(tz=timezone('America/Sao_Paulo'))

            csv_writer = csv.DictWriter(
                csv_file, fieldnames=self.__header, quoting=1)
            csv_writer.writerow(word)

    def __initialize_file(self) -> None:
        try:
            with open(self.__file_path, 'x') as csv_file:
                csv_writer = csv.DictWriter(
                    csv_file, fieldnames=self.__header, quoting=1)
                csv_writer.writeheader()
        except FileExistsError:
            pass
