#Modified from:  https://github.com/Prabhashi-97/Azure-IoT-with-Raspberry-Pi/blob/main/raspberryprogram.py

import random  
import time
from azure.iot.device import IoTHubDeviceClient, Message  
CONNECTION_STRING = "<Your-Devices-Primary-Connection-String-Here>"  
MSG_SND = '{{"temperature": {temperature},"humidity": {humidity}, "timestamp": {timestamp}}}'  
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
                ts = int(time.time()) #round to nearest second by using 'int'
                msg_txt_formatted = MSG_SND.format(temperature=temp, humidity=humid, timestamp=ts)  
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
