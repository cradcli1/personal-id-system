from dashboardReceivers import getDashboardData
from messageFormatting import formatWhoIsAround
dashboardAPIResponce = getDashboardData("mock", 0, 0, True)

if not dashboardAPIResponce:
    print("failed")
else:
    print(dashboardAPIResponce)

message = formatWhoIsAround(dashboardAPIResponce)
print("\n\nMessage: \n" + message)
