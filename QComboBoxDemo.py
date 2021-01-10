from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class QComboDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("下拉列表控件演示")
        self.resize(400, 50)
        self.move(300, 300)
        layout = QVBoxLayout()
        self.label = QLabel("请选择编程语言")

        self.cb = QComboBox()
        self.cb.addItem("C++")
        self.cb.addItem("Python")
        self.cb.addItems(["Java", "C#", "Ruby"])

        self.cb.currentIndexChanged.connect(self.selectionChange)

        layout.addWidget(self.label)
        layout.addWidget(self.cb)

        self.setLayout(layout)

    def selectionChange(self, i):
        self.label.setText(self.cb.currentText())
        self.label.adjustSize()

        for count in range(self.cb.count()):
            print("item:" + str(count) + "=" + self.cb.itemText(count))
        print("current index", i, "selection changed", self.cb.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QComboDemo()
    mainWin.show()
    sys.exit(app.exec_())