#!/bin/sh
source ~/venv/bin/activate
start_dir=$(pwd)
interpreter=$(which python)

mkdir -p /tmp/adafruit && cd /tmp/adafruit && \
wget https://github.com/adafruit/Adafruit_Python_DHT/archive/master.zip && \
unzip -o master.zip

cd Adafruit_Python_DHT-master && $interpreter setup.py install

cd $start_dir

pip install -r requirements.txt
