#This recieves the data and stiches it accordingly.

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
                dashboardAPIResponce[element]["y"] = scanningAPIResponce[dashboardAPIResponce[element]["macAddress"]]["y"]
                dashboardAPIResponce[element]["roomID"] = scanningAPIResponce[dashboardAPIResponce[element]
                                                                              ["macAddress"]]["roomID"]
                dashboardAPIResponce[element]["floorPlanName"] = scanningAPIResponce[dashboardAPIResponce[element]
                                                                              ["macAddress"]]["floorPlanName"]
            except:
                break
        return dashboardAPIResponce
    return False

# IF THE DASHBOARDAPI CALL FAILS, THE SCANNINGAPI CALL FAILS, OR IT FAILS TO STITCH THEN THE RETURN VALUE WILL BE THE BOOLEAN VALUE FALSE (SEE LINE 23).
