import json
import requests
import csv
import time
import os.path
#The numbers used as variable and the geolocations are w.r.t the BCC sensor ID and the placement of those sensors in the selecetd road network.
#Kelvin Grove road 
#API calls 
API_10035_10303=requests.get("https://route.api.here.com/routing/7.2/calculateroute.json?app_id="ENTER APP ID HERE"&app_code="ENTER APP CODE HERE"&waypoint0=geo!-27.4596556832,153.014583501&waypoint1=geo!-27.4511774594,153.010885566&mode=fastest;car;traffic:disabled")
API_10303_10307=requests.get("https://route.api.here.com/routing/7.2/calculateroute.json?app_id="ENTER APP ID HERE"&app_code="ENTER APP CODE HERE"&waypoint0=geo!-27.4511774594,153.010885566&waypoint1=geo!-27.4443529585,153.007455934&mode=fastest;car;traffic:disabled")
API_10307_10303=requests.get("https://route.api.here.com/routing/7.2/calculateroute.json?app_id="ENTER APP ID HERE"&app_code="ENTER APP CODE HERE"&waypoint0=geo!-27.4446214308,153.007716062&waypoint1=geo!-27.4511855477,153.011021478&mode=fastest;car;traffic:disabled")
API_10303_10035=requests.get("https://route.api.here.com/routing/7.2/calculateroute.json?app_id="ENTER APP ID HERE"&app_code="ENTER APP CODE HERE"&waypoint0=geo!-27.4511855477,153.011021478&waypoint1=geo!-27.4598909273,153.014964537&mode=fastest;car;traffic:disabled")
#Json extraction 
X = {}
X["Segment_1"]=1003510303
X["Timestamp"] = API_10035_10303.json()["response"]["metaInfo"]["timestamp"]
X["Free_Flow_Time_1"] = API_10035_10303.json()["response"]["route"][0]["summary"]["baseTime"]
X["Traffic_Time_1"] = API_10035_10303.json()["response"]["route"][0]["summary"]["trafficTime"]
X["Distance_1"]= API_10035_10303.json()["response"]["route"][0]["summary"]["distance"]
X["Segment_2"]=1030310307
X["Free_Flow_Time_2"] = API_10303_10307.json()["response"]["route"][0]["summary"]["baseTime"]
X["Traffic_Time_2"] = API_10303_10307.json()["response"]["route"][0]["summary"]["trafficTime"]
X["Distance_2"] = API_10303_10307.json()["response"]["route"][0]["summary"]["distance"]
X["Segment_3"]=1030710303
X["Free_Flow_Time_3"] = API_10307_10303.json()["response"]["route"][0]["summary"]["baseTime"]
X["Traffic_Time_3"] = API_10307_10303.json()["response"]["route"][0]["summary"]["trafficTime"]
X["Distance_3"] = API_10307_10303.json()["response"]["route"][0]["summary"]["distance"]
X["Segment_4"]=1030310035
X["Free_Flow_Time_4"] = API_10303_10035.json()["response"]["route"][0]["summary"]["baseTime"]
X["Traffic_Time_4"] = API_10303_10035.json()["response"]["route"][0]["summary"]["trafficTime"]
X["Distance_4"] = API_10303_10035.json()["response"]["route"][0]["summary"]["distance"]
#Saving as .csv
filename = "Here_map_KelvinGrove.csv"
#Checking if the file is already created 
file_exists = os.path.isfile(filename)
with open(filename, "a") as f:  # Just use "w" mode in 3.x
    w = csv.DictWriter(f, X.keys(), delimiter=",", lineterminator="\n")
    if not file_exists: #If the file does not exists write the header onto the newly created file
        w.writeheader()

    w.writerow(X) #Else, Only append the extracted information onto the next row in the file
