### Download the Azure-SDK-for-C-Arduino here:

https://github.com/Azure/azure-sdk-for-c-arduino

### Go To:

https://github.com/Azure/azure-sdk-for-c-arduino/tree/main/examples/Azure_IoT_Hub_ESP32

https://github.com/Azure/azure-sdk-for-c/tree/1ff8f33203d0635345a8e9b6717845b5924ccb39/sdk/samples/iot/aziot_esp32

### Get connection string
```
jjh
```

```
az iot hub monitor-events --hub-name iothubsdb1 -d testdevice
```

#define IOT_CONFIG_DEVICE_KEY = "Device Key = primary key"

### iot_configs.h defines into variables used by the sample
```
static const char* ssid = "<Your-WiFI-Network-Name>";
static const char* password = "<Your-WiFi-Password>";

static const char* host = "<Your-IoT-Hub-Name>.azure-devices.net";  
static const char* mqtt_broker_uri = "mqtts://<Your-IoT-Hub-Name>.azure-devices.net";
static const char* device_id = "<Your Device-ID AKA Device-Name>"; 
static const int mqtt_port = 8883;
```


Then in Arduino IDE:
Go to -->Sketch-->Include Library-->Add .zip Library

Next in the Arduino IDE:
Go to -->File-->Examples-->Azure SDK for C-->Azure IoT Hub ESP32
<p>
  
![image](https://user-images.githubusercontent.com/16296900/189236341-255bfd98-4f37-40d4-bd54-2d0a0c2262a5.png)

This will load 5 visible files in the tabs in the Arduino IDE, the only two you need to alter are:<p>
</br>
_Azure_IoT_Hub_32.ino (the Main program)_
</br>
_iot_configs.h (this contains your WiFi info and credentials)_
<p>
  
![image](https://user-images.githubusercontent.com/16296900/189236752-529aa258-04a2-430f-b6b0-bf7588e45db9.png)

links to alter payload from msgCount:

https://github.com/maxgerhardt/pio-azure-iot-arduino/blob/main/src/Azure_IoT_Hub_ESP32.cpp
<p>

