import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QWidget, QPushButton

app = QApplication(sys.argv)
widget = QWidget()

def onClick_Button():
    print("1")
    print("widget.x() = %d" % widget.x())
    print("widget.y() = %d" % widget.y())

btn = QPushButton(widget)
btn.setText("按钮")
btn.move(24, 52)
btn.clicked.connect(onClick_Button)

widget.resize(300, 240)
widget.move(250, 200)
widget.setWindowTitle("屏幕坐标系")
widget.show()

sys.exit(app.exec_())