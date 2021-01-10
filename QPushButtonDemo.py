from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QPushButtonDemo")
        self.resize(300, 200)
        self.move(300, 300)
        layout = QVBoxLayout()
        self.button1 = QPushButton("按钮1")
        self.button1.setText("first button")
        self.button1.setCheckable(True)
        self.button1.toggle()  # 按钮处于选中状态，在调用一次就是未选中
        self.button1.clicked.connect(lambda: self.whichButton(self.button1))
        self.button1.clicked.connect(self.buttonState)


        self.button2 = QPushButton("图像按钮")
        self.button2.setIcon(QIcon(QPixmap(".\\ico\\icon.ico")))
        self.button2.clicked.connect(lambda: self.whichButton(self.button2))

        self.button3 = QPushButton("不可用的按钮")
        self.button3.setEnabled(False)

        self.button4 = QPushButton("&MyButton")
        self.button4.setDefault(True)
        self.button4.clicked.connect(lambda: self.whichButton(self.button4))


        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        self.setLayout(layout)

    def whichButton(self, btn):
        print("被单击的按钮是：" + btn.text())

    def buttonState(self):
        if self.button1.isChecked():
            print("按钮1被选中")
        else:
            print("按钮1未被选中")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QPushButtonDemo()
    mainWin.show()
    sys.exit(app.exec_())
