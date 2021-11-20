
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView,QWebEnginePage as QWebPage
import sys
from PyQt5 import QtGui, QtCore, QtWebEngineWidgets



class Support(QtGui.QtWebEngineWidgets):

    def __init__(self, parent=None):
        super(Support, self).__init__(parent)

        self.supportTab()


    def supportTab(self):

        view = QtWebEngineWidgets.QWebView()

        url = "http://www.google.com"
        view.load(QtCore.QUrl(url))

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(view)

        self.setLayout(vbox)