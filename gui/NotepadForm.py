"""
 Created by PyCharm Community Edition.
 User: Anton Vasiliev <bysslaev@gmail.com>
 Date: 07/04/2018
 Time: 00:09

"""
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QMessageBox, QPushButton, QVBoxLayout, qApp, QTextEdit, QLabel, \
    QToolTip


class NotepadForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        text = self.readTextFromFile()
        self.label = QLabel()
        self.label.setText('Simple notepad:')
        self.label.resize(self.label.sizeHint())
        self.label.move(50, 30)

        self.txtEdit = QTextEdit()
        self.txtEdit.resize(700, 400)
        self.txtEdit.move(50, 50)
        self.txtEdit.setText(text)

        self.btnSave = QPushButton('Save')
        self.btnSave.setToolTip('Save text to file.')
        self.btnSave.resize(self.btnSave.sizeHint())
        self.btnSave.move(50, 380)
        self.btnSave.clicked.connect(self.saveText)

        self.btnRead = QPushButton('Read')
        self.btnRead.setToolTip('Read text from file.')
        self.btnRead.resize(self.btnRead.sizeHint())
        self.btnRead.move(50, 420)
        self.btnRead.clicked.connect(self.restoreText)

        self.btn = QPushButton('Clear')
        self.btn.setToolTip('Clear textedit')
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(50, 470)
        self.btn.clicked.connect(self.clearText)

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

        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def readTextFromFile(self):
        #     TODO: Need to implement
        return ""

    def saveText(self):
        #     TODO: Need to implement
        pass

    def restoreText(self):
        pass

    def clearText(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to clear text?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.txtEdit.setText('')
