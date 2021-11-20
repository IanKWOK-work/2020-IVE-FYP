import sys
from MainWindow import MainWindow
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = MainWindow.MainWindow()
    ui.setupUi(MainWindow)
    #ui.start()
    MainWindow.show()
    sys.exit(app.exec_())

