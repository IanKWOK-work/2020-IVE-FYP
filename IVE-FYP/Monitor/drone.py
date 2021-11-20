
from PyQt5.QtWidgets import QMessageBox
from dronekit import connect


class Drone:
    isconnect = False

    def __init__(self, connection_string):
        self.connection_string = connection_string
        try:
            print("connect")
            self.drone = connect(self.connection_string, wait_ready=True)
            print("connected")
            self.isconnect = True
        except:
            msgBox = QMessageBox()
            msgBox.setText("The connection to the drone timed out.")
            msgBox.exec_()

        # self.sitl = dronekit_sitl.start_default()
        # self.drone = connect('tcp:127.0.0.1:5760', wait_ready=True)

    def connectDrone(self):
        self.drone = connect(self.connection_string, wait_ready=True)

    def getDrone(self):
        return self.drone

    def disconnectDrone(self):
        if self.isconnect == True:
            self.drone.close()
        #self.sitl.stop()

