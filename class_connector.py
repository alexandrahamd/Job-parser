import logging
import os
import json


class Connector:
    """
    Класс коннектор к файлу
    """
    __data_file = None

    def __init__(self, df):
        self.__data_file = df
        self.__connect()

    def __connect(self):
        """
        Проверка на существование файла с данными и
        создание его при необходимости
        """
        try:
            if self.__data_file not in os.listdir('.'):
                with open(self.__data_file, 'w') as file:
                    file.write(json.dumps([]))
        except Exception as ex:
            logging.critical(ex)

    def insert(self, data):
        try:
            with open(self.__data_file, 'w', encoding='utf-8') as f:
                f.seek(0)
                json.dump(data, f)
        except:
            print('Ошибка записи файла')

        return self.__data_file


if __name__ == '__main__':
    df = Connector('df3.json')

    data_for_file = {'id': 1, 'title': 'tet'}

    df.insert(data_for_file)
    data_from_file = df.select(dict())
    assert data_from_file == [data_for_file]

    df.delete({'id': 1})
    data_from_file = df.select(dict())
    assert data_from_file == []
