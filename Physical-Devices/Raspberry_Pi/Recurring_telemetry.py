#samples/async-hub-scenarios/recurring_telemetry.py
# Modified by Stephen Borsay for Azure IoT course on Udemy

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import os
import asyncio
import time
import random
import uuid
import json
from azure.iot.device.aio import IoTHubDeviceClient
from azure.iot.device import Message


async def send_recurring_telemetry(device_client):
    # Connect the client.
    await device_client.connect()

    # Send recurring telemetry
    i = 0
    while True:
        i += 1
        temp =  random.randint(0, 130)
        humid = random.randint(0, 100)
        ts = int(time.time()) #round to nearest second by using 'int'
        payload = {
            "temperature": temp,
            "humidity": humid,
            "timestamp": ts
        }
        msg = Message(str(payload))
        msg.content_encoding = "utf-8"
        msg.content_type = "application/json"
        print("sending message #" + str(i))
        print(json.dumps(payload))
        await device_client.send_message(msg)
        time.sleep(5)


def main():
    # The connection string for a device should never be stored in code. For the sake of simplicity we're using an environment variable here.
    conn_str = "<Your-Devices-Primary-Connection-String-Here>"
    # The client object is used to interact with your Azure IoT hub.
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    print("IoTHub Device Client Recurring Telemetry Sample")
    print("Press Ctrl+C to exit")
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(send_recurring_telemetry(device_client))
    except KeyboardInterrupt:
        print("User initiated exit")
    except Exception:
        print("Unexpected exception!")
        raise
    finally:
        loop.run_until_complete(device_client.shutdown())
        loop.close()


if __name__ == "__main__":
    main()
