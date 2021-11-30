#This program is for formatting thee messages once the data has been aranged correctly.

#Given an array of dictionarys whos key is the user's name, or an  array of strings 
#Will return the message to send
def formatWhoIsAround(nearbyUsers):
    try: 
        message = "Currently nearby you are: \n"
        for key in nearbyUsers:
            message = message + key + "\n"
        return message
    except:
        False
#IF IT FAILS THE RETURN WILL BE FALSE