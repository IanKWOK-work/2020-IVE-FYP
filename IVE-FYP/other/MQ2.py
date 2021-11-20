#!/usr/bin/python
import RPi.GPIO as GPIO
import time

MQ_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(MQ_PIN,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        status = GPIO.input(MQ_PIN)
        #print(status)
        if status ==True:
            print("Nornal")
        else:
            print("dangerous")
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()