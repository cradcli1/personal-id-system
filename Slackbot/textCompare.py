D1 = {
    "name" : "Hoang Nguyen", 
    "lastState" : "Room 1",
    "whereToSend": "ABC"
}

D2 = {
    "name" : "Hoang Nguyen", 
    "lastState" : "Room 2",
    "whereToSend": "DEF"
}

D3 = {
    "name" : "Christopher Radcliffe", 
    "lastState" : "Room 3",
    "whereToSend": "GHI"
}
    
D4 = {
    "name" : "Sarvesh Kulkarni", 
    "lastState" : "Room 1",
    "whereToSend": "JKL"
}
    
A = [D1, D2, D3, D4]

def textCompare(array):
    name = "Hoang Nguyen"
    result = []
    for i in array:
        for value in i.values():
            if name in value:
                result.append(i)
    return result

def printResult(array):
    message = array[-1]
    name = message["name"]
    lastState = message["lastState"]
    whereToSend = message["whereToSend"]
    return [name, lastState, whereToSend]