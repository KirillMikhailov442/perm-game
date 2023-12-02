import sys
from PyQt5 import QtWidgets
from launcher import Ui_MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()

    ui_main = Ui_MainWindow()
    ui_main.setupUi(main_window)
    main_window.show()
    
    sys.exit(app.exec_())