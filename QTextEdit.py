from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class QTextEditDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTextEdit控件演示")
        self.resize(300, 280)
        self.move(300, 300)

        self.textEdit = QTextEdit()
        self.button1 = QPushButton("显示文本")
        self.button2 = QPushButton("显示HTML")
        self.button3 = QPushButton("获取文本")
        self.button4 = QPushButton("获取HTML")

        self.button1.clicked.connect(self.onClick_button1)
        self.button2.clicked.connect(self.onClick_button2)
        self.button3.clicked.connect(self.onClick_button3)
        self.button4.clicked.connect(self.onClick_button4)

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        self.setLayout(layout)

    def onClick_button1(self):
        self.textEdit.setPlainText("Hello World, 你好！")

    def onClick_button2(self):
        self.textEdit.setHtml("<font color='blue', size=5> Hello World!</font")

    def onClick_button3(self):
        print(self.textEdit.toPlainText())

    def onClick_button4(self):
        print(self.textEdit.toHtml())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QTextEditDemo()
    mainWin.show()
    sys.exit(app.exec_())