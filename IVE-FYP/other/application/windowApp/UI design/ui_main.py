# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_newMission.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1792, 1008)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_8.addWidget(self.graphicsView)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_10.addWidget(self.label_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.graphicsView_4.sizePolicy().hasHeightForWidth())
        self.graphicsView_4.setSizePolicy(sizePolicy)
        self.graphicsView_4.setMinimumSize(QtCore.QSize(0, 0))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.verticalLayout_3.addWidget(self.graphicsView_4)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.graphicsView_6 = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.graphicsView_6.sizePolicy().hasHeightForWidth())
        self.graphicsView_6.setSizePolicy(sizePolicy)
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.verticalLayout_3.addWidget(self.graphicsView_6)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.graphicsView_5 = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.graphicsView_5.sizePolicy().hasHeightForWidth())
        self.graphicsView_5.setSizePolicy(sizePolicy)
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.verticalLayout_2.addWidget(self.graphicsView_5)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.graphicsView_7 = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.graphicsView_7.sizePolicy().hasHeightForWidth())
        self.graphicsView_7.setSizePolicy(sizePolicy)
        self.graphicsView_7.setObjectName("graphicsView_7")
        self.verticalLayout_2.addWidget(self.graphicsView_7)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.graphicsView_8 = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.graphicsView_8.sizePolicy().hasHeightForWidth())
        self.graphicsView_8.setSizePolicy(sizePolicy)
        self.graphicsView_8.setObjectName("graphicsView_8")
        self.verticalLayout.addWidget(self.graphicsView_8)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.graphicsView_9 = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.graphicsView_9.sizePolicy().hasHeightForWidth())
        self.graphicsView_9.setSizePolicy(sizePolicy)
        self.graphicsView_9.setObjectName("graphicsView_9")
        self.verticalLayout.addWidget(self.graphicsView_9)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_10.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_10)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_9.addWidget(self.label_9)
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.graphicsView_3.sizePolicy().hasHeightForWidth())
        self.graphicsView_3.setSizePolicy(sizePolicy)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.verticalLayout_9.addWidget(self.graphicsView_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_9)

        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_7.addWidget(self.pushButton)


        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 849, 1024))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")



        #store graphs


        self.verticalLayout_graphs = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_graphs.setObjectName("verticalLayout_graphs")

        """
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.graphicsView_2.sizePolicy().hasHeightForWidth())
        self.graphicsView_2.setSizePolicy(sizePolicy)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout_7.addWidget(self.graphicsView_2)
        """
        #1
        #draw graph
        self.figure = plt.figure(figsize=(1,2.5))
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumSize(self.canvas.size())
        #fig = plt.gcf()
        #fig.set_size_inches(5, 5)
        # self.toolbar = NavigationToolbar(self.canvas, self)
        plt.suptitle("Temperature")

        #test temperature
        data = [random.random() for i in range(10)]
        self.figure.clear()
        plt.suptitle("Temperature (C)")
        y = (25.2,25.3,25.4,25.7,25.6,25.3,25.4,25.6,25.6,25.7)
        x = (5,10,15,20,25,30,35,40,45,50)
        ax = self.figure.add_subplot(111)
        ax.plot(x, y)
        self.canvas.draw()

        #self.button = QPushButton('Plot')
        #self.button.clicked.connect(self.plot)
        # layout = QVBoxLayout()
        # self.verticalLayout_7.addWidget(self.toolbar)
        #self.verticalLayout_7.addWidget(self.canvas)
        self.verticalLayout_graphs.addWidget(self.canvas)

        #2
        # draw graph
        self.figure = plt.figure(figsize=(1,2.5))
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumSize(self.canvas.size())
        # fig = plt.gcf()
        # fig.set_size_inches(5, 5)
        # self.toolbar = NavigationToolbar(self.canvas, self)
        plt.suptitle("Temperature")

        # test temperature
        data = [random.random() for i in range(10)]
        self.figure.clear()
        plt.suptitle("Temperature (C)")
        y = (25.2, 25.3, 25.4, 25.7, 25.6, 25.3, 25.4, 25.6, 25.6, 25.7)
        x = (5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
        ax = self.figure.add_subplot(111)
        ax.plot(x, y)
        self.canvas.draw()
        self.verticalLayout_graphs.addWidget(self.canvas)
        #self.verticalLayout_7.addWidget(self.button)

        #3
        # draw graph
        self.figure = plt.figure(figsize=(1,2.5))
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumSize(self.canvas.size())
        # fig = plt.gcf()
        # fig.set_size_inches(5, 5)
        # self.toolbar = NavigationToolbar(self.canvas, self)
        plt.suptitle("Temperature")

        # test temperature
        data = [random.random() for i in range(10)]
        self.figure.clear()
        plt.suptitle("Temperature (C)")
        y = (25.2, 25.3, 25.4, 25.7, 25.6, 25.3, 25.4, 25.6, 25.6, 25.7)
        x = (5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
        ax = self.figure.add_subplot(111)
        ax.plot(x, y)
        self.canvas.draw()
        self.verticalLayout_graphs.addWidget(self.canvas)
        #self.verticalLayout_7.addWidget(self.button)
        #4
        # draw graph
        self.figure = plt.figure(figsize=(1,2.5))
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumSize(self.canvas.size())
        # fig = plt.gcf()
        # fig.set_size_inches(5, 5)
        # self.toolbar = NavigationToolbar(self.canvas, self)
        plt.suptitle("Temperature")

        # test temperature
        data = [random.random() for i in range(10)]
        self.figure.clear()
        plt.suptitle("Temperature (C)")
        y = (25.2, 25.3, 25.4, 25.7, 25.6, 25.3, 25.4, 25.6, 25.6, 25.7)
        x = (5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
        ax = self.figure.add_subplot(111)
        ax.plot(x, y)
        self.canvas.draw()
        self.verticalLayout_graphs.addWidget(self.canvas)
        #self.verticalLayout_7.addWidget(self.button)
        #5
        # draw graph
        self.figure = plt.figure(figsize=(1,2.5))
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumSize(self.canvas.size())
        # fig = plt.gcf()
        # fig.set_size_inches(5, 5)
        # self.toolbar = NavigationToolbar(self.canvas, self)
        plt.suptitle("Temperature")

        # test temperature
        data = [random.random() for i in range(10)]
        self.figure.clear()
        plt.suptitle("Temperature (C)")
        y = (25.2, 25.3, 25.4, 25.7, 25.6, 25.3, 25.4, 25.6, 25.6, 25.7)
        x = (5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
        ax = self.figure.add_subplot(111)
        ax.plot(x, y)
        self.canvas.draw()
        self.verticalLayout_graphs.addWidget(self.canvas)
        #self.verticalLayout_7.addWidget(self.button)


        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_7.addWidget(self.scrollArea)

        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        #Menu
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1792, 22))
        self.menubar.setObjectName("menubar")
        self.menuMission = QtWidgets.QMenu(self.menubar)
        self.menuMission.setObjectName("menuFile")
        self.menuConnection = QtWidgets.QMenu(self.menubar)
        self.menuConnection.setObjectName("menuConnection")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Mission = QtWidgets.QAction(MainWindow)
        self.actionNew_Mission.setObjectName("actionNew_Mission")
        self.actionView_Mission = QtWidgets.QAction(MainWindow)
        self.actionView_Mission.setObjectName("actionView_Mission")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        #quit
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionClose.triggered.connect(QApplication.quit)
        #connect
        self.actionConnect = QtWidgets.QAction(MainWindow)
        self.actionConnect.setObjectName("actionConnect")


        self.actionConnect.triggered.connect(self.connect)
        #print(" GPS: %s" % self.drone.gps_0)
        self.actionDisconnect = QtWidgets.QAction(MainWindow)
        self.actionDisconnect.setObjectName("actionDisconnect")
        self.menuMission.addAction(self.actionNew_Mission)
        self.menuMission.addAction(self.actionSave)
        self.menuMission.addAction(self.actionClose)
        self.menuConnection.addAction(self.actionConnect)
        self.menuConnection.addAction(self.actionDisconnect)
        self.menubar.addAction(self.menuMission.menuAction())
        self.menubar.addAction(self.menuConnection.menuAction())




        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.menubar.setNativeMenuBar(False)  # False for current window, True for parent window

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Automated Data Collecting System"))
        self.label.setText(_translate("MainWindow", "Streaming"))
        self.label_5.setText(_translate("MainWindow", "UAV Details"))
        self.label_7.setText(_translate("MainWindow", "Airspeed"))
        self.label_6.setText(_translate("MainWindow", "Turn Coordinator"))
        self.label_4.setText(_translate("MainWindow", "Attitude"))
        self.label_3.setText(_translate("MainWindow", "Heading"))
        self.label_8.setText(_translate("MainWindow", "Altitude"))
        self.label_10.setText(_translate("MainWindow", "Vertical Speed"))
        self.label_9.setText(_translate("MainWindow", "Map"))
        self.label_2.setText(_translate("MainWindow", "Data Collection"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.menuMission.setTitle(_translate("MainWindow", "Mission"))
        self.menuConnection.setTitle(_translate("MainWindow", "Connection"))
        self.actionNew_Mission.setText(_translate("MainWindow", "New Mission"))
        self.actionView_Mission.setText(_translate("MainWindow", "View Mission"))
        self.actionSave.setText(_translate("MainWindow", "Output Result"))
        self.actionClose.setText(_translate("MainWindow", "Quit"))
        self.actionConnect.setText(_translate("MainWindow", "Connect"))
        self.actionDisconnect.setText(_translate("MainWindow", "Disconnect"))

    def plot(self):
        data = [random.random() for i in range(10)]
        self.figure.clear()
        plt.suptitle("Temperature (C)")
        ax = self.figure.add_subplot(111)
        ax.plot(data, '*-')
        self.canvas.draw()

    def connect(self):



        print("Start simulator (SITL)")
        import dronekit_sitl
        sitl = dronekit_sitl.start_default()
        connection_string = 'tcp:127.0.0.1:5760'

        from dronekit import connect, VehicleMode
        vehicle = connect(connection_string, wait_ready=True)


        # Get some vehicle attributes (state)
        print("Get some vehicle attribute values:")
        print(" GPS: %s" % vehicle.gps_0)
        print(" Battery: %s" % vehicle.battery)
        print(" Last Heartbeat: %s" % vehicle.last_heartbeat)
        print(" Is Armable?: %s" % vehicle.is_armable)
        print(" System status: %s" % vehicle.system_status.state)
        print(" Mode: %s" % vehicle.mode.name)  # settable

        # Close vehicle object before exiting script
        vehicle.close()

        # Shut down simulator
        sitl.stop()
        print("Completed")

import dronekit_sitl
from dronekit import connect, VehicleMode
class Drone:

    def __init__(self,conection_string):
        self.conection_string=conection_string
        sitl = dronekit_sitl.start_default()

    def connectDrone(self):
        drone = connect(self.connection_string, wait_ready=True)

    def getDrone(self):
        return self.drone
    def disconnectDrone(self):
        self.drone.close()
        self.sitl.stop()