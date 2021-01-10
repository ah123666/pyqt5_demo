"""
用掩码限制输入
"""
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class QLineEditMask(QWidget):
    def __init__(self):
        super(QLineEditMask, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("用掩码限制控件输入")
        formlayout = QFormLayout()

        ipLineEdit = QLineEdit()
        macLineEdit = QLineEdit()
        dateLineEdit = QLineEdit()
        licenseLineEdit = QLineEdit()

        # 192.168.21.45
        ipLineEdit.setInputMask("000.000.000.000;_")
        macLineEdit.setInputMask("HH:HH:HH:HH:HH:HH;_")
        dateLineEdit.setInputMask("0000-00-00")
        licenseLineEdit.setInputMask(">AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#")

        formlayout.addRow("数字掩码", ipLineEdit)
        formlayout.addRow("mac掩码", macLineEdit)
        formlayout.addRow("日期掩码", dateLineEdit)
        formlayout.addRow("许可证掩码", licenseLineEdit)

        self.setLayout(formlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QLineEditMask()
    mainWin.show()
    sys.exit(app.exec_())


