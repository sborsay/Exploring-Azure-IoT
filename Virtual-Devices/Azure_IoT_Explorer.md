### Command to get your conection string from the Azure cli
```
az iot hub device-identity connection-string show --hub-name <Your-IoT-Hub> -d <Your-Device>
```


### Advance scenario custom Azure CLI Command Example
```
az iot device simulate --device-id <Your-Device>--login "HostName=<Your-IoT-Hub>.azure-devices.net;SharedAccessKeyName=<Shared-Access-Policy-Name>;SharedAccessKey=<Your-Key>" --data '{"temperature":33,"humidity":88, "timestamp": 12345}'
```

#### Or using double quotes if needed 
```
az iot device simulate --device-id <Your-Device>--login "HostName=<Your-IoT-Hub>.azure-devices.net;SharedAccessKeyName=<Shared-Access-Policy-Name>;SharedAccessKey=<Your-Key>" --data "{"temperature":33,"humidity":88, "timestamp": 12345}"
```

