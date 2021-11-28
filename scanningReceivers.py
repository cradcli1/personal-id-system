# This code contains the receivers for the the dashboard API, either version 1 or 2
import requests
import json

BASEURL = "http://app.meraki.com/api"
V0EXTENTION = "/v0"
V1EXTENTION = "/v1"
TESTURL = "http://localhost:8081"
APIKEYHEADER = 'X-Cisco-Meraki-API-Key'


def scanningAPICall(networkID, apiKey, apiVersion=1, test=False):
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


def getScanningData(networkID, apiKey, apiVersion=1, test=False):
    returnValue = {}
    try:
        data = scanningAPICall(networkID, apiKey, apiVersion, test)

        for element in data["data"]["observations"]:
            returnValue[element["clientMac"]] = {
                "x": element["locations"][len(element["locations"])-1]["x"],
                "y": element["locations"][len(element["locations"])-1]["y"],
                "roomID": element["locations"][len(element["locations"])-1]["floorPlanId"],
                "floorPlanName": element["locations"][len(element["locations"])-1]["floorPlanName"]
            }
        return returnValue
    except:
        return False
