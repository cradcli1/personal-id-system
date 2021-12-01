# This is the main program that needs to be run in order for everything else to be done


from requests.models import Response
from dashboardReceivers import getDashboardData
from messageFormatting import formatWhoIsAround
from slackWebhooks import sendMessage
from getData import getData
from blindUserPath import blindUserUpdates
from array import *
from determineUserInput import determineUserInput
import schedule
import time
import zmq
import threading

datastore = [{"name": "Christopher Radcliffe",
              "lastState": "", "whereToSend": ""}]


def addPersonToDataStore(name, whereToSend):
    for element in datastore:
        if element["name"] == name:
            return
    datastore.append({"name": name, "lastState": "", "whereToSend": whereToSend})

#Set up communication socket
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

def blindUserThread():
    #Sets blindUserUpdate to run every minute
    schedule.every(1).minutes.do(blindUserUpdates, datastore = datastore)
    #Runs it imediatly
    blindUserUpdates(datastore)
    #Keeps the programming running
    while True:
        schedule.run_pending()
        #Whenever slack message comes through, call determineUserInput(user, userInput, webhook)
def intergrationThread():
    while True:
        message = socket.recv()
        result = message.decode()
        split = result.split('|')
        
        determineUserInput(split[0], split[1])


t1 = threading.Thread(target=blindUserThread, name='t1')
t2 = threading.Thread(target=intergrationThread, name='t2')
t1.start()
t2.start()
t1.join()
t2.join()