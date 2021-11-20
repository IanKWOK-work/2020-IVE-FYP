import paho.mqtt.client as mqtt, os
import time


# Define event callbacks
def on_connect(mosq, obj, flags, rc):
    print('on_connect:: Connected with result code ' + str(rc))
    print('rc: ' + str(rc))


def on_message(mosq, obj, msg):
    print('on_message:: this means  I got a message from broker for this topic')
    print(msg.topic + ' ' + str(msg.qos) + ' ' + str(msg.payload))


def on_subscribe(mosq, obj, mid, granted_qos):
    print('This means broker has acknowledged my subscribe request')
    print('Subscribed: ' + str(mid) + ' ' + str(granted_qos))


def on_log(mosq, obj, level, string):
    print(string)


def main():
    client = mqtt.Client()
    # Assign event callbacks
    client.on_message = on_message
    client.on_connect = on_connect
    client.on_subscribe = on_subscribe

    # Uncomment to enable debug messages
    client.on_log = on_log

    # Connect to the Broker
    # client.connect('192.168.12.1', 1883, 60)
    client.connect('navio.local', 1883, 60)

    client.loop_start()  # start the loop

    # Subscribe to messages
    client.subscribe('/IoTSensor/DHT22', 0)

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print('exiting')
        client.disconnect()
        client.loop_stop()



