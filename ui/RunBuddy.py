import sys
import Buddy
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = QMainWindow()

    ui = Buddy.Ui_Form()
    ui.setupUi(main_window)

    main_window.setWindowTitle("Buddy")
    main_window.show()
    sys.exit(app.exec_())
