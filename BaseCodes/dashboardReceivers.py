# This code contains the receivers for the the dashboard API, either version 1 or 2 Some sample data is shown at the base of the program
import requests
import json

BASEURL = "http://app.meraki.com/api"
V0EXTENTION = "/v0"
V1EXTENTION = "/v1"
TESTURL = "http://localhost:8080"
APIKEYHEADER = 'X-Cisco-Meraki-API-Key'


def dashboardAPICall(networkID, apiKey, apiVersion=1, test=False):
    # If connecting to test server
    url = ""

    if not test:
        url = BASEURL
        if apiVersion != 1:
            url = url + V0EXTENTION
        else:
            url = url + V1EXTENTION
    else:
        url = TESTURL

    url = url + "/networks/" + networkID + "/clients"

    payload = {}
    headers = {}
    responseBT = requests.request(
        "GET", url, headers=headers, data=payload)
    responseBT = json.loads(responseBT.text.encode('utf8'))
    return responseBT


def getDashboardData(networkID, apiKey, apiVersion=1, test=False):
    returnValue = {}
    try:
        data = dashboardAPICall(networkID, apiKey, apiVersion, test)
        for element in data:
            returnValue[element["user"]] = {
                "id": element["id"],
                "description": element["description"],
                "macAddress": element["mac"],
            }
        return returnValue
    except:
        return False

# IF THE API CALL FAILS OR DATA CAN'T BE FORMATTED THEN THE RETURN VALUE WILL BE THE BOOLEAN VALUE FALSE (SEE LINE 47).

# Once data has been returned from getScanningData it be:
# An array of dictionarys who's keys to access them is the name of the user of the device, 
# the dictionary contians the the user'sID and description as well as their devices mac address.


# [
#     {
#         "usage": { "sent": 138, "recv": 61 },
#         "id": "k74272e",
#         "description": "Christopher's phone",
#         "mac": "11:22:33:44:55:66",
#         "ip": "1.2.3.4",
#         "user": "Christopher Radcliffe",
#         "vlan": 255,
#         "switchport": null,
#         "ip6": "",
#         "firstSeen": Math.round(Date.now() / 1000) - 100,
#         "lastSeen": Math.round(Date.now() / 1000),
#         "manufacturer": "Apple",
#         "os": "iOS",
#         "recentDeviceSerial": "Q234-ABCD-5678",
#         "recentDeviceName": "My AP",
#         "recentDeviceMac": "00:11:22:33:44:55",
#         "ssid": "My SSID",
#         "status": "Online",
#         "notes": "My client note",
#         "ip6Local": "fe80:0:0:0:1430:aac1:6826:75ab",
#         "smInstalled": true,
#         "groupPolicy8021x": "Student_Access"
#     },
#     {
#         "usage": { "sent": 138, "recv": 61 },
#         "id": "e53624x",
#         "description": "Miles's phone",
#         "mac": "22:33:44:55:66:77",
#         "ip": "1.2.3.4",
#         "user": "Miles Meraki",
#         "vlan": 255,
#         "switchport": null,
#         "ip6": "",
#         "firstSeen": Math.round(Date.now() / 1000) - 3000,
#         "lastSeen": Math.round(Date.now() / 1000),
#         "manufacturer": "Apple",
#         "os": "iOS",
#         "recentDeviceSerial": "Q234-ABCD-5678",
#         "recentDeviceName": "My AP",
#         "recentDeviceMac": "00:11:22:33:44:55",
#         "ssid": "My SSID",
#         "status": "Online",
#         "notes": "My client note",
#         "ip6Local": "fe80:0:0:0:1430:aac1:6826:75ab",
#         "smInstalled": true,
#         "groupPolicy8021x": "Student_Access"
#     },
#     {
#         "usage": { "sent": 138, "recv": 61 },
#         "id": "g5d2734",
#         "description": "John's phone",
#         "mac": "33:44:55:66:77:88",
#         "ip": "1.2.3.4",
#         "user": "John Snow",
#         "vlan": 255,
#         "switchport": null,
#         "ip6": "",
#         "firstSeen": Math.round(Date.now() / 1000) - 3600,
#         "lastSeen": Math.round(Date.now() / 1000),
#         "manufacturer": "Apple",
#         "os": "iOS",
#         "recentDeviceSerial": "Q234-ABCD-5678",
#         "recentDeviceName": "My AP",
#         "recentDeviceMac": "00:11:22:33:44:55",
#         "ssid": "My SSID",
#         "status": "Online",
#         "notes": "My client note",
#         "ip6Local": "fe80:0:0:0:1430:aac1:6826:75ab",
#         "smInstalled": true,
#         "groupPolicy8021x": "Student_Access"
#     }
# ]