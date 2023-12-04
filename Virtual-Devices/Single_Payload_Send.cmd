###Monitor
---------
```
az iot hub monitor-events --hub-name <Your-IoT-Hub-Name>  --device-id <Your-IoT-Device-Name>
```


###OPTIONAL Formats (JSON is default)
----------------------------------------
```
az iot hub monitor-events --hub-name <Your IoT Hub Name> --output json
```

```
az iot hub monitor-events --hub-name iothubsdb1 --output table
```
-----------------------------------------


###Send IoT Payload from a terminal (you can use escaped or unescaped payload variables)
------------------------------------------------------------------------------------
```
az iot device send-d2c-message -n iothubsdb1 --device-id testdevice --data '{"temperature":73,"humidity":88, "timestamp":123456789}'
```

