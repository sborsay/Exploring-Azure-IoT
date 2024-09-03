# MicroPython HTTPS example for Wokwi.com
# You will need to modifiy 2 fields
# A) dict_keys = parse_connection with your 'connection string'
# B) sas_token_str = with your 'sas token string'

import network
import urequests
import time
import random

# Connect to WiFi
print("Connecting to WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
# Enter Your WiFI credentials below - WiFI Network name, Password
sta_if.connect('<YOUR-WIFI-NETWORk-NAME>', '<YOUR-WIFI-NETWORK-PASSWORD>')
while not sta_if.isconnected():
  print(".", end="")
  time.sleep(0.25)
print("Connected!")

import utime

from umqtt.robust import MQTTClient

def create_mqtt_client(client_id, hostname, username, password, port=8883, keepalive=120, ssl=True):
    if not keepalive:
        keepalive = 120
    if not ssl:
        ssl = True
    c = MQTTClient(client_id=client_id, server=hostname, port=8883, user=username, password=password, keepalive=120, ssl=True)
    c.DEBUG = True
    return c

def get_telemetry_topic(device_id):
    return get_topic_base(device_id) + "/messages/events/"   # Standard outgoing Message Topic - publsihed from device
    
def get_c2d_topic(device_id):
     return get_topic_base(device_id) + "/messages/devicebound/#"  #Standard incoming Message Topic - subscribed to on device

def get_topic_base(device_id, module_id=None):
    if module_id:
        base_str = "devices/" + device_id + "/modules/" + module_id
    else:
        base_str = "devices/" + device_id
    return base_str

DELIMITER = ";"
VALUE_SEPARATOR = "="

def parse_connection(connection_string):
    cs_args = connection_string.split(DELIMITER)
    dictionary = dict(arg.split(VALUE_SEPARATOR, 1) for arg in cs_args)
    return dictionary

HOST_NAME = "HostName"
SHARED_ACCESS_KEY_NAME = "SharedAccessKeyName"
SHARED_ACCESS_KEY = "SharedAccessKey"
SHARED_ACCESS_SIGNATURE = "SharedAccessSignature"
DEVICE_ID = "DeviceId"
MODULE_ID = "ModuleId"
GATEWAY_HOST_NAME = "GatewayHostName"

## Parse the connection string into constituent parts
## az iot hub device-identity connection-string show --hub-name <YOUR-IOT-HUB-NAME> --device-id <YOUR-IOT-DEVICE-NAME>
dict_keys = parse_connection("<Insert-Your-Primary-Connection-String-Here>")
## Example: "HostName=iothubsdb1.azure-devices.net;DeviceId=testdevice;SharedAccessKey=Sg2kG5je88QU1u4KJHqL1/dX1ntKdg645irWwOzr4=")
shared_access_key = dict_keys.get(SHARED_ACCESS_KEY)
shared_access_key_name =  dict_keys.get(SHARED_ACCESS_KEY_NAME)
gateway_hostname = dict_keys.get(GATEWAY_HOST_NAME)
hostname = dict_keys.get(HOST_NAME)
device_id = dict_keys.get(DEVICE_ID)
module_id = dict_keys.get(MODULE_ID)

## Create you own shared access signature from the connection string that you have
## Azure IoT Explorer can be used for this purpose.
## az iot hub generate-sas-token -n <YOUR-IOT-HUB-NAME> -d <YOUR-IOT-DEVICE-NAME> --du 999999
sas_token_str = "<Insert-Your-SAS-Token-String-Here>"
## Example: "SharedAccessSignature sr=iothubsdb1.azure-devices.net%2Fdevices%2Ftestdevice&sig=JFagdnaILBX72HQewsXX0OfS80K7fiC5gwO0%2BMYo%3D&se=1725619961"

## Create username following the below format '<HOSTNAME>/<DEVICE_ID>'
username = hostname + '/' + device_id

## Create UMQTT ROBUST or UMQTT SIMPLE CLIENT
mqtt_client = create_mqtt_client(client_id=device_id, hostname=hostname, username=username, password=sas_token_str, port=8883, keepalive=120, ssl=True)

print("connecting")
mqtt_client.reconnect()

def callback_handler(topic, message_receive):
    print("Received message")
    print(message_receive)

subscribe_topic = get_c2d_topic(device_id)
mqtt_client.set_callback(callback_handler)
mqtt_client.subscribe(topic=subscribe_topic)

topic = get_telemetry_topic(device_id)

#---------------------------------------
## A better send telemetry with a useful payload and non-blocking loop
while True: #loop forever
            pending_message = mqtt_client.check_msg()  # check for new subscription payload incoming
            if pending_message != 'None':  #check if we have a message 
                temp =  random.randint(0, 130)
                humid = random.randint(0, 100)
                deviceTime = time.time()
                print("Publishing")
                message="{\"temperature\": %d,\"humidity\": %d,\"timestamp\": %d}"%(temp,humid,deviceTime)
                mqtt_client.publish(topic=topic, msg=message)
                print("published payload")
                time.sleep(5)  #A 5 second delay between publishing, adjust as you like
            
## Send a C2D message and wait for it to arrive at the device
print("waiting for message")
mqtt_client.wait_msg()
