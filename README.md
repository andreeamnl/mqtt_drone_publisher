# MQTT Drone Publisher

This repository contains code for controlling a drone using MQTT messages.

## Contents

- [send.py](send.py): Python script responsible for publishing MQTT messages to control the drone.
- [install_dronekit.sh](install_dronekit.sh): Shell script to install Python and pip dependencies for DroneKit.
- [mqtt_setup.sh](mqtt_setup.sh): Shell script to install Python3, Paho MQTT Client, and clone Paho MQTT Python Client.
- [test.py](test.py): Python script for testing MQTT communication.

## Usage

1. **send.py**: This script connects to the Pixhawk, collects drone data, and publishes it as MQTT messages. You need to replace placeholders for HOST, MQTT_USER, and MQTT_PASS with your MQTT broker details.

2. **install_dronekit.sh**: Run this script to install Python and pip dependencies required for DroneKit.

    ```bash
    chmod +x install_dronekit.sh
    ./install_dronekit.sh
    ```

3. **mqtt_setup.sh**: Run this script to install Python3, Paho MQTT Client, and clone Paho MQTT Python Client.

    ```bash
    chmod +x mqtt_setup.sh
    ./mqtt_setup.sh
    ```

4. **test.py**: This script connects to the MQTT broker and publishes test data. Make sure to replace placeholders for HOST, MQTT_USER, and MQTT_PASS with your MQTT broker details.

## License

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for more details.

© Copyright 2021 HiveMQ GmbH
