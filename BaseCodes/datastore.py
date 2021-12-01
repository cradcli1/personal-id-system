datastore = []


def addPersonToDataStore(name, userID):
    for element in datastore:
        if element["name"] == name:
            return
    datastore.append({"name": name, "lastState": "", "userID": userID})
