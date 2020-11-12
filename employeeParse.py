from globals import keyList, deviceHistory, deviceCount, NUMBER_EMPLOYEES

# compare seen Scanning MACs with connected Dashboard MACs
# assign nearby employee info
def setNearbyEmployees(cmxMAC, dashboardResponse):
    global deviceCount

    for client in dashboardResponse:
        # client seen in both API calls
        if client['mac'] == cmxMAC:
            # bluetooth
            if len(client['id']) == 18 and client['name'] is not None: 
                # first check if employee is in deviceHistory to prevent duplicate entries
                for employee in deviceHistory['deviceList']:
                    # previously seen
                    if employee['name'] == client['name']:
                        # returning employee
                        if employee['isAway'] is True:
                            employee['firstSeen'] = client['lastSeen']
                            employee['lastSeen'] = None
                            employee['hasChanged'] = True
                        # continuous sighting
                        else:
                            employee['isContinuous'] = True
                            employee['hasChanged'] = False

                        employee['updatedSeen'] = client['lastSeen']
                        employee['isAway'] = False
                        deviceCount += 1

                        #print('{}'.format(client['name']))
                        break
                    # employee's intitial sighting
                    elif employee['name'] is None: 
                        employee['name'] = client['name'] 
                        employee['firstSeen'] = client['lastSeen']
                        employee['updatedSeen'] = client['lastSeen']
                        employee['isContinuous'] = False
                        employee['isAway'] = False
                        employee['hasChanged'] = True
                        deviceCount += 1
                        break
                    else:
                        continue
            # wifi
            elif len(client['id']) == 7: 
                for employee in deviceHistory['deviceList']:
                    # client previously and currently seen 
                    if employee['name'] == client['description']:
                        print('{}'.format(client['description']))
                        break
                for employee in deviceHistory['deviceList']:
                    # client first sighting and assign time
                    if employee['name'] is None: 
                        employee['name'] = client['description'] 
                        employee['firstSeen'] = client['lastSeen']
                        print('{}'.format(client['description']))
                        break
            else:
                continue

# assign away employee info    
def setAwayEmployees():
    global deviceCount

    for employee1 in deviceHistory['deviceList']:
        if employee1['isAway'] is False:
            for employee2 in deviceHistory['deviceList']:
                if employee1['name'] != employee2['name'] and employee2['isAway'] is False:
                    if employee1['updatedSeen'] < employee2['updatedSeen']:
                        employee1['lastSeen'] = employee1['updatedSeen']
                        employee1['firstSeen'] = None
                        employee1['isContinuous'] = False
                        employee1['isAway'] = True
                        employee1['hasChanged'] = True
                        deviceCount -= 1
                        break
                    elif employee2['updatedSeen'] < employee1['updatedSeen']:
                        employee2['lastSeen'] = employee2['updatedSeen']
                        employee2['firstSeen'] = None
                        employee2['isContinuous'] = False
                        employee2['isAway'] = True
                        employee2['hasChanged'] = True
                        deviceCount -= 1
                        continue
                    else:
                        continue

# set both nearby and away employees
# create employee count message
def setEmployeeInfo(cmxData, dashboardResponse):
    global deviceCount
    deviceCount = 0
    employeeCountMsg = ""

    for seenDevice in cmxData['data']['observations']:
        setNearbyEmployees(seenDevice['clientMac'], dashboardResponse)
        #print('Client MAC = {}'.format(seenDevice['clientMac']))
        #print('Client RSSI = {}\n'.format(seenDevice['rssi']))
    
    setAwayEmployees()

    if deviceCount >= NUMBER_EMPLOYEES:
        employeeCountMsg += "COVID WARNING!\n"
        
    employeeCountMsg += "{} employees are currently in the area\n".format(str(deviceCount))

    return employeeCountMsg