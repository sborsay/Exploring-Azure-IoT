
Link to Wokwi website with ESP32 selected:

https://wokwi.com/projects/new/micropython-esp32


Get your devices connection string with the Azure CLI and insert in the MicroPython program.

```	
az iot hub device-identity connection-string show --hub-name <Your-IoT-Hub> -d <Your-Device>
```

Get SAS token from the Azure CLI and insert in the MicroPython program.

```
az iot hub generate-sas-token -n <Your-IoT-Hub-Name> -d <Your-Device-ID> --du <Your-Validity-Duration-In-Seconds>
```

The monitor terminal command from Azure CLI.

```
az iot hub monitor-events --hub-name <Your-IoT-Hub-Name>  --device-id <Your-IoT-Device-Name>
```
