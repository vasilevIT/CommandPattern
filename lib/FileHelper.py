"""
 Created by PyCharm Community Edition.
 User: Anton Vasiliev <bysslaev@gmail.com>
 Date: 07/04/2018
 Time: 00:47

"""

import os


class FileHelper:
    """
    Класс для работы с файлами
    """

    TYPE_READ = 'r'
    TYPE_WRITE = 'w'

    def __init__(self, filename):
        self.file = None
        self.filename = filename
        self.type = self.TYPE_READ

    def open(self):
        """
        Метод для открытия файла
        :param type:
        :param filename:
        :return:
        """
        if os.path.isfile(self.filename):
            self.file = open(self.filename, self.type)

    def close(self):
        """
        Закрываем файл
        :return:
        """
        self.file.close()
