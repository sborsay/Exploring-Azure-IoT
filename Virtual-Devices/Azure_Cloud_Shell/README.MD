### Use the Azure CLI in Cloud Shell to monitor all devices on the IoT hub.
### (also works in Windows PowerShell and the Command after the Azure CLI is installed):
```
az iot hub monitor-events --hub-name <YOUR-IOT-HUB-NAME> --device-id <YOUR-IOT-DEVICE-NAME>
```

### Publish a test message device-to-cloud in the Azure Cloud Shell

```
az iot device send-d2c-message -n <YOUR-IOT-HUB-NAME> -d <YOUR-IOT-DEVICE-NAME> --data '{"temperature":33,"humidity":22, "timestamp": 123456}'
```

### Simulate a device
```
az iot device simulate --device-id <YOUR-IOT-DEVICE-NAME> --login "HostName=<YOUR-IOT-HUB-NAME>.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=CybgMGwDlpdhAtZrt56OAKzdPlhM67hLEyfME="
```

### Simulate using a template
```
az iot device send-d2c-message -n <YOUR-IOT-HUB-NAME> -d <YOUR-IOT-DEVICE-NAME> --model-id 'dtmi:com:example:temperaturecontroller;1'
```
