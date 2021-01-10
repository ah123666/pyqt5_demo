from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class QMessageBoxDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QMessageBoxDemo')
        self.resize(300, 400)
        self.move(300, 300)
        layout = QVBoxLayout()

        self.btn1 = QPushButton('关于')
        self.btn1.setText('显示关于对话框')
        self.btn1.clicked.connect(self.showDialog)

        self.btn2 = QPushButton('显示消息对话框')
        self.btn2.clicked.connect(self.showDialog)

        self.btn3 = QPushButton('显示警告对话框')
        self.btn3.clicked.connect(self.showDialog)

        self.btn4 = QPushButton('显示错误对话框')
        self.btn4.clicked.connect(self.showDialog)


        self.btn5 = QPushButton('显示提问对话框')
        self.btn5.clicked.connect(self.showDialog)


        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        layout.addWidget(self.btn4)
        layout.addWidget(self.btn5)
        self.setLayout(layout)

    def showDialog(self):
        text = self.sender().text()
        if text == '显示关于对话框':
            QMessageBox.about(self, '关于', '这是一个关于对话框')
        elif text == '显示消息对话框':
            reply = QMessageBox.information(self, '消息', '这是一个消息对话框', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            print(reply == QMessageBox.Yes)
        elif text == '显示警告对话框':
            QMessageBox.warning(self, '警告', '这是一个警告对话框', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        elif text == '显示错误对话框':
            QMessageBox.critical(self, '错误', '这是一个错误对话框', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        elif text == '显示提问对话框':
            QMessageBox.question(self, '提问', '这是一个提问对话框', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QMessageBoxDemo()
    mainWin.show()
    sys.exit(app.exec_())