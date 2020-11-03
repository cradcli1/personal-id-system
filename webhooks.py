import requests

def sendMessage(message):
    url = 'https://webexapis.com/v1/webhooks/incoming/Y2lzY29zcGFyazovL3VzL1dFQkhPT0svNzgxMWIyNTQtNTZjYS00NTdkLWI0M2MtM2JjOGY0N2U1OTky'
    myObj = {'text': message}

    requests.post(url, data = myObj)