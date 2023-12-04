#Modified from:  https://github.com/Prabhashi-97/Azure-IoT-with-Raspberry-Pi/blob/main/raspberryprogram.py

import random  
#import Adafruit_DHT
import time
from azure.iot.device import IoTHubDeviceClient, Message  
#sensor = Adafruit_DHT.DHT11
#pin = 4
CONNECTION_STRING = "HostName=iothubsdb1.azure-devices.net;DeviceId=testdevice;SharedAccessKey=Sg2kG5as7ZRU1u4lHRqL1/dX1ntLKdP8JPxirWwOzr4="  
MSG_SND = '{{"temperature": {temperature},"humidity": {humidity}}}'  
while True:
    
    def iothub_client_init():  
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)  
        return client  
    def iothub_client_telemetry_sample_run():  
        try:  
            client = iothub_client_init()  
            print ( "Sending data to IoT Hub, press Ctrl-C to exit" )  
            while True:  
                temp =  random.randint(0, 130)
                humid = random.randint(0, 100)
                msg_txt_formatted = MSG_SND.format(temperature=temp, humidity=humid)  
                message = Message(msg_txt_formatted)  
                print( "Sending message: {}".format(message) )  
                client.send_message(message)  
                print ( "Message successfully sent" )  
                time.sleep(3)  
        except KeyboardInterrupt:  
            print ( "IoTHubClient stopped" )  
    if __name__ == '__main__':  
        print ( "Press Ctrl-C to exit" )  
        iothub_client_telemetry_sample_run()
