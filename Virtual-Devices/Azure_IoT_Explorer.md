###  Install Azure IoT Explorer

https://github.com/Azure/azure-iot-explorer/releases


### Command to get conection string from azure cli
```
az iot hub device-identity connection-string show --hub-name <Your-IoT-Hub> -d <Your-Device>
```


### Advance scenario custom Azure CLI Command

az iot device simulate --device-id <Your-Device>--login "HostName=<Your-IoT-Hub>.azure-devices.net;SharedAccessKeyName=<Shared-Access-Policy-Name>;SharedAccessKey=<Your-Key>" --data '{"temerature":33,"humidity":88, "timestamp": 12345}'

#### Or double quotes

az iot device simulate --device-id <Your-Device>--login "HostName=<Your-IoT-Hub>.azure-devices.net;SharedAccessKeyName=<Shared-Access-Policy-Name>;SharedAccessKey=<Your-Key>" --data "{"temerature":33,"humidity":88, "timestamp": 12345}"

