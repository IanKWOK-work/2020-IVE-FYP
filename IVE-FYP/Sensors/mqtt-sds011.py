#!/usr/bin/python
from __future__ import print_function
import os
import time
import paho.mqtt.client as mqtt
from sds011 import SDS011

# Define SDS011
sensor = SDS011("/dev/ttyUSB0", use_query_mode=True)


# Define event callbacks
def on_connect(mosq, obj, flags, rc):
    print('on_connect:: Connected with result code ' + str(rc))
    print('rc: ' + str(rc))


def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))


def on_log(mosq, obj, level, string):
    print(string)


if __name__ == "__main__":
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
        record = open('/home/pi/pm25.csv', 'a+')
        if os.stat('/home/pi/pm25.csv').st_size == 0:
            record.write('Date,Time,PM2.5,PM10\r\n')
    except:
        pass

    sensor.sleep(sleep=False)

    try:
        i = 0
        while True:
            sensor.sleep(sleep=False)
            for t in range(20):
                values = sensor.query()
                if values is not None and len(values) == 2 and values[0] != 0 and i > 4:
                    print("PM2.5: ", values[0], ", PM10: ", values[1])
                    record.write('{0}, {1}, {2:0.1f}C, {3:0.1f}%\r\n'.format(time.strftime('%d/%m/%Y'),
                                                                             time.strftime('%H:%M:%S'), values[0],
                                                                             values[1]))
                    # Send messages to the Broker
                    client.publish("/IoTSensor/SDS011",
                                   "Time={0} PM25={1:0.1f} PM10={2:0.1f}".format(time.strftime('%H:%M:%S'), values[0],
                                                                                 values[1]))
                    time.sleep(2)

                i += 1

            print("Going to sleep for 1 min...")
            sensor.sleep()
            time.sleep(60)


    except KeyboardInterrupt:
        print('exiting')
        sensor.sleep()
        client.disconnect()
        client.loop_stop()
