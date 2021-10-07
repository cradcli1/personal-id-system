from dashboardReceivers import getDashboardData
from messageFormatting import formatWhoIsAround
from slackWebhooks import sendMessage

APIHOOK = "https://hooks.slack.com/services/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"
dashboardAPIResponce = getDashboardData("mock", 0, 0, True)
print("\nDataReceived\n-----------------------------------\n" +
      str(dashboardAPIResponce))
if dashboardAPIResponce:
    message = formatWhoIsAround(dashboardAPIResponce)
    print("\n\nMessage: \n" + message + "\n")
    print("Sent To:\n" + APIHOOK)
    slackMessage = [{
        "API": APIHOOK,
        "message": message
    }]
    sendMessage(slackMessage)
