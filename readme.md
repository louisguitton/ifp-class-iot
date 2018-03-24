# Step 1: install raspbian OS on the RPi
```
tar -zxvf ...
```
# Step 2: operate a raspberry pi
locate IP adress of router
```
ifconfig
```
find the IP adress of the RPi by scanning the IP of the router
```
nmap -F 192.168.178.1-254
```
ssh to the RPi
```
ssh pi@192.168.178.138
```
Shutdown safely
```
shutdown -h now
# then pull out the power cable
```
Restart
```
shutdown -r now
```

# Step 3: initial server setup
Once raspbian is setup we do the digital ocean initial server setup
https://www.digitalocean.com/community/tutorials/initial-server-setup-with-debian-8


# Step 4: Build the circuit with Python and GPIO
Follow https://thingsboard.io/docs/samples/raspberry/temperature/

```
python3 -m venv ~/venv
source ~/venv/bin/activate
sh install_librairies.sh
```
if there is a problem at this stage `sudo chown -R pi ~/venv/lib/python3.5/site-packages/`

Modify if needed `electronics.py` with the help of https://pinout.xyz/
```
python electronics.py
```

# Step 5: Publish the data using MQTT
Understanding the concept of MQTT:
* first tab `python mqtt_subscriber.py`
* second tab `python mqtt_publisher.py`

Getting a dashboard:
`python publish_to_thingsboard`
