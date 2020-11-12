# Global data to be shared among directory

NUMBER_EMPLOYEES = 4

keyList = ['name', 'firstSeen', 'updatedSeen', 'lastSeen', 'isContinuous', 
            'isAway', 'hasChanged']
deviceHistory = {'deviceList': [{key: None for key in keyList} for number in range(NUMBER_EMPLOYEES)]}

deviceCount = None

# deviceHistory = 
#   {
#       'deviceList': [
#           {
#               'name': <string>,
#               'firstSeen': <int>,
#               'updatedSeen': <int>,
#               'lastSeen': <int>,
#               'isContinuous': <bool>,
#               'isAway': <bool>,  
#               'hasChanged': <bool>,
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