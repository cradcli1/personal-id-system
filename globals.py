# Global data to be shared among directory

mainUser = 'Andrea'

NUMBER_EMPLOYEES = 4

keyList = ['isMainUser', 'name', 'firstSeen', 'updatedSeen', 'lastSeen', 'isContinuous', 
            'isAway', 'justLeft', 'zone', 'hasChanged']
deviceHistory = {'deviceList': [{key: None for key in keyList} for number in range(NUMBER_EMPLOYEES)]}

deviceCount = 0 #None

# deviceHistory = 
#   {
#       'deviceList': [
#           {
#               'isMainUser': <bool>
#               'name': <string>,
#               'firstSeen': <int>,
#               'updatedSeen': <int>,
#               'lastSeen': <int>,
#               'isContinuous': <bool>,
#               'isAway': <bool>,  
#               'justLeft': <bool>,  
#               'zone': <int>, # 1 or 2
#               'hasChanged': <bool>
#           },
#           {
#               'isMainUser': <bool>
#               'name': <string>,
#               'firstSeen': <int>,
#               'updatedSeen': <int>,
#               'lastSeen': <int>,
#               'isContinuous': <bool>,
#               'isAway': <bool>,  
#               'justLeft': <bool>,  
#               'zone': <int>, # 1 or 2
#               'hasChanged': <bool>
#           }, 
#           ...
#       ]
#   }