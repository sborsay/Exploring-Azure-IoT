//MQTT.fx switch fountain, modified by Stephen Borsay
//add /$.ct=application%2Fjson&$.ce=utf-8 for decoded non base64
//devices/<DEVICE_ID>/messages/events/$.ct=application%2Fjson&$.ce=utf-8

var Thread = Java.type("java.lang.Thread");
 
var topic = "devices/<Your-Device-ID>/messages/events/$.ct=application%2Fjson&$.ce=utf-8";
var waitTime = 2000;
var iterations = 10;

function execute(action) {
    out("Test Script: " + action.getName());
    for (var i = 0; i < iterations; i++) {
        sendPayload();
        Thread.sleep(waitTime);
    }
    action.setExitCode(0);
    action.setResultText("done.");
    out("Test Script: Done");
    return action;
}

function sendPayload() {
	
	var temp = Math.round(Math.random()*130);
	var humid = Math.round(Math.random()*100);
	var ts = Date.now();
	
	var IoT_Payload = 
	
		{ 
		  "temperature" :  temp, 
		  "humidity"    :  humid,
		  "timestamps"  :  ts
		}

var payload = JSON.stringify(IoT_Payload)

	mqttManager.publish(topic, payload);
	out("Topic is:  \n" + topic);
	out("payload sent \n" + payload);
}

function out(message){
     output.print(message);
}
