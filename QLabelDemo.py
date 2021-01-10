import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QToolTip, QPushButton, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon, QFont, QPalette, QPixmap
from PyQt5.QtCore import Qt


class QLabelDemo(QMainWindow):
    def __init__(self):
        super(QLabelDemo, self).__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle("QLabelDemo")
        label1 = QLabel()
        label2 = QLabel()
        label3 = QLabel()
        label4 = QLabel()

        # HTML标签
        label1.setText("<font color=yellow>这是一个文本标签.</font>")
        label1.setAutoFillBackground(True)
        palette = QPalette()  # 设置调色板
        palette.setColor(QPalette.Window, Qt.blue)  # 设置背景色
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)  # 文本居中对齐

        label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")

        label3.setAlignment(Qt.AlignCenter)  # 文本居中对齐
        label3.setToolTip("这是一个图片标签")
        label3.setPixmap(QPixmap("C:\\Users\\dell\\Desktop\\Img\\9.jpeg"))

        label4.setText("<a href='https://item.jd.com/12417265.html'>感谢关注</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip("这是一个超链接")
        label4.setOpenExternalLinks(True)

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHoverd)
        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)
        self.setWindowTitle("QLabel控件演示")

        mainForm = QWidget()
        mainForm.setLayout(vbox)
        self.setCentralWidget(mainForm)

    def linkHoverd(self):
        print("当鼠标滑过label2时，触发事件")

    def linkClicked(self):
        print("当鼠标单击label4时，触发事件")


    #     self.button1 = QPushButton("退出")
    #     self.button1.clicked.connect(self.onClick_Buttton)
    #
    #     QToolTip.setFont(QFont("SansSerif", 12))
    #     self.setToolTip("这是<b>主窗口</b>")
    #     self.button1.setToolTip("点击退出！")
    #
    #     layout = QHBoxLayout()
    #     layout.addWidget(self.button1)
    #
    #     mainForm = QWidget()
    #     mainForm.setLayout(layout)
    #     self.setCentralWidget(mainForm)
    #
    # # 按钮单击事件方法()槽
    # def onClick_Buttton(self):
    #     sender = self.sender()
    #     print(sender.text() + "按钮被按下")
    #     app = QApplication.instance()
    #     # 退出应用程序
    #     app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = QLabelDemo()
    main_win.show()
    sys.exit(app.exec_())
