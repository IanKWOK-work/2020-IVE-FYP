from PyQt5.QtCore import pyqtSignal, QObject
import time


class VehicleLocation(QObject):
    updateMap = pyqtSignal(object)
    exist = False

    def run(self):
        while True:
            if (self.exist):
                detail = {"location_lat": self.vehicle.location.global_frame.lat,
                          "location_lon": self.vehicle.location.global_frame.lon}
            else:
                detail = {"location_lat": "", "location_lon": ""}
            self.updateMap.emit(detail)
            time.sleep(5)

    def setVehicle(self, vehicle):
        self.vehicle = vehicle
        self.exist = True
