#!/bin/bash

# Install Python3
sudo apt update
sudo apt install -y python3 python3-pip

# Install Paho MQTT Client
pip3 install paho-mqtt

# Clone Paho MQTT Python Client
git clone --depth 1 -b v1.6.1 https://github.com/eclipse/paho.mqtt.python 
cd paho.mqtt.python 
python3 setup.py install
