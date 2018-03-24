import os
import time
import sys
import json

import Adafruit_DHT
import paho.mqtt.client as mqtt

MQTT_SERVER = 'localhost'
MQTT_PATH = 'test_channel'

client = mqtt.Client()

client.connect(MQTT_SERVER, 1883, 60)

humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 14)
humidity = round(humidity, 2)
temperature = round(temperature, 2)
print("Temperature: {}C, Humidity: {}%".format(temperature, humidity))
sensor_data['temperature'] = temperature
sensor_data['humidity'] = humidity

# Sending humidity and temperature data to ThingsBoard
client.publish(MQTT_PATH, json.dumps(sensor_data), 1)

client.disconnect()
