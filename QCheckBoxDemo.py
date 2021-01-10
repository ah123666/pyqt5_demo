from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class QCheckBoxDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("复选框控件演示")
        layout = QHBoxLayout()
        self.checkBox1 = QCheckBox("复选框控件1")
        self.checkBox1.setChecked(True)
        self.checkBox1.stateChanged.connect(lambda : self.checkBoxState(self.checkBox1))
        layout.addWidget(self.checkBox1)

        self.checkBox2 = QCheckBox("复选框控件2")
        self.checkBox2.stateChanged.connect(lambda : self.checkBoxState(self.checkBox2))
        layout.addWidget(self.checkBox2)

        self.checkBox3 = QCheckBox("半选中")
        self.checkBox3.setTristate(True)
        self.checkBox3.setCheckState(Qt.PartiallyChecked)
        self.checkBox3.stateChanged.connect(lambda : self.checkBoxState(self.checkBox3))
        layout.addWidget(self.checkBox3)

        self.setLayout(layout)

    def checkBoxState(self, cb):
        # check1State = self.checkBox1.text() + ', is checked=' + \
        #     str(self.checkBox1.isChecked()) + \
        #     ', checkState=' + str(self.checkBox1.checkState()) + '\n'
        # check2State = self.checkBox2.text() + ', is checked=' + \
        #     str(self.checkBox2.isChecked()) + \
        #     ', checkState=' + str(self.checkBox2.checkState()) + '\n'
        # check3State = self.checkBox3.text() + ', is checked=' + \
        #     str(self.checkBox3.isChecked()) + \
        #     ', checkState=' + str(self.checkBox3.checkState()) + '\n'
        # print(check1State + check2State + check3State)
        checkState = cb.text() + ', is checked=' + \
            str(cb.isChecked()) + \
            ', checkState=' + str(cb.checkState()) + '\n'
        print(checkState)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QCheckBoxDemo()
    mainWin.show()
    sys.exit(app.exec_())


