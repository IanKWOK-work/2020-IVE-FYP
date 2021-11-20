from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import QUrl
from PyQt5 import QtWebEngineWidgets,QtWidgets
from PyQt5.QtWidgets import QApplication

app = QApplication([])
view = QtWebEngineWidgets.QWebEngineView()
view.setGeometry(100,150,1280,550)
url="http://google.com"
view.setWindowTitle("Browser"+url)
view.setUrl(QtWidgets.QMainWindow.Qurl(url))
#view.load()
view.show()
app.exec_()