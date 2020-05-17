#!/bin/bash

raspivid -t 999999 -w 1080 -h 720 -fps 25 -hf -b 2000000 -o - | \gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 \! gdppay ! tcpserversink host=192.168.12.1 port=5000