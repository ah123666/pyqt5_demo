import sys
import TestSizePolicy
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    
    ui = TestSizePolicy.Ui_MianWin()
    ui.setupUi(main_window)
    
    main_window.setWindowTitle("TestSizePolicy")
    main_window.show()
    sys.exit(app.exec_())
