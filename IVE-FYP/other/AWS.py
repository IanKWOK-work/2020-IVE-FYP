#!/usr/bin/python
import os
import json
import ssl
import sys
import subprocess
import time
from datetime import date, datetime

try:
    import Adafruit_DHT
except ImportError:
    subprocess.call([sys.executable, "-m", "pip", "install", "Adafruit_DHT"])
finally:
    import Adafruit_DHT

try:
    from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
except ImportError:
    subprocess.call([sys.executable, "-m", "pip", "install", "AWSIoTPythonSDK"])
finally:
    from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# ****************************************************
# Set Pin No, AWS Config
# ****************************************************

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 17  # GPIO17, 11th

# ****************************************************
# Set AWS Connection
# ****************************************************

myMQTTClient = AWSIoTMQTTClient("Navio")
myMQTTClient.configureEndpoint("a1v0bqj6bq2xv9-ats.iot.us-west-2.amazonaws.com", 8883)
myMQTTClient.configureCredentials("/home/pi/connect_device_package/root-CA.crt",
                                  "/home/pi/connect_device_package/Navio.private.key",
                                  "/home/pi/connect_device_package/Navio.cert.pem")
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

# connect and publish
myMQTTClient.connect()
myMQTTClient.publish("Navio/DHT22", "connected", 0)

# ****************************************************
# Publish AWS
# ****************************************************

try:
    record = open('/home/pi/humidity.csv', 'a+')
    if os.stat('/home/pi/humidity.csv').st_size == 0:
        record.write('Date,Time,Temperature,Humidity\r\n')
except:
    pass

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    now = datetime.utcnow()
    now_str = now.strftime('%Y-%m-%dT%H:%M:%SZ')  # e.g. 2016-04-18T06:12:25.877Z

    if humidity is not None and temperature is not None:
        if humidity <= 3000:
            print("Temperature={0:0.1f}\N{DEGREE SIGN}C  Humidity={1:0.1f}%".format(temperature, humidity))
            record.write('{0}, {1}, {2:0.1f}\N{DEGREE SIGN}C, {3:0.1f}%\r\n'.format(time.strftime('%d/%m/%Y'),
                                                                                    time.strftime('%H:%M:%S'),
                                                                                    temperature, humidity))

            payload = '{ "timestamp": "' + now_str + '","temperature": ' + "{:.2f}".format(
                temperature) + ',"humidity": ' + "{:.2f}".format(humidity) + ' }'
            print(payload)
            myMQTTClient.publish("Navio/DHT22", payload, 0)
    else:
        print("Failed to retrieve data from humidity sensor")

    time.sleep(10)
