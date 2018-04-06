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
    TYPE_WRITE_APPEND = 'a+'

    def __init__(self, filename):
        self.file = None
        self.filename = filename
        self.type = self.TYPE_READ

    def setType(self, type):
        self.type = type

    def open(self):
        """
        Метод для открытия файла
        :param type:
        :param filename:
        :return:
        """
        if not os.path.isfile(self.filename):
            self.createFile()
        self.file = open(self.filename, self.type)

    def close(self):
        """
        Закрываем файл
        :return:
        """
        self.file.close()

    def createFile(self):
        f = open(self.filename, 'w')
        f.close()
