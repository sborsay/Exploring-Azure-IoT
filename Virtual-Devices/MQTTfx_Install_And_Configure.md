paid mqttfx tool

free version one location

feeee version 2 location

article link  telling how to use mqttfx with azure

MQTTfx fonfiguration


Broker address on MQTTfx is host name on Azure IoT hub:

<Your-IoT-Hub-Name> azure-devices.net

Broker Port :

8883

Client ID on MQTTfx is your Device ID (Device name) on Azure

Username on MQTT is:

<Your-IoT-Hub-Name>/<Your-Device-ID>/?api-version=2022-04-30


Password is an SAS token, to generate it via the CLI use:

az iot hub generate-sas-token -n <Your-IoT-Hub-Name> -d <Your-Device-ID> --du <Your-Validity-Duration-In-Seconds>




