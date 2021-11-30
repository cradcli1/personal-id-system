from messageFormatting import formatWhoIsAround
from slackWebhooks import sendMessage
from getData import getData
from basicDataSearching import *

def blindUserUpdates(datastore):
    APIResponce = getData("mock", 0, 0, True)
    if APIResponce:
        messages = []
        for blindUser in datastore:
            formatedUserResponce = formatWhoIsAround(whoIsAround(blindUser["name"], APIResponce))
            if blindUser["lastState"] != formatedUserResponce:
                messages.append(
                    {formatedUserResponce, blindUser["whereToSend"]})
                blindUser["lastState"] = formatedUserResponce
        try:
            print("SENDING MESSAGE :" + str(messages))
            # sendMessage(givenUserResponce)
        except:
            print("FAILED TO FORMAT OR SEND DATA")
    else:
        print("FAILED TO RECIEVE  DATA")