from requests.models import Response
from dashboardReceivers import getDashboardData
from messageFormatting import formatWhoIsAround
from slackWebhooks import sendMessage
from getData import getData
from array import *
import schedule
import time

datastore = [{"name": "Christopher Radcliffe",
              "lastState": "", "whereToSend": ""}]
APIHOOK = "https://hooks.slack.com/services/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"
def addPersonToDataStore(name, whereToSend):
    for element in datastore:
        if element["name"] == name:
            return
    datastore.append({"name": name, "lastState": "", "whereToSend": whereToSend})
def whoIsAround(user, APIResponce):
    givenUserResponce = {}
    room = APIResponce[user]["roomID"]
    for people in APIResponce:
        if APIResponce[people]["roomID"] == room and people != user:
            givenUserResponce[people] = APIResponce[people]
    return givenUserResponce

def findUserLocation(personToFind, APIResponce):
    return APIResponce[personToFind]["floorPlanName"]

def blindUserUpdatesMain():
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
            print("STUFF")
    else:
        print("Stuff")



schedule.every(1).minutes.do(blindUserUpdatesMain)
blindUserUpdatesMain()
while True:
    schedule.run_pending()