# Installation
1. install raspbian OS on the RPi
```
tar -zxvf ...
```
2. operate a raspberry pi
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

3. initial server setup
Once raspbian is setup we do the digital ocean initial server setup
https://www.digitalocean.com/community/tutorials/initial-server-setup-with-debian-8


/etc/dhcpcd.conf

eth0
static ip_address = 192.168.1.100 / 24
static routers = 192.168.1.1
static domain_name_servers = 192.168.1.1

wlan0 interface
static ip_address = 192.168.0.100 / 24
static routers = 192.168.1.1
static domain_name_servers = 192.168.1.1

sudo update-alternatives --config python3

4. Build the circuit with Python and GPIO
```
python3 -m venv ~/venv
source ~/venv/bin/activate
sh install_librairies.sh
```
if there is a problem at this stage `sudo chown -R pi ~/venv/lib/python3.5/site-packages/`

https://pinout.xyz/

5. Publish the data using MQTT
