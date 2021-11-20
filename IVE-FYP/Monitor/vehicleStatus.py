from PyQt5.QtCore import pyqtSignal, QObject
import time


class VehicleStatus(QObject):
    updateQFI = pyqtSignal(object)
    exist = False

    def run(self):
        while True:
            if (self.exist):
                # split attitude
                attitude = str(self.vehicle.attitude).split(':')
                attitude = attitude[1].split('=')
                attitude_pitch = float(attitude[1].split(',')[0])
                attitude_yaw = float(attitude[2].split(',')[0])
                attitude_roll = float(attitude[3].split(',')[0])
                detail = {"airspeed": self.vehicle.airspeed,
                          "attitude_pitch": attitude_pitch,
                          "attitude_yaw": attitude_yaw,
                          "attitude_roll": attitude_roll,
                          "altitude": self.vehicle.location.global_relative_frame.alt,
                          "groundspeed": format(float(self.vehicle.groundspeed), '0.3f'),
                          "heading": self.vehicle.heading,
                          "verticalSpeed": self.vehicle.velocity[2]}
            else:
                detail = {"airspeed": "", "attitude_pitch": "", "attitude_yaw": "", "attitude_roll": "", "altitude": "",
                          "groundspeed": "", "heading": "", "verticalSpeed": ""}

            self.updateQFI.emit(detail)

            time.sleep(0.2)

    def setVehicle(self, vehicle):
        self.vehicle = vehicle
        self.exist = True
