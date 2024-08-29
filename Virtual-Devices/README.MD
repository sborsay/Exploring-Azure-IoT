## Monitor incoming IoT data from a device
```
az iot hub monitor-events --hub-name <YOUR-IOT-HUB-NAME> --device-id <YOUR-IOT-DEVICE-NAME>
```

## Publish to a topic with the following format in your device code
```
devices/{device name}/messages/events/
```
## Publish a test nesage device-to-cloud

```
az iot device send-d2c-message -n iothubsdb1 -d testdevice --data '{\"fhfh\":33,\"jffj\":22}'
```

#Simulate a  device from powershell or MS Code
```
az iot device simulate --device-id testdevice --login "HostName=iothubsdb1.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=CymzMGwDlpdhAtZokKkEz5X8OAKzdPlhM9EuVLEyfME="
```

#Simulate using a template
```
az iot device send-d2c-message -n iothubsdb1 -d testdevice --model-id 'dtmi:com:example:temperaturecontroller;1'
```

## To Monitor Device to Cloud Telemetry Azure IoT Hub
---

### Method #1:  Use the Azure CLI in Windows PowerShell to monitor all devices on the IoT hub:
```
az iot hub monitor-events --hub-name <youriothubname>
```
Or for only a specific device on that hub

```
az iot hub monitor-events --hub-name --device-id
```
or

```
az iot hub monitor-events --output table --device-id mydevice --hub-name {YourIoTHubName}
```
------

###Generate SAS Token from CLI

```
az iot hub generate-sas-token -n [IoTHub Name] --policy registryRead --key-type secondary
```

```
az iot hub generate-sas-token --connection-string "HostName=iot-Hub.azure-devices.net;DeviceId=deviceId;SharedAccessKey=foo"
```


![image](https://user-images.githubusercontent.com/16296900/189200449-1da089be-560f-4e85-9616-d0a98e137f34.png)

Documentation: https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli </br>
https://docs.microsoft.com/en-us/cli/azure/azure-cli-reference-for-iot

---

### Method #2:  Use Azure IoT Tools for Visual Studio Code:

From the terminal tab in VS Code issue the same command as Method #1:

![image](https://user-images.githubusercontent.com/16296900/189199059-1cc2ff93-72a6-499a-81dd-a87fbfa4c90f.png)

Documentation: https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-vscode-iot-toolkit-cloud-device-messaging

---

### Method #3:  Use Azure IoT Explorer GUI tool:

While in IoT Tool go to:
```
Home--> IoT Hubs --> View Devices in this hub --> Device ID --> Telemetry --> Start
```
![image](https://user-images.githubusercontent.com/16296900/189202274-329b6e28-0c70-42f4-92e4-e51f9f8c3f02.png)

Documentation:  https://github.com/Azure/azure-iot-explorer/releases
</br>  https://docs.microsoft.com/en-us/azure/iot-fundamentals/howto-use-iot-explorer

```

//https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-direct-methods

az iot hub generate-sas-token -n <iothubName> --du <duration>

curl -X POST \
  https://<iothubName>.azure-devices.net/twins/<deviceId>/methods?api-version=2021-04-12\
  -H 'Authorization: SharedAccessSignature sr=iothubname.azure-devices.net&sig=x&se=x&skn=iothubowner' \
  -H 'Content-Type: application/json' \
  -d '{
    "methodName": "reboot",
    "responseTimeoutInSeconds": 200,
    "payload": {
        "input1": "someInput",
        "input2": "anotherInput"
    }
}'

```


