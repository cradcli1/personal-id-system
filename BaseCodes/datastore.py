datastore = [{"name": "Christopher Radcliffe",
              "lastState": "", "whereToSend": ""}]


def addPersonToDataStore(name):
    for element in datastore:
        if element["name"] == name:
            return
    datastore.append({"name": name, "lastState": ""})
