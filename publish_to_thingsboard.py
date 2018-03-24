import os
import time
import sys
import json

import Adafruit_DHT
import paho.mqtt.client as mqtt

THINGSBOARD_HOST = 'demo.thingsboard.io'
THINGSBOARD_PATH = 'v1/devices/me/telemetry'
ACCESS_TOKEN = 'cKkt7XsLAlpQJxMsBlte'

# Data capture and upload interval in seconds. Less interval will eventually hang the DHT22.
INTERVAL=2

sensor_data = {'temperature': 0, 'humidity': 0}

next_reading = time.time()

client = mqtt.Client()

# Set access token
client.username_pw_set(ACCESS_TOKEN)

# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(THINGSBOARD_HOST, 1883, 60)

client.loop_start()

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 14)
        humidity = round(humidity, 2)
        temperature = round(temperature, 2)
        print("Temperature: {}C, Humidity: {}%".format(temperature, humidity))
        sensor_data['temperature'] = temperature
        sensor_data['humidity'] = humidity

        # Sending humidity and temperature data to ThingsBoard
        client.publish(THINGSBOARD_PATH, json.dumps(sensor_data), 1)

        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()
