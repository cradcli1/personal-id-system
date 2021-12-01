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
def determineUserInput(user, userInput, socket):
    lower = userInput.lower()
    print(lower)
    
    if 'who is around me' in lower:
        data = getData("mock", 0, 0, True)
        if data:
            try: 
                whoIsNearby = whoIsAround(user, data)
                message = formatWhoIsAround(whoIsNearby)
                print("Slack Message: \n" + message)
                socket.send_string(message)
            except:
                socket.send(b"Failed")
        else:
            socket.send(b"Failed")
    
    elif 'where is ' in lower:
        
        data = getData("mock", 0, 0, True)
        if data:
            try:
                people = userInput[10:]
                print(people) 
                print(len(people)) 
                message = findUserLocation(people, data)
                print("Slack Message: \n" + message)
                socket.send_string(message)
            except:
                socket.send(b"Failed")
        else:
            socket.send_string("Failed")
    
    elif 'i am blind' in lower:
        print("Running code to add a blind person")
        addPersonToDataStore(user)
        socket.send_string("Done")
    else: 
        print("Request Not Found")
        socket.send_string("Request Not Found")