#Milton Road  
#API calls 
API_10182_10080=requests.get("https://route.api.here.com/routing/7.2/calculateroute.json?app_id=SRVnBFmfBJ71awkDteFZ&app_code=TgwZ0by1O4tjs6QkXzTmtw&waypoint0=geo!-27.4661776437,153.012619214&waypoint1=geo!-27.4706772112,152.999830575&mode=fastest;car;traffic:disabled")
API_10080_10128=requests.get("https://route.api.here.com/routing/7.2/calculateroute.json?app_id=SRVnBFmfBJ71awkDteFZ&app_code=TgwZ0by1O4tjs6QkXzTmtw&waypoint0=geo!-27.4706772112,152.999830575&waypoint1=geo!-27.4785649175,152.989312127&mode=fastest;car;traffic:disabled")
API_10128_10080=requests.get("https://route.api.here.com/routing/7.2/calculateroute.json?app_id=SRVnBFmfBJ71awkDteFZ&app_code=TgwZ0by1O4tjs6QkXzTmtw&waypoint0=geo!-27.4784986653,152.989285786&waypoint1=geo!-27.4706044855,152.999814321&mode=fastest;car;traffic:disabled")
API_10080_10182=requests.get("https://route.api.here.com/routing/7.2/calculateroute.json?app_id=SRVnBFmfBJ71awkDteFZ&app_code=TgwZ0by1O4tjs6QkXzTmtw&waypoint0=geo!-27.4706044855,152.999814321&waypoint1=geo!-27.4659986099,153.012601375&mode=fastest;car;traffic:disabled")
#Json extraction 
Time_Stamp_S2 = API_10182_10080.json()["response"]["metaInfo"]["timestamp"]
Free_Flow_Time_10182_10080 = API_10182_10080.json()["response"]["route"][0]["summary"]["baseTime"]
Traffic_Time_10182_10080 = API_10182_10080.json()["response"]["route"][0]["summary"]["trafficTime"]
Distance_10182_10080 = API_10182_10080.json()["response"]["route"][0]["summary"]["distance"]

Free_Flow_Time_10080_10128 = API_10080_10128.json()["response"]["route"][0]["summary"]["baseTime"]
Traffic_Time_10080_10128 = API_10080_10128.json()["response"]["route"][0]["summary"]["trafficTime"]
Distance_10080_10128 = API_10080_10128.json()["response"]["route"][0]["summary"]["distance"]

Free_Flow_Time_10128_10080 = API_10128_10080.json()["response"]["route"][0]["summary"]["baseTime"]
Traffic_Time_10128_10080 = API_10128_10080.json()["response"]["route"][0]["summary"]["trafficTime"]
Distance_10128_10080 = API_10128_10080.json()["response"]["route"][0]["summary"]["distance"]

Free_Flow_Time_10080_10182 = API_10080_10182.json()["response"]["route"][0]["summary"]["baseTime"]
Traffic_Time_10080_10182 = API_10080_10182.json()["response"]["route"][0]["summary"]["trafficTime"]
Distance_10080_10182 = API_10080_10182.json()["response"]["route"][0]["summary"]["distance"]
#Saving as .csv
Y = {}
Y["Timestamp"] = Time_Stamp_S2
Y["Segment_1"]=1018210080
Y["Free_Flow_Time_1"]=Free_Flow_Time_10182_10080
Y["Traffic_Time_1"]=Traffic_Time_10182_10080
Y["Distance_1"]=Distance_10182_10080
Y["Segment_2"]=1008010128
Y["Free_Flow_Time_2"]=Free_Flow_Time_10080_10128
Y["Traffic_Time_2"]=Traffic_Time_10080_10128
Y["Distance_2"]=Distance_10080_10128
Y["Segment_3"]=1012810080
Y["Free_Flow_Time_3"]=Free_Flow_Time_10128_10080
Y["Traffic_Time_3"]=Traffic_Time_10128_10080
Y["Distance_3"]=Distance_10128_10080
Y["Segment_4"]=1008010182
Y["Free_Flow_Time_4"]=Free_Flow_Time_10080_10182
Y["Traffic_Time_4"]=Traffic_Time_10080_10182
Y["Distance_4"]=Distance_10080_10182
filename = "Here_map_MiltonRoad.csv"
#Checking if the file is already created 
file_exists = os.path.isfile(filename)
with open(filename, "a") as f:  # Just use "w" mode in 3.x
    w = csv.DictWriter(f, Y.keys(), delimiter=",", lineterminator="\n")
    if not file_exists: #If the file does not exists write the header onto the newly created file
        w.writeheader()

    w.writerow(Y) #Else, Only append the extracted information onto the next row in the file


