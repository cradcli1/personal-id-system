NUMBER_EMPLOYEES = 4

keyList = ['name', 'firstSeen', 'updatedSeen', 'lastSeen', 'isContinuous', 
            'isAway', 'hasChanged']
deviceHistory = {'deviceList': [{key: None for key in keyList} for number in range(NUMBER_EMPLOYEES)]}

#deviceCount = 0

# deviceHistory = 
#   {
#       'deviceList': [
#           {
#               'name': None,
#               'firstSeen': None,
#               'updatedSeen': None,
#               'lastSeen': None,
#               'isContinuous': None,
#               'isAway': None,  
#               'hasChanged': None
#               'zone':
#           },
#           {
#               'name': None,
#               'firstSeen': None,
#               'updatedSeen': None,
#               'lastSeen': None,
#               'isContinuous': None,
#               'isAway': None,  
#               'hasChanged': None
#           }, 
#           ...
#       ]
#   }

clients = { 'observations': [ 
    {   'name': 'A', 
        'lastSeen': 1 },
    {   'name': 'B', 
        'lastSeen': 2 },
    {   'name': 'C', 
        'lastSeen': 3 },
    {   'name': 'D', 
        'lastSeen': 4 }
    ]
}

# only adding seen... previously seen done in other function
#for client in clients['observations']:
#    for emp in deviceHistory['deviceList']:
#        if emp['name'] is None: # first appearance in list
#            emp['name'] = client['name'] 
#            emp['firstSeen'] = client['lastSeen']
#            break

#print(clients['observations'])

#print(deviceHistory['deviceList'])
#deviceHistory.clear()