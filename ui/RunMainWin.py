import sys
import MainWin


from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    ui = MainWin.Ui_MainWin()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())
