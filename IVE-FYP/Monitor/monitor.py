# -*- coding: utf-8 -*-
import math
import os
import time
from datetime import datetime
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QApplication, QMainWindow, QWidget

from drone import Drone
from vehicleStatus import VehicleStatus
from vehicleLocation import VehicleLocation

from pyqtlet import L, MapWidget

import gi
from gi.overrides import Gtk

gi.require_version('Gst', '1.0')
gi.require_version('GstVideo', '1.0')
from gi.repository import Gst, GObject, GstVideo

GObject.threads_init()
Gst.init(None)

from mqttClient import MqttClient
from plotCanvas import PlotCanvas

from threadGUI import ThreadGUI
from qfi import qfi_ADI, qfi_ALT, qfi_SI, qfi_HSI, qfi_VSI, qfi_TC


class Monitor(QMainWindow):
    def setupUi(self, MainWindow):
        self.drone = None
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1792, 1008)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_1 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_1.setObjectName("gridLayout_1")

        # creat Simple Window
        self.container = QWidget(self)
        self.container.setFixedSize(854,480)
        self.container.setWindowTitle('Test1')

        # container.connect('destroy', self.quit)
        self.setCentralWidget(self.container)
        self.winId = self.container.winId()
        #self.resize(480, 320)

        # Create GStreamer pipeline
        self.videoPipeline()

        # Create bus to get events from GStreamer pipeline
        self.bus = self.pipeline.get_bus()
        self.bus.add_signal_watch()
        self.bus.enable_sync_message_emission()
        self.bus.connect('message::error', self.on_error)
        self.bus.connect('message::eos', self.on_eos)
        self.bus.connect('sync-message::element', self.on_sync_message)

        # uav detail ui
        self.gridLayout = QtWidgets.QGridLayout()

        self.adi = qfi_ADI.qfi_ADI(self)
        self.adi.resize(240, 240)
        self.adi.reinit()
        self.gridLayout.addWidget(self.adi, 0, 0)

        self.alt = qfi_ALT.qfi_ALT(self)
        self.alt.resize(240, 240)

        self.alt.reinit()
        self.gridLayout.addWidget(self.alt, 0, 1)

        self.hsi = qfi_HSI.qfi_HSI(self)
        self.hsi.resize(240, 240)
        self.hsi.reinit()
        self.gridLayout.addWidget(self.hsi, 0, 2)

        self.si = qfi_SI.qfi_SI(self)
        self.si.resize(240, 240)
        self.si.reinit()
        self.gridLayout.addWidget(self.si, 1, 0,1,2,alignment=QtCore.Qt.AlignCenter)

        self.vsi = qfi_VSI.qfi_VSI(self)
        self.vsi.resize(240, 240)
        self.vsi.reinit()
        self.gridLayout.addWidget(self.vsi, 1, 1,1,2,alignment=QtCore.Qt.AlignCenter)

        self.tc = qfi_TC.qfi_TC(self)
        self.tc.resize(240, 240)
        self.tc.reinit()

        self.setLayout(self.gridLayout)

        # end uav detail ui


        self.gridLayout_1.addWidget(self.container,0,0)
        self.gridLayout_1.addLayout(self.gridLayout,0,1)

        # Map
        self.mapWidget = MapWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.mapWidget.sizePolicy().hasHeightForWidth())
        self.mapWidget.setSizePolicy(sizePolicy)
        self.gridLayout_1.addWidget(self.mapWidget,1,0)
        self.map = L.map(self.mapWidget)

        self.map.setView([22.305711, 114.253426], 20)
        L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(self.map)

        self.marker = L.marker([22.305711, 114.253426])
        self.marker.bindPopup('No connection')
        self.map.addLayer(self.marker)
        self.count = 0

        #build scrollArea which is placed the graphs
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 849, 1024))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_graphs = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_graphs.setObjectName("verticalLayout_graphs")

        # draw graphs
        # 1 PM2.5
        self.data_pm25 = []
        self.data_pm25_time = []
        self.data_pm25_collectTime = []
        self.canvas_pm25 = PlotCanvas(self, width=1, height=4)
        self.canvas_pm25.init_plot("PM2.5", "µg/m³", "Time(s)")
        self.canvas_pm25.setMinimumSize(self.canvas_pm25.size())
        self.verticalLayout_graphs.addWidget(self.canvas_pm25)
        # 2 PM10
        self.data_pm10 = []
        self.data_pm10_time = []
        self.data_pm10_collectTime = []
        self.canvas_pm10 = PlotCanvas(self, width=1, height=4)
        self.canvas_pm10.init_plot("PM10", "µg/m³", "Time(s)")
        self.canvas_pm10.setMinimumSize(self.canvas_pm10.size())
        self.verticalLayout_graphs.addWidget(self.canvas_pm10)
        # 3 temperature
        self.data_temp = []
        self.data_temp_time = []
        self.data_temp_collectTime = []
        self.canvas_temp = PlotCanvas(self, width=1, height=4)
        self.canvas_temp.init_plot("Temperature", "Temperature(C)", "Time(s)")
        self.canvas_temp.setMinimumSize(self.canvas_temp.size())
        self.verticalLayout_graphs.addWidget((self.canvas_temp))
        # 4 humidity
        self.data_hum = []
        self.data_hum_time = []
        self.data_hum_collectTime = []
        self.canvas_hum = PlotCanvas(self, width=1, height=4)
        self.canvas_hum.init_plot("Humidity", "Humidity(%)", "Time(s)")
        self.canvas_hum.setMinimumSize(self.canvas_hum.size())
        self.verticalLayout_graphs.addWidget((self.canvas_hum))

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_1.addWidget(self.scrollArea,1,1)

        # Menu
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

        # new mission
        self.actionNew_Mission = QtWidgets.QAction(MainWindow)
        self.actionNew_Mission.setObjectName("actionNew_Mission")
        self.actionNew_Mission.triggered.connect(self.newMission)
        self.actionView_Mission = QtWidgets.QAction(MainWindow)
        self.actionView_Mission.setObjectName("actionView_Mission")

        # save as
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.triggered.connect(self.saveAs)

        # quit
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionClose.triggered.connect(QApplication.quit)

        # connect
        self.actionConnect = QtWidgets.QAction(MainWindow)
        self.actionConnect.setObjectName("actionConnect")
        self.actionConnect.triggered.connect(self.connect)

        #disconnect
        self.actionDisconnect = QtWidgets.QAction(MainWindow)
        self.actionDisconnect.setObjectName("actionDisconnect")
        self.actionDisconnect.triggered.connect(self.disconnect)

        self.menuMission.addAction(self.actionNew_Mission)
        self.menuMission.addAction(self.actionSave)
        self.menuMission.addAction(self.actionClose)
        self.menuConnection.addAction(self.actionConnect)
        self.menuConnection.addAction(self.actionDisconnect)
        self.menubar.addAction(self.menuMission.menuAction())
        self.menubar.addAction(self.menuConnection.menuAction())

        # menu button setting
        self.actionConnect.setDisabled(False)
        self.actionDisconnect.setDisabled(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.menubar.setNativeMenuBar(False)  # False for current window, True for parent window

        # update detail
        self.updateQFI_thread = VehicleStatus()
        self.updateQFI_thread.updateQFI.connect(self.updateQFI)
        self.updateMap_thread = VehicleLocation()
        self.updateMap_thread.updateMap.connect(self.updateMap)

        #build thread
        self.thread1 = QThread()
        self.thread2 = QThread()
        self.updateQFI_thread.moveToThread(self.thread1)
        self.updateMap_thread.moveToThread(self.thread2)

        # start thread
        self.thread1.started.connect(self.updateQFI_thread.run)
        self.thread1.start()
        self.thread2.started.connect(self.updateMap_thread.run)
        self.thread2.start()

        MainWindow.setCentralWidget(self.centralwidget)


    @QtCore.pyqtSlot(int)
    def on_stateChanged(self, state):
        if state == MqttClient.Connected:
            print(state)
            self.client.subscribe([("/IoTSensor/DHT22",0),("/IoTSensor/SDS011",1)])

    @QtCore.pyqtSlot(str)
    def on_messageSignal(self, msg):
        val = msg
        print(val)
        type = val.split(" ")[1].split("=")[0]
        if type == "Temperature":
            val = val.replace("Time=", "")
            val = val.replace("Temperature=", "")
            val = val.replace("Humidity=", "")
            val = val.split(" ")
            sTime = val[0] #String format
            dTime = datetime.strptime(sTime, '%H:%M:%S') #Time format
            temp = val[1].replace("C", "")
            hum = val[2].replace("%", "")
            self.storeData(self.data_temp,temp,self.data_temp_time,self.data_temp_collectTime,sTime,dTime)
            self.storeData(self.data_hum,hum, self.data_hum_time, self.data_hum_collectTime, sTime, dTime)
        elif type == "PM25":
            val = val.replace("Time=", "")
            val = val.replace("PM25=", "")
            val = val.replace("PM10=", "")
            val = val.split(" ")
            sTime = val[0] #String format
            dTime = datetime.strptime(sTime, '%H:%M:%S') #Time format
            pm25 = val[1]
            pm10 = val[2]
            self.storeData(self.data_pm25,pm25,self.data_pm25_time,self.data_pm25_collectTime,sTime,dTime)
            self.storeData(self.data_pm10,pm10,self.data_pm10_time,self.data_pm10_collectTime,sTime,dTime)
        self.draw()


    def storeData(self, target, data,target_time,target_collectTime, sTime,dTime):
        print(data)
        target.append(float(data))

        if (len(target_time) != 0):
            lTime = datetime.strptime(target_collectTime[-1], '%H:%M:%S') #lastest collect time
            timeDiff = dTime-lTime
            target_time.append(target_time[-1] + int(str(timeDiff.seconds)))
            target_collectTime.append(sTime)
        else:
            print('first')
            target_time.append(0)
            target_collectTime.append(sTime)

    def draw(self):
        # print("draw")
        self.canvas_pm25.update_figure(self.data_pm25_time,self.data_pm25)
        self.canvas_pm10.update_figure(self.data_pm10_time, self.data_pm10)
        self.canvas_temp.update_figure(self.data_temp_time, self.data_temp)
        self.canvas_hum.update_figure(self.data_hum_time, self.data_hum)

    def saveAs(self):
        path = QFileDialog.getExistingDirectory(self, 'Choose Directory')
        directory = time.strftime('%d-%m-%Y') + ' ' + time.strftime('%H-%M-%S')

        if path != "":
            path = path + "/" + directory
            os.mkdir(path)
            record = open(path + "/" + 'raw_data.txt', 'a+')
            output_temp = ""
            output_hum = ""
            output_pm25 = ""
            output_pm10 = ""
            output_temp_collectTime = ""
            output_hum_collectTime = ""
            output_pm25_collectTime = ""
            output_pm10_collectTime = ""

            if len(self.data_temp) != 0:
                output_temp = ["%.1f" % number for number in self.data_temp]
                output_temp = ','.join(output_temp)
                output_temp_collectTime = ','.join(self.data_temp_collectTime)
            if len(self.data_hum) != 0:
                output_hum = ["%.1f" % number for number in self.data_hum]
                output_hum = ','.join(output_hum)
                output_hum_collectTime = ','.join(self.data_hum_collectTime)
            if len(self.data_pm25) != 0:
                output_pm25 = ["%.1f" % number for number in self.data_pm25]
                output_pm25 = ','.join(output_pm25)
                output_pm25_collectTime = ','.join(self.data_pm25_collectTime)
            if len(self.data_pm10) != 0:
                output_pm10 = ["%.1f" % number for number in self.data_pm10]
                output_pm10 = ','.join(output_pm10)
                output_pm10_collectTime = ','.join(self.data_pm10_collectTime)


            output = "{\n" \
                     "\"Temperature\":{" \
                     "\n\t\"Data\":[" + output_temp + "],\n\t\"Unit\":C," \
                     "\n\t\"CollectedTime\":["+output_temp_collectTime+"]\n\t}"\
                     "\n\"Humidity\":{"\
                     "\n\t\"Data\":[" + output_hum + "],\n\t\"Unit\":%,"\
                     "\n\t\"CollectedTime\":["+output_hum_collectTime+"]\n\t}" \
                     "\n\"PM2.5\":{" \
                     "\n\t\"Data\":[" + output_pm25 + "],\n\t\"Unit\":µg/m³," \
                     "\n\t\"CollectedTime\":[" + output_pm25_collectTime + "]\n\t}" \
                     "\n\"PM10\":{" \
                     "\n\t\"Data\":[" + output_pm10 + "],\n\t\"Unit\":µg/m³," \
                     "\n\t\"CollectedTime\":[" + output_pm10_collectTime + "]\n\t}" \
                     "\n}"
            record.write(output)
            self.canvas_temp.outputImage(path + "/" + "Temperature")
            self.canvas_hum.outputImage(path + "/" + "Humidity")
            self.canvas_pm25.outputImage(path + "/" + "PM2.5")
            self.canvas_pm10.outputImage(path + "/" + "PM10")

    def newMission(self):
        msgBox = QMessageBox()
        msgBox.setText("Do you want to create a new mission now? If yes, then the current mission will be closed.")
        msgBox.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        option = msgBox.exec_()
        if option == QMessageBox.Ok:
            # os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
            os.execl(sys.executable, sys.executable, *sys.argv)
            # os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)

    def videoPipeline(self):
        self.pipeline = Gst.Pipeline()
        self.tcpsrc = Gst.ElementFactory.make('tcpclientsrc', 'tcpsrc')
        self.tcpsrc.set_property("host", '192.168.12.1')
        self.tcpsrc.set_property("port", 5000)

        self.gdepay = Gst.ElementFactory.make('gdpdepay', 'gdepay')
        self.rdepay = Gst.ElementFactory.make('rtph264depay', 'rdepay')
        self.avdec = Gst.ElementFactory.make('avdec_h264', 'avdec')
        self.vidconvert = Gst.ElementFactory.make('videoconvert', 'vidconvert')
        self.asink = Gst.ElementFactory.make('autovideosink', 'asink')
        self.asink.set_property('sync', False)

        self.pipeline.add(self.tcpsrc)
        self.pipeline.add(self.gdepay)
        self.pipeline.add(self.avdec)
        self.pipeline.add(self.rdepay)
        self.pipeline.add(self.vidconvert)
        self.pipeline.add(self.asink)

        self.tcpsrc.link(self.gdepay)
        self.gdepay.link(self.rdepay)
        self.rdepay.link(self.avdec)
        self.avdec.link(self.vidconvert)
        self.vidconvert.link(self.asink)

    def on_sync_message(self, bus, message):
        if message.get_structure().get_name() == 'prepare-window-handle':
            message.src.set_property('force-aspect-ratio', True)
            message.src.set_window_handle(self.winId)

    def quit(self, container):
        self.pipeline.set_state(Gst.State.NULL)
        Gtk.main_quit()

    def on_eos(self, bus, msg):
        print('on_eos(): seeking to start of video')
        self.pipeline.seek_simple(
            Gst.Format.TIME,
            Gst.SeekFlags.FLUSH | Gst.SeekFlags.KEY_UNIT,
            0
        )

    def on_error(self, bus, msg):
        print('on_error():', msg.parse_error())

    def start(self):
        self.pipeline.set_state(Gst.State.PLAYING)

    def updateQFI(self, detail):
        if(detail["airspeed"] != ""):
            self.adi.setRoll(math.degrees(detail["attitude_roll"]))
            self.adi.setPitch(math.degrees(detail["attitude_pitch"]))
            self.alt.setAltitude(detail["altitude"])
            self.si.setSpeed(detail["airspeed"])
            self.hsi.setHeading(detail["heading"])
            self.vsi.setClimbRate(detail["verticalSpeed"])

            self.adi.viewUpdate.emit()
            self.alt.viewUpdate.emit()
            self.si.viewUpdate.emit()
            self.hsi.viewUpdate.emit()
            self.vsi.viewUpdate.emit()

    def updateMap(self, detail):

        # Working with the maps with pyqtlet
        if (detail["location_lat"] != ""):
            self.map.removeLayer(self.marker)
            if self.count == 0:
                self.map.setView([detail["location_lat"], detail["location_lon"]], 20)
            self.count += 1
            if self.count % 10 == 0:
                self.map.setView([detail["location_lat"], detail["location_lon"]], 20)
            self.marker = L.marker([detail["location_lat"], detail["location_lon"]])
            self.marker.bindPopup('UAV Here')
            self.map.addLayer(self.marker)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Automated Data Collecting System"))
        self.menuMission.setTitle(_translate("MainWindow", "Mission"))
        self.menuConnection.setTitle(_translate("MainWindow", "Connection"))
        self.actionNew_Mission.setText(_translate("MainWindow", "New Mission"))
        self.actionView_Mission.setText(_translate("MainWindow", "View Mission"))
        self.actionSave.setText(_translate("MainWindow", "Save As"))
        self.actionClose.setText(_translate("MainWindow", "Quit"))
        self.actionConnect.setText(_translate("MainWindow", "Connect"))
        self.actionDisconnect.setText(_translate("MainWindow", "Disconnect"))

    def connect(self):
        self.drone = Drone('udp:0.0.0.0:14550')
        if self.drone.isconnect == True:
            self.vehicle = self.drone.getDrone()
            self.actionConnect.setDisabled(True)
            self.actionDisconnect.setDisabled(False)

            #MQtt start
            self.client = MqttClient(self)
            self.client.stateChanged.connect(self.on_stateChanged)
            self.client.messageSignal.connect(self.on_messageSignal)
            self.client.hostname = "192.168.12.1"
            self.client.connectToHost()

            #start Map and QFI
            self.updateMap_thread.setVehicle(self.vehicle)
            self.updateQFI_thread.setVehicle(self.vehicle)
            self.start()

            # Animation thread
            t2 = ThreadGUI(self.gridLayout)
            t2.daemon = True
            t2.start()
        else:
            self.disconnect()


    def disconnect(self):
        self.drone.disconnectDrone()
        self.actionConnect.setDisabled(False)
        self.actionDisconnect.setDisabled(True)
        self.updateMap_thread.exist = False
        self.updateQFI_thread.exist = False
        self.quit(self.container)

        self.adi.setRoll(0)
        self.adi.setPitch(0)
        self.alt.setAltitude(0)
        self.si.setSpeed(0)
        self.hsi.setHeading(0)
        self.vsi.setClimbRate(0)

        self.adi.viewUpdate.emit()
        self.alt.viewUpdate.emit()
        self.si.viewUpdate.emit()
        self.hsi.viewUpdate.emit()
        self.vsi.viewUpdate.emit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Monitor()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
