### Use the Azure CLI in Cloud Shell to monitor all devices on the IoT hub.  (also works in Windows PowerShell and the Command after the Azure CLI is installed):
```
az iot hub monitor-events --hub-name <youriothubname> --device-id <YOUR-DEVICE-NAMA>
```

## Publish a test message device-to-cloud in the Azure Cloud-Shell

```
az iot device send-d2c-message -n <YOUR-IOT-HUB-NAME> -d <YOUR-IoT-DEVICE-NAME> --data '{"temperature":33,"humidity":22, "timestamp": 123456}'
```

#Simulate a device from powershell or MS Code
```
az iot device simulate --device-id testdevice --login "HostName=iothubsdb1.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=CymzMGwDlpdhAtZokKkEz5X8OAKzdPlhM9EuVLEyfME="
```

#Simulate using a template
```
az iot device send-d2c-message -n iothubsdb1 -d testdevice --model-id 'dtmi:com:example:temperaturecontroller;1'
```
