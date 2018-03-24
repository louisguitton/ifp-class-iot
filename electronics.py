import Adafruit_DHT


def sensor_get():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 14)
    print('Temp: {:.2f}C'.format(temperature))
    print('Hum: {:.2f}%'.format(humidity))
    return humidity, temperature


if __name__ == "__main__":
    sensor_get()
