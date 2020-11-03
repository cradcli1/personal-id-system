import os #.path
#import sys
import requests, json

#sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# dashboard call for connected WiFi clients
def dashboardWifi():
    url = "https://api.meraki.com/api/v1/networks/L_634444597505819269/clients/"

    payload = {}
    headers = {
    'X-Cisco-Meraki-API-Key': os.environ['MERAKI_DASHBOARD_API_KEY']
    }

    responseWifi = requests.request("GET", url, headers=headers, data = payload)
    responseWifi = json.loads(responseWifi.text.encode('utf8'))
    return responseWifi

# dashboard call for connected BT clients
def dashboardBT():
    url = "https://api.meraki.com/api/v1/networks/L_634444597505819269/bluetoothClients?perPage=20"

    payload = {}
    headers = {
    'X-Cisco-Meraki-API-Key': os.environ['MERAKI_DASHBOARD_API_KEY']
    }

    responseBT = requests.request("GET", url, headers=headers, data = payload)
    responseBT = json.loads(responseBT.text.encode('utf8'))
    return responseBT    