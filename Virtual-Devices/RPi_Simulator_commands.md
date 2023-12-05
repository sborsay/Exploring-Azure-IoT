### Microsoft Raspberry Pi emmulator link:

https://azure-samples.github.io/raspberry-pi-web-simulator/


### Retrieve your connection string from the Azure CLI
```
az iot hub device-identity connection-string show --hub-name <Your-IoT-Hub> -d <Your-Device>
```

### Terminal monitor command
```
az iot hub monitor-events --hub-name <Your-IoT-Hub-Name>  --device-id <Your-IoT-Device-Name>
```

