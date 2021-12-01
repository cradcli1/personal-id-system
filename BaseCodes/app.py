# This is the main program that needs to be run in order for everything else to be done


from requests.models import Response
from dashboardReceivers import getDashboardData
from messageFormatting import formatWhoIsAround
from slackWebhooks import sendMessage
from getData import getData
from blindUserPath import blindUserUpdates
from array import *
from determineUserInput import determineUserInput
from datastore import *
import schedule
import time
import zmq
import threading


#Set up communication socket
context1 = zmq.Context()
socket1 = context1.socket(zmq.REP)
socket1.bind("tcp://*:5555")

context2 = zmq.Context()
socket2 = context2.socket(zmq.REQ)
socket2.connect("tcp://localhost:6666")

def blindUserThread():
    #Sets blindUserUpdate to run every minute
    schedule.every(1).minutes.do(blindUserUpdates, datastore = datastore, socket = socket2)
    #Runs it imediatly
    blindUserUpdates(datastore, socket2)
    #Keeps the programming running
    while True:
        schedule.run_pending()
        #Whenever slack message comes through, call determineUserInput(user, userInput, webhook)
def intergrationThread():
    while True:
        message = socket1.recv()
        result = message.decode()
        split = result.split('|')
        print("Received: ")
        
        determineUserInput(split[0][1:-1], split[1], socket1)


t1 = threading.Thread(target=blindUserThread, name='t1')
t2 = threading.Thread(target=intergrationThread, name='t2')
t1.start()
t2.start()
t1.join()
t2.join()