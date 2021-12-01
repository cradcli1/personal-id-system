import os
import re
import zmq
import logging
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
from pathlib import Path
from textCompare import *

env_path = Path('.') / '.env'

load_dotenv(dotenv_path=env_path)

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

context1 = zmq.Context()
socket1 = context1.socket(zmq.REQ)
socket1.connect("tcp://localhost:5555")

context2 = zmq.Context()
socket2 = context2.socket(zmq.REP)
socket2.bind("tcp://*:6666")


logger = logging.getLogger(__name__)
#@app.chat_postMessage(channel='#slack-integration', text = "Hello World")



# Add functionality here

name_store = []

@app.middleware  # or app.use(log_request)
def log_request(logger, body, next):
    logger.debug(body)
    return next()

#Obtain name of person users want to locate
@app.event("app_mention")
def mention_response(client, event, body, say, logger):
    logger.info(body)
    message = event["text"][15:]
    messageSplit = message.split('|') #split between message [0] and username [1]
    user = event["user"]
    channel_id = event["channel"]
    if 'where is ' in message:
        say(f"Hi there <@{user}>! You wish to know {messageSplit[0]}")

        #send request
        print(messageSplit[1])
        print(messageSplit[0][:-1])
        response = messageSplit[1] + " | " + messageSplit[0][:-1]
        print(response)
        socket1.send_string(response)

        #obtain response and post to channel where the message was posted in 
        obtain = socket1.recv()
        decoded = obtain.decode()
        client.chat_postMessage(
            channel = channel_id,
            text = decoded
        )
    elif 'who is around me' in message:
        say(f"Hi there <@{user}>! You wish to know who is around you")
        # compare obtained name to storage to get appropriate response
    
        # Set up communication socket to talk to server


        #send request
        print(messageSplit[1])
        print(messageSplit[0][:-1])
        response = messageSplit[1] + " | " + messageSplit[0][:-1]
        print(response)
        socket1.send_string(response)

        #obtain response and post to channel where the message was posted in 
        obtain = socket1.recv()
        decoded = obtain.decode()
        client.chat_postMessage(
            channel = channel_id,
            text = decoded
        )
    

# @app.message(re.compile("(hi|Hi|hello|Hello|hey|Hey)"))
# def ask_who(message, say, context):
#     greeting = context['matches'][0]
#     user = message["user"]
#     say(f"{greeting} there, <@{user}>! Who do you need to locate?")

# @app.message(":wave:")
# def say_hello(message, say):
#     user = message['user']
#     say(f"Hi there, <@{user}>! Who do you need to locate?")

# Obtain the name of the person whose location is wanted in the message of the user
@app.event("message")
def handle_message_events(client, event, body, say, logger):
    logger.info(body)
    message = event["text"]
    messageSplit = message.split('|')
    user = event["user"]
    if 'where is ' in message:
        say(f"Hi there <@{user}>! You wish to know {messageSplit[0]}")
        # compare obtained name to storage to get appropriate response
        #send request
        print(user)
        print(message)
        response = messageSplit[1] + " | " + messageSplit[0][:-1]
        print(response)
        socket1.send_string(response)

        #obtain response and post to channel where the message was posted in 
        obtain = socket1.recv()
        decoded = obtain.decode()
        say(f"{decoded}")
    elif 'who is around me' in message:
        say(f"Hi there <@{user}>! You wish to know who is around you")
        # compare obtained name to storage to get appropriate response
    
        # Set up communication socket to talk to server


        #send request
        print(messageSplit[1])
        print(messageSplit[0][:-1])
        response = messageSplit[1] + " | " + messageSplit[0][:-1]
        print(response)
        socket1.send_string(response)

        #obtain response and post to channel where the message was posted in 
        obtain = socket1.recv()
        decoded = obtain.decode()
        say(f"{decoded}")
    elif 'i am blind' in message:
        say(f"Hi there <@{user}>! Since you are blind, we will be sending you automatic updates")

        response = str(messageSplit[0][:-1]) + " | " + str(messageSplit[1][1:]) + " | " + user[1:]
        print(response)

        socket1.send_string(response)

        message = socket1.recv()
        decoded = message.decode()
        say(f"{decoded}")


@app.error
def global_error_handler(error, body, logger):
    logger.exception(error)
    logger.info(body)

def main():
    handler = SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN"))
    handler.start()

# Start your app
if __name__ == "__main__":
    main()