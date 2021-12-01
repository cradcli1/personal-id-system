datastore = [{"name": "Christopher Radcliffe",
              "lastState": ""}]


def addPersonToDataStore(name):
    for element in datastore:
        if element["name"] == name:
            return
    datastore.append({"name": name, "lastState": ""})
