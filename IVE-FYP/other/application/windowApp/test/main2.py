import sys
import ui_main
from PyQt5 import QtWidgets
Ui_MainWindow = ui_main.Ui_MainWindow


class CoperQt(QtWidgets.QMainWindow,Ui_MainWindow):#创建一个Qt对象
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)  # 创建主界面对象
        Ui_MainWindow.__init__(self)  # 主界面对象初始化
        self.setupUi(self)  # 配置主界面对象
        #self.label.setText("hi")
        #self.label.text()
        #print(self.label.text())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CoperQt()#创建QT对象
    window.show()#QT对象显示
   #print(window.label.text())
    sys.exit(app.exec_())


