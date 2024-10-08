### Paid Full Featured tool

https://softblade.de/en/mqtt-fx/

### Free version of MQTTfx 1.71 used in lecture 

https://web.archive.org/web/20210514230412/https://www.jensd.de/apps/mqttfx/1.7.1

Alternate Location:

https://github.com/SeppPenner/mqttfx171-backup

---

### Article link -  "How to send MQTT messages to an Azure IoT Hub by MQTT.fx client"

https://weblogs.asp.net/morteza/how-to-send-mqtt-messages-to-an-azure-iothub-by-mqttfx-client

---

### MQTTfx Configuration

Broker address on MQTTfx is host name on Azure IoT hub:
```
<Your-IoT-Hub-Name> azure-devices.net
```

Broker Port :
```
8883
```

Client ID on MQTTfx is your Device ID (Device name) on Azure

Username on MQTT is:
```

<Your-IoT-Hub-Name>/<Your-Device-ID>/?api-version=2022-04-30
```

Password is an SAS token, to generate it via the CLI use:
```

az iot hub generate-sas-token -n <Your-IoT-Hub-Name> -d <Your-Device-ID> --du <Your-Validity-Duration-In-Seconds>
```


Use this portion of YOUR OWN SAS token as your Password (Do not include parenethesis):
```

SharedAccessSignature sr=<YOUR-HUB-NAME>.azure-devices.net%2Fdevices%2F<YOUR-DEVICE-NAME>&sig=6yUB5Eh5g3d5g3dU0LrzyjN2K5%2BYqL3QZ%2BNWXNU%3D&se=1724135529
```





