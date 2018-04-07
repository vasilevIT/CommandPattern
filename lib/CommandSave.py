"""
 Created by PyCharm Community Edition.
 User: Anton Vasiliev <bysslaev@gmail.com>
 Date: 07/04/2018
 Time: 15:20

"""
from lib.FileWriter import FileWriter
from lib.ICommand import ICommand
from lib.Logger import Logger


class CommandSave(ICommand):
    """
    Класс сохранения данных из формы в файл
    """

    def execute(self):
        text = self.form.txtEdit.toPlainText()
        filewriter = FileWriter(self.form.userfile)
        filewriter.open()
        filewriter.writeLine(text)
        filewriter.close()
        logger = Logger()
        logger.log("saveText()")
