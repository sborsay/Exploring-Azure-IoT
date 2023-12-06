get connection string
```
az iot hub device-identity connection-string show -d testdevice --hub-name iothubsdb1
```

monitor device to cloud traansmissions
```
az iot hub monitor-events --hub-name iothubsdb1 -d testdevice
```

Original:

https://github.com/VSChina/ESP32_AzureIoT_Arduino

But use this:

https://github.com/insighio/ESP32_AzureIoT_Arduino

This fixes the error with: <p>
socket_async.c <p>
lines 131-153 - "Socket connect failed"

```
connect_ret = connect(sock, (const struct sockaddr*)&sock_addr, sizeof(sock_addr));  
				result = sock;
				/*
                if (connect_ret == -1)
                {
                    int sockErr = get_socket_errno(sock);
                    if (sockErr != EINPROGRESS)
                    {
                      
                        LogError("Socket connect failed, not EINPROGRESS: %d", sockErr);
                        result = SOCKET_ASYNC_INVALID_SOCKET;
                    }
                    else
                    {
                        // This is the normally expected code path for our non-blocking socket
                        
                        result = sock;
                    }
                }
                else
                {
                   
                    // This result would be a surprise because a non-blocking socket
                    // returns EINPROGRESS. But it could happen if this thread got
                    // blocked for a while by the system while the handshake proceeded,
                    // or for a UDP socket.
                    result = sock;
                }
				*/
```
---
Download the entire zip file here:

https://github.com/insighio/ESP32_AzureIoT_Arduino

Then in Arduino IDE:
Go to -->Sketch-->Include Library-->Add .zip Library

Next in the Arduino IDE:
Go to -->File-->Examples-->ESP32 Azure IoT Arduino-->GetStarted


<p>
  
![image](https://user-images.githubusercontent.com/16296900/189241148-c9e5027e-9e24-4ddc-92e8-95f98e6af196.png)
