import sys
import MainWin1


from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    ui = MainWin1.Ui_MainWin1()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())
