"""
 Created by PyCharm Community Edition.
 User: Anton Vasiliev <bysslaev@gmail.com>
 Date: 07/04/2018
 Time: 01:37

"""
import datetime

from lib.FileWriter import FileWriter


class Logger:
    """
    Класс для записи логов
    """

    def __init__(self):
        self.logfile = 'log.txt'

    def setLogFile(self, logfile):
        self.logfile = logfile

    def log(self, string):
        now = datetime.datetime.now()

        filewriter = FileWriter(self.logfile)
        filewriter.setType(FileWriter.TYPE_WRITE_APPEND)
        filewriter.open()
        filewriter.writeLine(str(" ".join((":".join((str(now.hour), str(now.minute), str(now.second))), string))))
        filewriter.close()
