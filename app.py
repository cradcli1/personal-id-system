from requests.models import Response
from dashboardReceivers import getDashboardData
from messageFormatting import formatWhoIsAround
from slackWebhooks import sendMessage
from getData import getData
from array import *

datastore = [{"name": "Christopher Radcliffe",
              "lastState": "", "whereToSend": ""}]
APIHOOK = "https://hooks.slack.com/services/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"

APIResponce = getData("mock", 0, 0, True)
#print("API RESPONCE\n" + str(APIResponce) + "\n")
#print("datastore\n" + str(datastore) + "\n")

if APIResponce:
    messages = []
    for blindUser in datastore:
        givenUserResponce = {}
        # print(blindUser)
        room = APIResponce[blindUser["name"]]["roomID"]
        # print(room)
        for people in APIResponce:
            # print(APIResponce[people])
            # print(APIResponce[people]["roomID"])
            if APIResponce[people]["roomID"] == room and people != blindUser["name"]:
                givenUserResponce[people] = APIResponce[people]
            print(str(givenUserResponce) + "\n\n\n")
    print(formatWhoIsAround(APIResponce))
    messages.append(
        {formatWhoIsAround(APIResponce), blindUser["whereToSend"]})
    try:
        print("SENDING MESSAGE :" + str(messages))
        # sendMessage(givenUserResponce)
    except:
        print("STUFF")
else:
    print("Stuff")
