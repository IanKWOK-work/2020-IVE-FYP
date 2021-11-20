#!/usr/bin/python

import os
import sys
import time
import subprocess
import paho.mqtt.client as mqtt

try:
    import Adafruit_DHT
except ImportError:
    subprocess.call([sys.executable, "-m", "pip", "install", "Adafruit_DHT"])
finally:
    import Adafruit_DHT

# Define sensor
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 17  # GPIO17, 11th


# Define event callbacks
def on_connect(mosq, obj, flags, rc):
    print ('on_connect:: Connected with result code ' + str(rc))
    print('rc: ' + str(rc))


def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))


def on_log(mosq, obj, level, string):
    print(string)


client = mqtt.Client()
# Assign event callbacks
client.on_connect = on_connect
client.on_publish = on_publish

# Uncomment to enable debug messages
client.on_log = on_log

# Connect to the Broker
client.connect('localhost', 1883, 60)
time.sleep(1)

client.loop_start()

run = True

try:
    record = open('/home/pi/humidity.csv', 'a+')
    if os.stat('/home/pi/humidity.csv').st_size == 0:
        record.write('Date,Time,Temperature,Humidity\r\n')
except:
    pass

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

        if humidity is not None and temperature is not None:
            if humidity <= 3000:
                print("Temperature={0:0.1f}C  Humidity={1:0.1f}%".format(temperature, humidity))
                record.write('{0}, {1}, {2:0.1f}C, {3:0.1f}%\r\n'.format(time.strftime('%d/%m/%Y'),
                                                                         time.strftime('%H:%M:%S'), temperature,
                                                                         humidity))
                # Send messages to the Broker
                client.publish("/IoTSensor/DHT22","Time={0} Temperature={1:0.1f}C Humidity={2:0.1f}%".format(time.strftime('%H:%M:%S'),temperature, humidity))

        else:
            print("Failed to retrieve data from humidity sensor")

        time.sleep(10)

except KeyboardInterrupt:
    print ('exiting')
    client.disconnect()
    client.loop_stop()
