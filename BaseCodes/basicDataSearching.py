#Basic ways to seach the data recieved

def whoIsAround(user, APIResponce):
    givenUserResponce = {}
    room = APIResponce[user]["roomID"]
    for people in APIResponce:
        if APIResponce[people]["roomID"] == room and people != user:
            givenUserResponce[people] = APIResponce[people]
    return givenUserResponce
#Will return a dictionary of dictionarys with the first depth keys being the name of the user, and the second depth being the rest of the information

def findUserLocation(personToFind, APIResponce):
    return APIResponce[personToFind]["floorPlanName"]