#!/usr/bin/python3
import datetime
from re import L
import sys
import subprocess

try:
    from sh import ip
except ImportError:
    subprocess.call([sys.executable, "-m", "pip", "install", "sh"])
finally:
    from sh import ip

try:
    import picamera
except ImportError:
    subprocess.call([sys.executable, "-m", "pip", "install", "picamera"])
finally:
    import picamera

DNSMASQ_LEASES_FILE = "/var/lib/misc/dnsmasq.leases"


class LeaseEntry:
    def __init__(self, leasetime, macAddress, ipAddress, name):
        if (leasetime == '0'):
            self.staticIP = True
        else:
            self.staticIP = False
        self.leasetime = datetime.datetime.fromtimestamp(
            int(leasetime)
        ).strftime('%Y-%m-%d %H:%M:%S')
        self.macAddress = macAddress.upper()
        self.ipAddress = ipAddress
        self.name = name

    def serialize(self):
        return {
            'staticIP': self.staticIP,
            'leasetime': self.leasetime,
            'macAddress': self.macAddress,
            'ipAddress': self.ipAddress,
            'name': self.name
        }


def leaseSort(arg):
    # Fixed IPs first
    if arg.staticIP == True:
        return '0' + arg.ipAddress
    else:
        return arg.ipAddress


def getLeases():
    leases = list()
    with open(DNSMASQ_LEASES_FILE) as f:
        for line in f:
            elements = line.split()
            if len(elements) == 5:
                entry = LeaseEntry(elements[0],
                                   elements[1],
                                   elements[2],
                                   elements[3])
                leases.append(entry)
    leases.sort(key=leaseSort)
    leases = [lease.serialize() for lease in leases]
    return leases


class myClass(list):
    def __new__(self, *args, **kwargs):
        return super(L, self).__new__(self, args, kwargs)

    def __init__(self, *args, **kwargs):
        if len(args) == 1 and hasattr(args[0], '__iter__'):
            list.__init__(self, args[0])
        else:
            list.__init__(self, args)
        self.__dict__.update(kwargs)

    def __call__(self, **kwargs):
        self.__dict__.update(kwargs)
        return self


def main():
    myClass.hostname = ""
    myClass.codec = "h264"
    myClass.debug = ""
    myClass.sdp = ""
    ipAddress = list()
    for item in getLeases():
        print(item['ipAddress'])
        ipAddress.append(item['ipAddress'])

    myClass.hostname = ipAddress
    # print(ipAddress)
    print(myClass.hostname)
    # gst.main(myClass)
    print(ip("neigh", "show", "dev", "wlan0"))


if __name__ == "__main__":
    main()
