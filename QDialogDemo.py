from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class QDialogDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QDialogDemo")
        self.resize(300, 200)
        self.button = QPushButton(self)
        self.button.setText("弹出对话框")
        self.button.move(50, 50)
        self.button.clicked.connect(self.showDialog)

    def showDialog(self):
        dialog = QDialog()
        dialog.resize(200, 100)
        btn = QPushButton('退出', dialog)
        btn.move(50, 50)
        btn.clicked.connect(dialog.close)
        dialog.setWindowTitle("对话框")
        dialog.setWindowModality(Qt.ApplicationModal) # 显示对话框时其他的控件都不可用

        dialog.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QDialogDemo()
    mainWin.show()
    sys.exit(app.exec_())



