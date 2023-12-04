### Azure IoT SDK  Python link

https://github.com/Azure/azure-iot-sdk-python

Or use:

```
pip install azure-iot-device
```


### Connection String CLI command to install in Python Program

```
az iot hub device-identity connection-string show -d <Your-IoT-Device-ID> --hub-name <Your-IoT-Hub-Name>
```


### To monitor hub device

```
az iot hub monitor-events --hub-name <Your-IoT-Hub-Name> -d <Your-Device-ID>
```
