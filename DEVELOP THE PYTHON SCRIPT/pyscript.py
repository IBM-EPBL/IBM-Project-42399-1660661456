#IBM Watson IOT Platform
#pip install wiotp-sdk 
import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "9fds9f",
        "typeId": "kpr123",
        "deviceId":"1122"
    },
    "auth": {
        "token": "+_HOJ)L?Vl4OV8ZMm("
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    temp=random.randint(-20,125)
    turb=random.randint(0,250)
    phs=random.randint(0,14)
    
    myData={'temperature':temp, 'turbidity':turb,'PH value':phs}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
