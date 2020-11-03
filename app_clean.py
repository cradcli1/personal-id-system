from flask import Flask, json, request
from datetime import datetime, timedelta
import time
import requests, os
import dateutil.relativedelta

# global variables
import config

# functions in shared directory
from dashboard import *
from webhooks import *
from timeRetrieval import *
from deviceParse import *
# global list/dictionary
from config import currentDevices, previousDevices


# init a flash web app
app = Flask(__name__)

# validate web server from meraki
@app.route('/', methods=['GET'])
def getValidator():
    return "99dfc74e4abb542eeb07195a89161d5303da09ab"

#def get_curr_devices(client_name)

# receive location data
@app.route('/', methods=['POST'])
def getCmxJSON():
    cmxData = request.json
    # print full json
    # cmxdata = json.dumps(cmxdata, indent=2)

    # determine device type
    if cmxData['type'] == "BluetoothDevicesSeen":
        print("\nBluetooth Devices Seen:\n")
        btResponse = dashboardBT()
        parseSeenDevices(cmxData, btResponse)
        currentEpoch = time.time()
        currentTime = datetime.fromtimestamp(currentEpoch) # YYYY-MM-DD HH:MM:SS
        for clientName in currentDevices:
            nearbyCoworker = "{} is currently in your vicininty!\n".format(clientName)
            lastSeen = getLastSeen(clientName, currentTime, btResponse)
            message = nearbyCoworker + lastSeen
            sendMessage(message)
            # print("{}".format(message))
        for clientName in previousDevices.items():
            print("{} is no longer in the area but was last nearby at x EST".format(clientName))
    elif cmxData['type'] == "DevicesSeen":
        print("\nWiFi Devices Seen:\n")
        wifiResponse = dashboardWifi()
        parseSeenDevices(cmxData, wifiResponse)
        for clientName in currentDevices:
            print("{} is currently in your vicininty!".format(clientName))
        for clientName, clientTime in previousDevices.items():
            print("{} is no longer in the area but was last nearby at {} EST".format(clientName, timeConvWifi(clientTime)))  
        print()  
    else:
        print("Unknown Device 'type'")
    
    return "CMX POST Received"


if __name__ == '__main__':
    # run app
    app.run(port=8000, debug=False)

