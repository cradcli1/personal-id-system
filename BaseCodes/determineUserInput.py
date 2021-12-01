import re
from messageFormatting import formatWhoIsAround
from basicDataSearching import *
from getData import *
from datastore import *
import zmq


#User input options:
# 1. Who is around me
# 2. Where is __________
# 3. I am blind

#User: name of user, string
#input: user input, string
def determineUserInput(user, userInput):
    lower = userInput.lower()
    
    if 'who is around me' in lower:
        data = getData("mock", 0, 0, True)
        if data:
            message = formatWhoIsAround(whoIsAround(user, data))
            print("Slack Message: \n" + message)
            socket.send(message)
        else:
            socket.send(b"Failed")
    
    elif 'where is ' in lower:
        data = getData("mock", 0, 0, True)
        if data:
            message = findUserLocation(user, data)
            socket.send(message)
        else:
            socket.send(b"Failed")
    
    elif 'i am blind' in lower:
        print("Running code to add a blind person")
        addPersonToDataStore(user, webhook)
        socket.send(b"Done")
    else: 
        print("Running code to add a blind person")
        socket.send(b"Error")
        #SEND ERROR MESSAGE !!!!!!!HOANG