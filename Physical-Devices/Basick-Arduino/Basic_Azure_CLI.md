### Get your connection string

az iot hub device-identity connection-string show -d <Your-Device-ID> --hub-name <Your-IoT-Hub-Name>

### Monitor your device to cloud traansmissions

az iot hub monitor-events --hub-name <Your-IoT-Hub-Name> -d <Your-Device-ID>
