from dashboardReceivers import getDashboardData
from messageFormatting import formatWhoIsAround
from slackWebhooks import sendMessage
dashboardAPIResponce = getDashboardData("mock", 0, 0, True)
print("\nDataReceived\n-----------------------------------\n" +
      str(dashboardAPIResponce))
if dashboardAPIResponce:
    message = formatWhoIsAround(dashboardAPIResponce)
    print("\n\nMessage: \n" + message)
    slackMessage = [{
        "API": "https://hooks.slack.com/services/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",
        "message": message
    }]
    sendMessage(slackMessage)
