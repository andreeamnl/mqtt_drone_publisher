#
# Copyright 2021 HiveMQ GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#enable TLS client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)

import time
import paho.mqtt.client as paho
from dronekit import connect, VehicleMode
import json
from paho import mqtt

HOST = "9b7b323ee67e46d18f9317162c8e8841.s1.eu.hivemq.cloud"
PORT = 8883
MQTT_USER = "sergiu.doncila"
MQTT_PASS = "QWEasd!@#123"
TOPIC = "agrobot/pixhawk"

# Connect to the Pixhawk
vehicle = connect("/dev/ttyACM0", baud=57600, wait_ready=True)
# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

# using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
# userdata is user defined data of any type, updated by user_data_set()
# client_id is the given name of the client
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set(MQTT_USER, MQTT_PASS)
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect(HOST, PORT)

# setting callbacks, use separate functions like above for better visibility
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

# subscribe to all topics of encyclopedia by using the wildcard "#"
client.subscribe("agrobot/#", qos=1)

def publish_data():
    while True:
        data = {
            #"version": vehicle.version,
            "location_global_frame_lat": vehicle.location.global_frame.lat,
            "location_global_frame_long": vehicle.location.global_frame.lon,
            "location_global_frame_alt": vehicle.location.global_frame.alt,
            "attitude_pitch": vehicle.attitude.pitch,
            "attitude_yaw": vehicle.attitude.yaw,
            "attitude_roll": vehicle.attitude.roll,


            "velocity_vx": vehicle.velocity[0],
            "velocity_vy": vehicle.velocity[1],
            "velocity_vz": vehicle.velocity[2],

            "gps_eph": vehicle.gps_0.eph,
            "gps_epv": vehicle.gps_0.epv,
            "gps_fix_type": vehicle.gps_0.fix_type,
            "gps_satellites_visible": vehicle.gps_0.satellites_visible,

            "groundspeed": vehicle.groundspeed,
        }

        payload = json.dumps(data)
        client.publish(TOPIC, payload, qos=1)
        print("Data published:", payload)

        time.sleep(5)  # Publish data every 5 seconds

if __name__ == "__main__":
    try:
        publish_data()
    except KeyboardInterrupt:
        print("Interrupted, exiting...")
    finally:
        vehicle.close()
        client.disconnect()


# a single publish, this can also be done in loops, etc.
#client.publish("agrobot/data", payload="hot", qos=1)

# loop_forever for simplicity, here you need to stop the loop manually
# you can also use loop_start and loop_stop
#client.loop_forever()