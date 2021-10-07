def formatWhoIsAround(nearbyUsers):
    message = "Currently nearby you are: \n"
    for key in nearbyUsers:
        message = message + key + "\n"
    return message
