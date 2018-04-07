"""
 Created by PyCharm Community Edition.
 User: Anton Vasiliev <bysslaev@gmail.com>
 Date: 07/04/2018
 Time: 00:09

"""
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QTextEdit, QLabel, QToolTip
from lib.CommandClear import CommandClear
from lib.CommandRestore import CommandRestore
from lib.CommandSave import CommandSave


class NotepadForm(QWidget):
    """
    Форма блокнота
    """

    def __init__(self):
        super().__init__()
        self.userfile = "simplyfile.txt"
        self.commands = {}
        self.commands["save"] = CommandSave(self)
        self.commands["restore"] = CommandRestore(self)
        self.commands["clear"] = CommandClear(self)
        self.initUI()

    def initUI(self):
        """ Инициализация компонентов формы"""
        QToolTip.setFont(QFont('SansSerif', 10))
        self.label = QLabel()
        self.label.setText('Simple notepad:')
        self.label.resize(self.label.sizeHint())
        self.label.move(50, 30)

        self.txtEdit = QTextEdit()
        self.txtEdit.resize(700, 400)
        self.txtEdit.move(50, 50)

        self.btnSave = QPushButton('Save')
        self.btnSave.setToolTip('Save text to file.')
        self.btnSave.resize(self.btnSave.sizeHint())
        self.btnSave.move(50, 380)

        self.btnRead = QPushButton('Read')
        self.btnRead.setToolTip('Read text from file.')
        self.btnRead.resize(self.btnRead.sizeHint())
        self.btnRead.move(50, 420)

        self.btn = QPushButton('Clear')
        self.btn.setToolTip('Clear textedit')
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(50, 470)


        vBox = QVBoxLayout()
        vBox.addStretch(1)
        vBox.addWidget(self.label)
        vBox.addWidget(self.txtEdit)
        vBox.addWidget(self.btnSave)
        vBox.addWidget(self.btnRead)
        vBox.addWidget(self.btn)

        self.setLayout(vBox)
        self.resize(700, 400)
        self.setWindowTitle('Notepad')

        """Привязка команд к кнопкам формы"""
        self.btnSave.clicked.connect(self.commands["save"].execute)
        self.btnRead.clicked.connect(self.commands["restore"].execute)
        self.btn.clicked.connect(self.commands["clear"].execute)

        self.show()