#Coronation Drive
#API calls 
API_10221_10181=requests.get("https://route.api.here.com/routing/7.2/calculateroute.json?app_id=SRVnBFmfBJ71awkDteFZ&app_code=TgwZ0by1O4tjs6QkXzTmtw&waypoint0=geo!-27.4688091406,153.010921146&waypoint1=geo!-27.4785548882,152.999575331&mode=fastest;car;traffic:disabled")
API_10181_10152=requests.get("https://route.api.here.com/routing/7.2/calculateroute.json?app_id=SRVnBFmfBJ71awkDteFZ&app_code=TgwZ0by1O4tjs6QkXzTmtw&waypoint0=geo!-27.4785548882,152.999575331&waypoint1=geo!-27.4860809025,152.993312789&mode=fastest;car;traffic:disabled")
API_10152_10181=requests.get("https://route.api.here.com/routing/7.2/calculateroute.json?app_id=SRVnBFmfBJ71awkDteFZ&app_code=TgwZ0by1O4tjs6QkXzTmtw&waypoint0=geo!-27.4859933765,152.993206339&waypoint1=geo!-27.4784860649,152.999516649&mode=fastest;car;traffic:disabled")
API_10181_10021=requests.get("https://route.api.here.com/routing/7.2/calculateroute.json?app_id=SRVnBFmfBJ71awkDteFZ&app_code=TgwZ0by1O4tjs6QkXzTmtw&waypoint0=geo!-27.4784860649,152.999516649&waypoint1=geo!-27.4686911369,153.011057327&mode=fastest;car;traffic:disabled")
#Json extraction 
Time_Stamp_S3 = API_10221_10181.json()["response"]["metaInfo"]["timestamp"]
Free_Flow_Time_10221_10181 = API_10221_10181.json()["response"]["route"][0]["summary"]["baseTime"]
Traffic_Time_10221_10181 = API_10221_10181.json()["response"]["route"][0]["summary"]["trafficTime"]
Distance_10221_10181 = API_10221_10181.json()["response"]["route"][0]["summary"]["distance"]
Free_Flow_Time_10181_10152 = API_10181_10152.json()["response"]["route"][0]["summary"]["baseTime"]
Traffic_Time_10181_10152 = API_10181_10152.json()["response"]["route"][0]["summary"]["trafficTime"]
Distance_10181_10152 = API_10181_10152.json()["response"]["route"][0]["summary"]["distance"]
Free_Flow_Time_10152_10181 = API_10152_10181.json()["response"]["route"][0]["summary"]["baseTime"]
Traffic_Time_10152_10181 = API_10152_10181.json()["response"]["route"][0]["summary"]["trafficTime"]
Distance_10152_10181 = API_10152_10181.json()["response"]["route"][0]["summary"]["distance"]
Free_Flow_Time_10181_10021 = API_10181_10021.json()["response"]["route"][0]["summary"]["baseTime"]
Traffic_Time_10181_10021 = API_10181_10021.json()["response"]["route"][0]["summary"]["trafficTime"]
Distance_10181_10021 = API_10181_10021.json()["response"]["route"][0]["summary"]["distance"]
#Saving as .csv
Z = {}
Z["Timestamp"] = Time_Stamp_S3
Z["Segment_1"]=1022110181
Z["Free_Flow_Time_1"]=Free_Flow_Time_10221_10181
Z["Traffic_Time_1"]=Traffic_Time_10221_10181
Z["Distance_1"]=Distance_10221_10181
Z["Segment_2"]=1018110152
Z["Free_Flow_Time_2"]=Free_Flow_Time_10181_10152
Z["Traffic_Time_2"]=Traffic_Time_10181_10152
Z["Distance_2"]=Distance_10181_10152
Z["Segment_3"]=1015210181
Z["Free_Flow_Time_3"]=Free_Flow_Time_10152_10181
Z["Traffic_Time_3"]=Traffic_Time_10152_10181
Z["Distance_3"]=Distance_10152_10181
Z["Segment_4"]=1018110021
Z["Free_Flow_Time_4"]=Free_Flow_Time_10181_10021
Z["Traffic_Time_4"]=Traffic_Time_10181_10021
Z["Distance_4"]=Distance_10181_10021
filename = "Here_map_CoronationDrive.csv"
#Checking if the file is already created 
file_exists = os.path.isfile(filename)
with open(filename, "a") as f:  # Just use "w" mode in 3.x
    w = csv.DictWriter(f, Z.keys(), delimiter=",", lineterminator="\n")
    if not file_exists: #If the file does not exists write the header onto the newly created file
        w.writeheader()

    w.writerow(Z) #Else, Only append the extracted information onto the next row in the file
