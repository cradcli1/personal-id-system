from dashboardReceivers import getDashboardData
from messageFormatting import formatWhoIsAround
from slackWebhooks import sendMessage
dashboardAPIResponce = getDashboardData("mock", 0, 0, True)

if not dashboardAPIResponce:
    print("failed")
else:
    print(dashboardAPIResponce)

message = formatWhoIsAround(dashboardAPIResponce)
print("\n\nMessage: \n" + message)

slackMessage = [{
    "API": "https://hooks.slack.com/services/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",
    "message": message
}]
sendMessage(slackMessage)
