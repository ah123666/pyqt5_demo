import sys
import CalculatorWin
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = CalculatorWin.Ui_CalculatorWin()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
