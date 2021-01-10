import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QMessageBoxDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QMessageBoxDemo')
        self.resize(300, 400)
        self.mainWidget = QWidget()
        self.setCentralWidget(self.mainWidget)
        layout = QVBoxLayout()
        self.button1 = QPushButton('显示关于对话框')
        self.button1.clicked.connect(self.showDialog)
        self.button2 = QPushButton('显示消息对话框')
        self.button2.clicked.connect(self.showDialog)
        self.button3 = QPushButton('显示警告对话框')
        self.button3.clicked.connect(self.showDialog)
        self.button4 = QPushButton('显示错误对话框')
        self.button4.clicked.connect(self.showDialog)
        self.button5 = QPushButton('显示提问对话框')
        self.button5.clicked.connect(self.showDialog)

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)
        self.mainWidget.setLayout(layout)

    def showDialog(self):
        text = self.sender().text()
        if text == '显示关于对话框':
            QMessageBox.about(self, '关于', '这是一个关于对话框')
        elif text == '显示消息对话框':
            reply = QMessageBox.information(self, '消息', '这是一个消息对话框', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        elif text == '显示警告对话框':
            QMessageBox.warning(self, '警告', '这是一个警告对话框')
        elif text == '显示错误对话框':
            QMessageBox.critical(self, '错误', '这是一个错误对话框')
        elif text == '显示提问对话框':
            QMessageBox.question(self, '提问', '这是一个提问对话框')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = QMessageBoxDemo()
    main_win.show()
    sys.exit(app.exec_())
