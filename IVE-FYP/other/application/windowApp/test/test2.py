import sys

from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication

from PyQt5.QtGui import QIcon


class Menu(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        exitAct = QAction(QIcon('exit.png'), ' &Quit', self)

        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False) #False for current window, True for parent window
        #self.menubar.setNativeMenuBar(False) #False for current window, True for parent window
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        bar = self.menuBar()
        file = bar.addMenu("Edit")
        file.addAction("New")

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Menu()
    sys.exit(app.exec_())