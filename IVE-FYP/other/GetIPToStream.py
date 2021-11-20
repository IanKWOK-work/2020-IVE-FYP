#!/usr/bin/python3
from re import L
from other.gstreamcam import main as gst
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


def getIP():
    leases = list()
    for line in ip("neigh", "show", "dev", "ap0"):
        elements = line.split()
        leases.append(elements[0])

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

    myClass.hostname = getIP()
    gst(myClass)


if __name__ == "__main__":
    main()
