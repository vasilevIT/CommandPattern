"""
 Created by PyCharm Community Edition.
 User: Anton Vasiliev <bysslaev@gmail.com>
 Date: 07/04/2018
 Time: 15:20

"""
from PyQt5.QtWidgets import QMessageBox
from lib.ICommand import ICommand
from lib.Logger import Logger


class CommandClear(ICommand):
    """
    Команда очистки текстового поля
    """

    def execute(self):
        reply = QMessageBox.question(self.form, 'Message',
                                     "Are you sure to clear text?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.form.txtEdit.setText('')
            logger = Logger()
            logger.log("clearText()")
