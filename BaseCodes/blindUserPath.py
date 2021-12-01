from messageFormatting import formatWhoIsAround
from slackWebhooks import sendMessage
from getData import getData
from basicDataSearching import *
import zmq


def blindUserUpdates(datastore, socket):
    APIResponce = getData("mock", 0, 0, True)
    if APIResponce:
        for blindUser in datastore:
            try:
                formatedUserResponce = formatWhoIsAround(whoIsAround(blindUser["name"], APIResponce))
                if blindUser["lastState"] != formatedUserResponce:
                    try:
                        print("SENDING MESSAGE TO " + blindUser["name"] + ": \n" + str(formatedUserResponce))
                        socket.send_string(blindUser["name"] + " | " + formatedUserResponce)
                        print(blindUser["name"] + " | " + formatedUserResponce)
                    except:
                        print("FAILED TO SEND DATA")
                    blindUser["lastState"] = formatedUserResponce
            except:
                print("Blind user is not here")
    else:
        print("FAILED TO RECIEVE  DATA")