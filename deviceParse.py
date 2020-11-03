from config import currentDevices, previousDevices

# compare seen MACs with connected clients
def getDeviceName(cmxMAC, dashboardResponse):
    for client in dashboardResponse:
        # connected device seen in Scanning API call
        if client['mac'] == cmxMAC:
            if len(client['id']) == 18 and client['name'] is not None: # bluetooth
                #if client['name'] is not None:
                currentDevices.append(client['name'])
                print('{}'.format(client['name']))
            elif len(client['id']) == 7: # wifi
                currentDevices.append((client['description']))
                print('{}'.format(client['description']))
            else:
                print("Unknown device name")


# isolate device mac, location, rssi
def parseSeenDevices(cmxData, dashboardResponse):
    currentDevices.clear()
    previousDevices.clear()
    for device in cmxData['data']['observations']:
        getDeviceName(device['clientMac'], dashboardResponse)
        print('Client MAC = {}'.format(device['clientMac']))
        #print('\tClient Location = {}'.format(device['location']))
        print('Client RSSI = {}'.format(device['rssi']))
        print()
    for client in dashboardResponse:
        if len(client['id']) == 18 and client['name'] is not None and client['name'] not in (currentDevices or previousDevices):
            previousDevices[client['name']] = client['lastSeen']
        elif len(client['id']) == 7 and client['description'] not in (currentDevices or previousDevices): # EFFICIENCY
            previousDevices[client['description']] = client['lastSeen']
