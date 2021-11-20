# FYP - Automated Data Collecting System for Environment Using UAVs and Smartphones

IVE(LWL), Software Engineering, Final Year Project

## Collaborators

* **Siu Chi Wang** - *Streaming, IoT, UAV, README* - [wing199901](https://github.com/wing199901)
* **Wong Ming Yuen** - *Initial work, GUI, Charts & Graphs* - [Ethan7102](https://github.com/Ethan7102)
* **Kwok Tsz Lung** - *???* - [BirdyKwok](https://github.com/BirdyKwok)
* **Chau Yat Sum** - *???* - [NathMon](https://github.com/NathMon)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Hardware

``` 

1\. a Raspberry Pi 3B+
2\. a Raspberry Pi Camera Module
3\. a Navio2 Autopilot HAT
4\. a high power wireless USB adapter(Alfa AWUS036NHA)
5\. a DIY quadcopter
6\. a 4s battery
7\. a laptop
8\. a Smartphone
9\. DHT22 sensor
10. SDS011 sensor

```

Software

``` 

1\. Python3(3.8) 
2\. QGroundControl
3\. Mission Planner
4\. Terminal

```

## Installing

### UAV Side Configuration

#### Raspberry Pi Configuration

Navio requires a preconfigured Raspbian to run. Emlid provide a unified SD card image for Raspberry Pi.

Follow the instruction to configure your Raspberry Pi
(https://docs.emlid.com/navio2/common/ardupilot/configuring-raspberry-pi/)

``` 
If you want to use SSH to remote access your Raspberry Pi, placing a file named 'ssh' into the boot partition.
```

#### Configure Access Point(AP)

We choose to use create_ap to create an access point, because it provides a simple way to do thing easier.

``` 
git clone https://github.com/oblique/create_ap
cd create_ap
make install
```

The basic syntax to create a NATed virtual network is the following:

``` 
create_ap wlan0 eth0 MyAccessPoint MyPassPhrase
```

Here is our configuration

``` 
CHANNEL=default
GATEWAY=192.168.12.1
WPA_VERSION=1+2
ETC_HOSTS=0
DHCP_DNS=gateway
NO_DNS=0
NO_DNSMASQ=0
HIDDEN=0
MAC_FILTER=0
MAC_FILTER_ACCEPT=/etc/hostapd/hostapd.accept
ISOLATE_CLIENTS=0
SHARE_METHOD=none
IEEE80211N=1
IEEE80211AC=0
HT_CAPAB=[HT40+]
VHT_CAPAB=
DRIVER=nl80211
NO_VIRT=0
COUNTRY=
FREQ_BAND=2.4
NEW_MACADDR=
DAEMONIZE=0
NO_HAVEGED=0
WIFI_IFACE=wlan0
INTERNET_IFACE=
SSID=Navio
PASSPHRASE=ChangeMe
USE_PSK=0
```

To generate this .conf file at /etc

``` 
create_ap -n --ieee80211n --ht_capab '[HT40+]' wlan0 Navio ChangeMe --mkconfig /etc/create_ap.conf
```

To run this configuration with:

``` 
create_ap --config /etc/create_ap.conf
```

Start service immediately:

``` 
systemctl start create_ap
```

Start on boot:

``` 
systemctl enable create_ap
```

##### Increase the transmission power 

It is a way to make your UAV more stable. But please check your country law is allow high power transmission.

``` 
https://forum.backbox.org/howtos/alfa-awus036nha-2w-(33-dbm)-configuration/
```

#### ArduPilot Configuration

We run ArduPilot on Raspberry Pi with Navio. The autopilot's code works directly on Raspberry Pi.

You can follow the instructions with the Navio2 docs(https://docs.emlid.com/navio2/common/ardupilot/installation-and-running/)

#### Onboard calibration

Here we use Mission Planner to calibrate the onboard sensors.

Follow the instruction to calibrate the onboard sensors
(https://docs.emlid.com/navio2/ardupilot/tips/)

### Sensors

In this project, we choose two sensors that install on the UAV and transmit the climate date to laptop

#### DHT22 temperature-humidity sensor

The DHT22 is a basic, low-cost digital temperature and humidity sensor. It uses a capacitive humidity sensor and a thermistor to measure the surrounding air, and spits out a digital signal on the data pin

![image](https://5.imimg.com/data5/DV/AL/GJ/SELLER-6366772/dht22-digital-temperature-and-humidity-sensor-module-500x500.jpg)

* We use the GPIO17_DF13 as the data pin
* Pin 2 for 5V
* Pin 6 for ground

![image](https://docs.emlid.com/navio2/dev/img/pinout.png)

#### SDS011 Air Quality Sensor

The SDS 011 Sensor is a quite recent Air Quality Sensor developed by Nova Fitness, a spin-off from the university of Jinan (in Shandong). 
It is connected through a USB-Serial-Converter.

![image](https://aqicn.org/air/images/sensors/sds011-large.png)

#### Copy Python file to Raspberry Pi

You can find two Python files in /Sensor folder at this GitHub repository, named mqtt-dht22.py and mqtt-sds011.py

##### Making mqtt-dht22.py startup at boot

Create unit file using command as shown below:

``` 
sudo nano /lib/systemd/system/dht22.service
```

Add in the following text:

``` 
[Unit]
 Description=DHT22 MQTT Publish
 After=multi-user.target

 [Service]
 Type=idle
 ExecStart=/usr/bin/python3 /home/pi/mqtt-dht22.py

 [Install]
 WantedBy=multi-user.target
```

The permission on the unit file needs to be set to 644 :

``` 
sudo chmod 644 /lib/systemd/system/dht22.service
```

Now the unit file has been defined we can tell systemd to start it during the boot sequence :

``` 
sudo systemctl daemon-reload
sudo systemctl enable dht22.service
```

Reboot the Pi and your custom service should run:

``` 
sudo reboot
```

##### Making mqtt-sds011.py startup at boot

Repeat the upon steps, remember to replace 'dht22' to sds011.

### Video Streaming

Run an update

``` 
apt-get update
```

Install gstreamer

``` 
apt-get install gstreamer1.0
```

Start the streaming

``` 
raspivid -t 999999 -w 1080 -h 720 -fps 25 -hf -b 2000000 -o - | \gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 \! gdppay ! tcpserversink host=192.168.12.1 port=5000
```

You can find the code in /Video\ Streaming

#### Make the Streaming startup at boot

Create unit file using command as shown below:

``` 
sudo nano /lib/systemd/system/streaming.service
```

Add in the following text:

``` 
[Unit]
 Description=Video Streaming Service
 After=multi-user.target

 [Service]
 Type=idle
 ExecStart=/usr/bin /home/pi/video-streaming.sh 

 [Install]
 WantedBy=multi-user.target
```

The permission on the unit file needs to be set to 644 :

``` 
sudo chmod 644 /lib/systemd/system/streaming.service
```

Now the unit file has been defined we can tell systemd to start it during the boot sequence :

``` 
sudo systemctl daemon-reload
sudo systemctl enable streaming.service
```

Reboot the Pi and your custom service should run:

``` 
sudo reboot
```

#### The Streaming delay

![image](https://github.com/Ethan7102/FYP/raw/master/Streaming%20delay.png)

### Laptop Side Configuration

#### Install Packages
“Requirements files” are files containing a list of items to be installed using pip install like so:

``` 
pip3 install -r requirements.txt
```

You can find the [requirements.txt](https://github.com/Ethan7102/FYP/raw/master/requirments.txt) in the root directory.

## How to run the system

1\. Boot the Raspberry Pi

2\. Connect the Wi-Fi from your raspberry Pi AP

3\. run monitor.py on your laptop

``` 
python3 monitor.py
```

4\. Press Connection in the navigation bar from the monitor APP

## How to save date

1\. Press the Mission button on the Navigation bar

2\. Press the Save As button to select the path that you want to save

## How to disconnect the UAV

1\. Press the Connection button on the Navigation bar

2\. Press the Disconnect button to disconnect the UAV

## How to clear the old mission

1\. Press the Mission button on the Navigation bar

2\. Press the New Mission button to start a new missions

``` 
It will clear all the data from previous mission, please save before you start a new mission.
```

![image](https://github.com/Ethan7102/FYP/raw/master/Screen%20Shot/rec/readme1.png)

## How to quit the application

1\. Press the Mission button on the Navigation bar

2\. Press the quit button 

## Built With

* [DroneKit Python](https://github.com/dronekit/dronekit-python) - The drone API used
* [QGroundControl](http://qgroundcontrol.com) - The ground control station used on smartphone
* [create_ap](https://github.com/oblique/create_ap) - The Access Point API used
* [GStreamer](https://gstreamer.freedesktop.org) - The media-handling component used
* [PyQt](https://riverbankcomputing.com/software/pyqt/intro) - The GUI framework used 
* [GTK](https://www.gtk.org) - The GUI framework used 
* [Eclipse Paho](https://www.eclipse.org/paho/) - The MQTT API used
* [PyGObject](https://pygobject.readthedocs.io/en/latest/index.html) - It provides bindings for GObject based libraries such as GTK, GStreamer.
* [pyqtlet](https://github.com/skylarkdrones/pyqtlet) - The map wrapper used
* [Matplotlib](https://matplotlib.org) - The library for creating graphics and charts used
* [QFlightInstruments](https://github.com/JdeRobot/ThirdParty/tree/master/qflightinstruments) - The flight instrument used

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Ethan7102/FYP/raw/master/LICENSE) file for details

## Acknowledgments

* 
* 
