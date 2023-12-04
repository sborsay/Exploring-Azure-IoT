### MQTT Explorer Download

https://mqtt-explorer.com/

### MQTT Explorer "Username" String
```
<Your-IoT-Hub-Name>.azure-devices.net/<Your-Device-ID/Name>/?api-version=2021-04-12
```

### Azure CLI Command to get COnnection String
```
az iot hub generate-sas-token -n <Your-IoT-Hub-Name> -d <Your-Device-ID> --du <Your-Validity-Duration-In-Seconds>
```

### recognized external device topic

devices/<Your-Device-ID>/messages/events/

### Our device payload example

{"temperature":73,"humidity":88, "timestamp":123456789}
