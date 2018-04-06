"""
 Created by PyCharm Community Edition.
 User: Anton Vasiliev <bysslaev@gmail.com>
 Date: 07/04/2018
 Time: 00:46

"""
from lib.FileHelper import FileHelper


class FileWriter(FileHelper):
    """
    Класс для записи данных в текстовый файл
    """

    def __init__(self, filename):
        super().__init__(filename)
        self.type = self.TYPE_WRITE

    def writeLine(self, text):
        """
        Записывает строку в файл
        :param text:
        :return:
        """
        if not self.file:
            return
        self.file.write(text)
        self.file.write('\n')
