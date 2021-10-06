def formatWhoIsAround(nearbyUsers):
    message = "Currently nearby you are \n"
    for element in nearbyUsers:
        message = message + element["user"] + "\n"
    return message
