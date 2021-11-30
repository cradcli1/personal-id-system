import re
from app import addPersonToDataStore
from messageFormatting import formatWhoIsAround
from basicDataSearching import *

#User input options:
# 1. Who is around me
# 2. Where is __________
# 3. I am blind

#User: name of user, string
#input: user input, string
def determineUserInput(user, userInput, webhook):
    lower = userInput.lower()
    
    if 'who is around me' is in lower:
        data = APIResponce = getData("mock", 0, 0, True)
        if data:
            message = formatWhoIsAround(whoIsAround(user, data))
            print("Slack Message: \n" + message)
        else:
            print("Data failed who is around")
    
    else if 'where is ' is in lower:
        data = APIResponce = getData("mock", 0, 0, True)
        #Person code needs work
        if data:
            #message = findUserLocation(user, data)
            print("Slack Message: \n" + message)
        else:
            print("Data failed where is")
    
    else if 'i am blind' is in lower:
        print("Running code to add a blind person")
        addPersonToDataStore(user, webhook)
        #SEND CONFIRMATION MESSAGE !!!!!!!HUANG
    else: 
        print("Running code to add a blind person")
        #SEND ERROR MESSAGE !!!!!!!HUANG