from flask import Flask, json, request
import time, schedule

# init a flash web app
app = Flask(__name__)

# validate web server from meraki
@app.route('/', methods=['GET'])
def get_validator():
    return "99dfc74e4abb542eeb07195a89161d5303da09ab"

def get_cmxJSON():
    cmxdata = request.json
    # Determine device type
    if cmxdata['type'] == "DevicesSeen":
        print("WiFi Devices Seen")
    elif cmxdata['type'] == "BluetoothDevicesSeen":
        print("Bluetooth Devices Seen")
        for device in cmxdata['data']['observations']:
            # print('Associated Access Point MAC= {}'.format(cmxdata['data']['apMac']))
            print('Client MAC = {}'.format(device['clientMac']))
            # print('Client Location = {}'.format(device['location']))
            print('RSSI = {}'.format(device['rssi']))
            print()
    else:
        print("Unknown Device 'type'")

    return "CMX POST"

# receive location data
@app.route('/', methods=['POST'])
def post_JSON():
    schedule.every(30).seconds.do(get_cmxJSON)

    return "CMX Received"



if __name__ == '__main__':
    # run app
    app.run(port=8000, debug=False)
