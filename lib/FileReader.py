"""
 Created by PyCharm Community Edition.
 User: Anton Vasiliev <bysslaev@gmail.com>
 Date: 07/04/2018
 Time: 01:06

"""
from lib.FileHelper import FileHelper


class FileReader(FileHelper):
    """
    Класс для чтения из текстового файла
    """

    def __init__(self, filename):
        super().__init__(filename)
        self.type = self.TYPE_READ

    def readLine(self):
        """
        Читает строку из файла
        :return:
        """
        return self.file.readline()
