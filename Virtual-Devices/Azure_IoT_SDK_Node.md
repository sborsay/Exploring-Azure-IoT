### Azure IoT SDK  Node link:

https://github.com/Azure/azure-iot-sdk-node

Or use

```
git clone https://github.com/azure/azure-iot-sdk-node
```

### Get your Connection String From the Azure CLI command to embed in the Node.js program
```
az iot hub device-identity connection-string show -d <Your-IoT-Device-ID> --hub-name <Your-IoT-Hub-Name>
```

### From the terminal command line use:

```
npm install azure-iot-device azure-iot-device-mqtt --save
```

Or, with some other samples from the SDK you will need to use use

```
npm install azure-iot-device azure-iot-device-amqp --save
```

### To monitor hub device

```
az iot hub monitor-events --hub-name <Your-IoT-Hub-Name> -d <Your-Device-ID>
```



