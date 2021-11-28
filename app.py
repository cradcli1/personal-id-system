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


def main():
    APIResponce = getData("mock", 0, 0, True)
    if APIResponce:
        messages = []
        for blindUser in datastore:
            givenUserResponce = {}
            # print(blindUser)
            room = APIResponce[blindUser["name"]]["roomID"]
            # print(room)
            for people in APIResponce:
                print(people != blindUser["name"])
                if APIResponce[people]["roomID"] == room and people != blindUser["name"]:
                    givenUserResponce[people] = APIResponce[people]
            formatedUserResponce = formatWhoIsAround(givenUserResponce)
            print(formatedUserResponce)
            print(blindUser["lastState"])
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

schedule.every(1).minutes.do(main)
main()
while True:
    schedule.run_pending()