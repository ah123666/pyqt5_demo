import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication,\
    QWidget, QPushButton


class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication, self).__init__()
        self.resize(300, 120)
        self.setWindowTitle("退出应用程序")

        # 添加Button
        self.button1 = QPushButton("退出")
        # 信号与槽关联
        self.button1.clicked.connect(self.onClick_Buttton)

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainForm = QWidget()
        mainForm.setLayout(layout)
        self.setCentralWidget(mainForm)

    # 按钮单击事件方法()槽
    def onClick_Buttton(self):
        sender = self.sender()
        print(sender.text() + "按钮被按下")
        app = QApplication.instance()
        # 退出应用程序
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuitApplication()
    main.show()
    sys.exit(app.exec_())
