import os
import requests, json

# dashboard call for connected WiFi clients
def dashboardWifi():
    url = os.environ['MERAKI_URL_WIFI']

    payload = {}
    headers = {
        'X-Cisco-Meraki-API-Key': os.environ['MERAKI_DASHBOARD_API_KEY']
    }

    responseWifi = requests.request("GET", url, headers=headers, data = payload)
    responseWifi = json.loads(responseWifi.text.encode('utf8'))
    return responseWifi

# dashboard call for connected BT clients
def dashboardBT():
    url = os.environ['MERAKI_URL_BT']

    payload = {}
    headers = {
        'X-Cisco-Meraki-API-Key': os.environ['MERAKI_DASHBOARD_API_KEY']
    }

    responseBT = requests.request("GET", url, headers=headers, data = payload)
    responseBT = json.loads(responseBT.text.encode('utf8'))
    return responseBT    

def getNetworkInfo():
    url = "https://api.meraki.com/api/v1/organizations/877530/networks"

    payload = {}
    headers = {
        'X-Cisco-Meraki-API-Key': '9b14ebe4396e70c0aa903f0915edabf4794ca47b'
    }

    responseNwk = requests.request("GET", url, headers=headers, data = payload)
    responseNwk = json.loads(responseNwk.text.encode('utf8'))
    return responseNwk