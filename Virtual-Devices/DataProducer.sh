#  Modified for Azure CLI by Stephen Borsay
#  Original code found at: https://aws.amazon.com/blogs/iot/integrating-iot-data-with-your-data-lake-with-new-aws-iot-analytics-features/

#!/bin/bash

iterations=5
wait=5

for (( i = 1; i <= $iterations; i++)) {

  CURRENT_TS=`date +%s`
  TEMP=$(( 15 + $RANDOM % 20 ))
  HUMIDITY=$(( 50 + $RANDOM % 40 ))

  # 3% chance of throwing an anomalous temperature reading
  if [ $(($RANDOM % 100)) -gt 97 ]
  then
    echo "Temperature out of range"
    TEMP=$(($TEMP*6))
  fi

  echo "Publishing message to Azure IoT Hub via the Azure CLI:"
  echo "temperature: $TEMP"
  echo "humidity: $HUMIDITY"
  echo "timestamp: $CURRENT_TS"

 az iot device send-d2c-message -n iothubsdb1 -d testdevice --data "{"temperature":$TEMP,"humidity":$HUMIDITY, "timestamp":$CURRENT_TS}" 

  sleep $wait
}
