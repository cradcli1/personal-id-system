# This is the main program that needs to be run in order for everything else to be done


from requests.models import Response
from dashboardReceivers import getDashboardData
from messageFormatting import formatWhoIsAround
from slackWebhooks import sendMessage
from getData import getData
from blindUserPath import blindUserUpdates
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


#Sets blindUserUpdateS to run every minute
schedule.every(1).minutes.do(blindUserUpdates, datastore = datastore)

#Runs it imediatly
blindUserUpdates(datastore)

#Keeps the programming running
while True:
    schedule.run_pending()