"""
 Created by PyCharm Community Edition.
 User: Anton Vasiliev <bysslaev@gmail.com>
 Date: 07/04/2018
 Time: 15:20

"""
from lib.FileReader import FileReader
from lib.ICommand import ICommand
from lib.Logger import Logger


class CommandRestore(ICommand):
    """
    Комманда восстановления текста из файла
    """

    def execute(self):
        filereader = FileReader(self.form.userfile)
        filereader.open()
        text = ''
        while True:
            temp_str = filereader.readLine()
            if not temp_str:
                break
            text += temp_str
        self.form.txtEdit.setText(text)
        logger = Logger()
        logger.log("readTextFromFile()")
        filereader.close()
