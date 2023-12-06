#include <WiFi.h>
#include "Esp32MQTTClient.h"

// Please input the SSID and password of WiFi
const char* ssid     = "<Your-WiFi-Network-Name>";
const char* password = "<Your-WiFi-Password>";

/*String containing Hostname, Device Id & Device Key in the format:                         */
/*  "HostName=<host_name>;DeviceId=<device_id>;SharedAccessKey=<device_key>"                */
/*  "HostName=<host_name>;DeviceId=<device_id>;SharedAccessSignature=<device_sas_token>"    */

/*   it will look like HostName=#########.azure-devices.net;DeviceId=#######;SharedAccessKey=################# */
static const char* connectionString = "<Paste-Your-Connection-String-Here>";

static bool hasIoTHub = false;

void setup() {
  Serial.begin(115200);
  Serial.println("Starting connecting WiFi.");
  delay(10);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  if (!Esp32MQTTClient_Init((const uint8_t*)connectionString))
  {
    hasIoTHub = false;
    Serial.println("Initializing IoT hub failed.");
    return;
  }
  hasIoTHub = true;
}

unsigned long lastPublish; //for millis

void loop() {
  Serial.println("start sending events.");
  if (hasIoTHub)
  {
    char buff[128];
    //fake number range, adjust as you like, floats are ony 4 bytes
    float temp =   random(0,120); 
    float humid =  random(50,100);//50 - 100% humidity
  
    sprintf(buff, "{\"uptime\":%lu,\"temperature\":%.0f,\"humidity\":%.0f}", millis() / 1000, temp, humid);

     if (millis() - lastPublish > 10000) {

    if (Esp32MQTTClient_SendEvent(buff)) //publish payload
    {
      Serial.println("Sending data succeed");
      Serial.println(buff);
    }
    else
    {
      Serial.println("Failure...");
    }

         lastPublish = millis(); 
  }
    delay(5000);
  }
}
