from datetime import datetime, timedelta
import time
import dateutil.relativedelta

def getLastSeen(clientName, currentTime, btResponse):
    for client in btResponse:
        name = client['name']
        if name == clientName:
            lastEpoch = client['lastSeen']
            lastSeenTime = datetime.fromtimestamp(lastEpoch) # YYYY-MM-DD HH:MM:SS
            diffEpoch = dateutil.relativedelta.relativedelta (currentTime, lastSeenTime)

            # same day only
            if diffEpoch.day is None:
                message = "{} was last seen".format(name)
                if diffEpoch.hours > 0:
                    message += " {} hour".format(diffEpoch.hours)
                    if diffEpoch.hours > 1:
                        message += "s"
                if diffEpoch.minutes > 0:
                    message += " {} minute".format(diffEpoch.minutes)
                    if diffEpoch.minutes > 1:
                        message += "s"
                if diffEpoch.seconds > 0:
                    message += " {} seconds ago.".format(diffEpoch.seconds)
    return message

# returns time only; only used in preliminary wifi testing
def timeConvWifi(lastSeen):
    lastSeen = lastSeen[-9:-1] # DOES NOT ACCOUNT FOR DAY
    hour = int(lastSeen[:2])
    hour -= 4
    lastSeen = str(hour) + lastSeen[2:]

    return lastSeen