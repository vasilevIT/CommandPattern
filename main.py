"""
 Created by PyCharm Community Edition.
 User: Anton Vasiliev <bysslaev@gmail.com>
 Date: 07/04/2018
 Time: 00:15

"""
import sys
from PyQt5.QtWidgets import QApplication

from gui.NotepadForm import NotepadForm

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = NotepadForm()
    sys.exit(app.exec_())