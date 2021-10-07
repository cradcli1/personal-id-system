import requests
import os
from slack_sdk.webhook import WebhookClient
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# sample code for posting a message to a Slack channel using a wekhook url
# general channel
#url = "https://hooks.slack.com/services/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"
#webhook = WebhookClient(url)
#response = webhook.send(text = "Hello!")

# testing channel
#url = "https://hooks.slack.com/services/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"
#webhook = WebhookClient(url)
#response = webhook.send(text = "Hello!")

D1 = {
    "API": "https://hooks.slack.com/services/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",
    "message": "Hello to the general channel"
}

D2 = {
    "API": "https://hooks.slack.com/services/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",
    "message": "Hello to the testing channel"
}

A = [D1, D2]


def sendMessage(A):
    for element in A:
        url = element["API"]
        webhook = WebhookClient(url)
        message = element["message"]
        response = webhook.send(text=message)


sendMessage(A)
