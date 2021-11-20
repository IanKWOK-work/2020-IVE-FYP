#!/usr/bin/python

import os
import sys
import time
import subprocess

try:
    import Adafruit_DHT
except ImportError:
    subprocess.call([sys.executable, "-m", "pip", "install", "Adafruit_DHT"])
finally:
    import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 17  # GPIO17, 11th

try:
    record = open('/home/pi/humidity.csv', 'a+')
    if os.stat('/home/pi/humidity.csv').st_size == 0:
        record.write('Date,Time,Temperature,Humidity\r\n')
except:
    pass

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        if humidity <= 3000:
            print("Temperature={0:0.1f}C  Humidity={1:0.1f}%".format(temperature, humidity))
            record.write('{0}, {1}, {2:0.1f}C, {3:0.1f}%\r\n'.format(time.strftime('%d/%m/%Y'),
                                                                     time.strftime('%H:%M:%S'), temperature,
                                                                     humidity))
    else:
        print("Failed to retrieve data from humidity sensor")

    time.sleep(30)  # 5
