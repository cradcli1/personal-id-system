datastore = [{"name": "Christopher Radcliffe",
              "lastState": "", "whereToSend": ""}]


def addPersonToDataStore(name, whereToSend):
    for element in datastore:
        if element["name"] == name:
            return
    datastore.append({"name": name, "lastState": "", "whereToSend": whereToSend})
