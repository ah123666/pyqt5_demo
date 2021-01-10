import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QToolTip, QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon, QFont


class ToolTipForm(QMainWindow):
    def __init__(self):
        super(ToolTipForm, self).__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont("SansSerif", 12))
        self.setToolTip("今天是<b>星期五</b>")
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle("设置控件提示信息")
        self.button1 = QPushButton("退出")
        self.button1.setToolTip("这是一个按钮！")

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainForm = QWidget()
        mainForm.setLayout(layout)
        self.setCentralWidget(mainForm)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = ToolTipForm()
    main_win.show()
    sys.exit(app.exec_())
