from dashboardReceivers import getDashboardData
from scanningReceivers import getScanningData


def getData(networkID, apiKey, apiVersion=1, test=False):
    dashboardAPIResponce = getDashboardData(
        networkID, apiKey, apiVersion, test)
    scanningAPIResponce = getScanningData(
        networkID, apiKey, apiVersion, test)
    if dashboardAPIResponce and scanningAPIResponce:
        for element in dashboardAPIResponce:
            try:
                dashboardAPIResponce[element]["x"] = scanningAPIResponce[dashboardAPIResponce[element]["macAddress"]]["x"]
            except:
                break
            try:
                dashboardAPIResponce[element]["y"] = scanningAPIResponce[dashboardAPIResponce[element]["macAddress"]]["y"]
            except:
                break
            try:
                dashboardAPIResponce[element]["roomID"] = scanningAPIResponce[dashboardAPIResponce[element]
                                                                              ["macAddress"]]["roomID"]
            except:
                break
        return dashboardAPIResponce
    return False
