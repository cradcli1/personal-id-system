from globals import mainUser, keyList, deviceHistory, deviceCount, NUMBER_EMPLOYEES

# compare seen Scanning MACs with connected Dashboard MACs
# assign nearby employee info
def setNearbyEmployees(cmxMAC, dashboardResponse):
    global deviceCount
    global mainUser

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
                            employee['isAway'] = False
                            employee['hasChanged'] = True
                        # continuous sighting
                        else:
                            employee['isContinuous'] = True
                            employee['hasChanged'] = False

                        employee['updatedSeen'] = client['lastSeen']
                        #deviceCount += 1

                        #print('{}'.format(client['name']))
                        break
                    # employee's intitial sighting
                    elif employee['name'] is None: 
                        if client['name'] == mainUser:
                            employee['isMainUser'] = True
                            employee['name'] = 'You'
                        else:
                            employee['isMainUser'] = False
                            employee['name'] = client['name'] 
                            #deviceCount += 1
                                                    
                        employee['firstSeen'] = client['lastSeen']
                        employee['updatedSeen'] = client['lastSeen']
                        employee['isContinuous'] = False
                        employee['isAway'] = False
                        employee['hasChanged'] = True
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

    # compare last in range employees
    # employees with lower updatedSeen times are 
    for employee1 in deviceHistory['deviceList']:
        if employee1['isAway'] is False and employee1['isMainUser'] is False:
            for employee2 in deviceHistory['deviceList']:
                if employee1['name'] != employee2['name'] and employee2['isAway'] is False:
                    if employee1['updatedSeen'] < employee2['updatedSeen']:
                        employee1['firstSeen'] = None
                        employee1['lastSeen'] = employee1['updatedSeen']
                        employee1['isContinuous'] = False
                        employee1['isAway'] = True
                        employee1['justLeft'] = True
                        employee1['hasChanged'] = True
                        #deviceCount -= 1
                        break
                    elif employee2['updatedSeen'] < employee1['updatedSeen']:
                        employee2['firstSeen'] = None
                        employee2['lastSeen'] = employee2['updatedSeen']
                        employee2['isContinuous'] = False
                        employee2['isAway'] = True
                        employee2['justLeft'] = True
                        employee2['hasChanged'] = True
                        #deviceCount -= 1
                        break
                    else:
                        continue

# set both nearby and away employees
# create employee count message
def setEmployeeInfo(cmxData, dashboardResponse):
    #global deviceCount
    #deviceCount = 0

    for seenDevice in cmxData['data']['observations']:
        setNearbyEmployees(seenDevice['clientMac'], dashboardResponse)
        #print('Client MAC = {}'.format(seenDevice['clientMac']))
        #print('Client RSSI = {}\n'.format(seenDevice['rssi']))
    
    setAwayEmployees()

def employeeCount():
    global deviceCount
    deviceCount = 0
    employeeCountMsg = ""

    #for employee in deviceHistory['deviceList']:
    #    if employee['isAway'] is None:
    #        deviceCount += 1

    if deviceCount >= NUMBER_EMPLOYEES - 1:
        employeeCountMsg += "COVID WARNING! AREA AT CAPACITY!\n"
        
    employeeCountMsg += "{} other employees are currently in the area.".format(str(deviceCount - 1))

    return employeeCountMsg