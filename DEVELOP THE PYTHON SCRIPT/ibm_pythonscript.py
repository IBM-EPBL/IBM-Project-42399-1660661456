import ibmiotf.application
import ibmiotf.device
import time
import random
import sys

#ibm watson device credentials

organization="gdkgkx"
deviceType="kprp"
deviceid="2222"
authMethod="token"
authToken="na)UXp4FWOjf1iJhOn"

#generate random values for pH and turbity


def myCommandCallback(cmd):
    print ("command received: %s" % cmd.data)
    if(cmd.data['command']=="MOTOR_ON"):
        print('motoron')
    elif(cmd.data['command']=="MOTOR_OFF"):
        print('motoroff')
try:
        deviceOptions={"org": organization,"type": deviceType,"id": deviceid,"auth-method":authMethod, "auth-token":authToken}
        deviceCli = ibmiotf.device.Client(deviceOptions)

except Exception as e:
        print ("caught exception connecting device %s" %str(e))
        sys.exit()


#connect and sending data

deviceCli.connect()

while True:
    pH=random.randint(0,14)
    turb=random.randint(0,250)
    temp=random.randint(0,40)
    
    data={'pH':pH,'Turbidity':turb,'Temperature':temp}
    print(data)
    def myOnPublishCallBack():
        print("pH Value of Water %s " %pH)
        print("Turbidity Value of Water %s " %turb)
        print("Temperature Value of Water %s " %temp)
    success=deviceCli.publishEvent("IoTSensor","json",data,qos=0,on_publish=myOnPublishCallBack)
    if not success:
        print ("Not connected to IoTF")
    time.sleep(2)

    deviceCli.commandCallback=myCommandCallback


#disconnect the device from the cloud

deviceCli.connect()
