import json
import requests
import csv
import time
import os.path
#The numbers used as variable and the geolocations are w.r.t the BCC sensor ID and the placement of those sensors in the selecetd road network.
#Kelvin Grove road 
#API calls 
API_10035_10303=requests.get("https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins=-27.4596556832,153.014583501&destinations=-27.4511774594,153.010885566&travelMode=driving&timeUnit=second&key="ENTER API KEY HERE")
API_10303_10307=requests.get("https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins=-27.4511774594,153.010885566&destinations=-27.4443529585,153.007455934&travelMode=driving&timeUnit=second&key="ENTER API KEY HERE")
API_10307_10303=requests.get("https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins=-27.4446214308,153.007716062&destinations=-27.4511855477,153.011021478&travelMode=driving&timeUnit=second&key="ENTER API KEY HERE")
API_10303_10035=requests.get("https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins=-27.4511855477,153.011021478&destinations=-27.4598909273,153.014964537&travelMode=driving&timeUnit=second&key="ENTER API KEY HERE")
#Json extraction 
Distance_10035_10303=API_10035_10303.json()["resourceSets"][0]["resources"][0]["results"][0]["travelDistance"]
Time_10035_10303=API_10035_10303.json()["resourceSets"][0]["resources"][0]["results"][0]["travelDuration"]
Distance_10303_10307=API_10303_10307.json()["resourceSets"][0]["resources"][0]["results"][0]["travelDistance"]
Time_10303_10307=API_10303_10307.json()["resourceSets"][0]["resources"][0]["results"][0]["travelDuration"]
Distance_10307_10303=API_10307_10303.json()["resourceSets"][0]["resources"][0]["results"][0]["travelDistance"]
Time_10307_10303=API_10307_10303.json()["resourceSets"][0]["resources"][0]["results"][0]["travelDuration"]
Distance_10303_10035=API_10303_10035.json()["resourceSets"][0]["resources"][0]["results"][0]["travelDistance"]
Time_10303_10035=API_10303_10035.json()["resourceSets"][0]["resources"][0]["results"][0]["travelDuration"]
#Saving as .csv 
X={}
ts = int(time.time())
X["Timestamp"] = ts
X["Segment_1"]= 1003510303 
X["Time_1"] = Time_10035_10303
X["Distance_1"] = Distance_10035_10303
X["Segment_2"]= 1030310307
X["Time_2"] = Time_10303_10307
X["Distance_2"] = Distance_10303_10307
X["Segment_3"]= 1030710303
X["Time_3"] = Time_10307_10303
X["Distance_3"] = Distance_10307_10303
X["Segment_4"]= 1030310035
X["Time_4"] = Time_10303_10035
X["Distance_4"] = Distance_10303_10035
filename = "Bing_map_KelvinGrove.csv"
file_exists = os.path.isfile(filename)
with open(filename, "a") as f:  # Just use "w" mode in 3.x
    w = csv.DictWriter(f, X.keys(), delimiter=",", lineterminator="\n")
    # condition checks if the .csv file exists. In case its true, no need to add the headers on to the existing csv instead just append the information on to the next row.
    if not file_exists:
        w.writeheader()

    w.writerow(X)


#Coronation Drive 
#API calls 
API_10221_10181=requests.get("https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins=-27.4688091406,153.010921146&destinations=-27.4785548882,152.999575331&travelMode=driving&timeUnit=second&key=AmNLMVwCflw6GxKxfDThujTfsVEkABm1zx6aWyhfBfwJ2o0MMu9VRjjXsSwHrGnn")
API_10181_10152=requests.get("https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins=-27.4785548882,152.999575331&destinations=-27.4860809025,152.993312789&travelMode=driving&timeUnit=second&key=AmNLMVwCflw6GxKxfDThujTfsVEkABm1zx6aWyhfBfwJ2o0MMu9VRjjXsSwHrGnn")
API_10152_10181=requests.get("https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins=-27.4859933765,152.993206339&destinations=-27.4784860649,152.999516649&travelMode=driving&timeUnit=second&key=AmNLMVwCflw6GxKxfDThujTfsVEkABm1zx6aWyhfBfwJ2o0MMu9VRjjXsSwHrGnn")
API_10181_10021=requests.get("https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins=-27.4784860649,152.999516649&destinations=-27.4686911369,153.011057327&travelMode=driving&timeUnit=second&key=AmNLMVwCflw6GxKxfDThujTfsVEkABm1zx6aWyhfBfwJ2o0MMu9VRjjXsSwHrGnn")
#Json extraction 
Distance_10221_10181=API_10221_10181.json()["resourceSets"][0]["resources"][0]["results"][0]["travelDistance"]
Time_10221_10181=API_10221_10181.json()["resourceSets"][0]["resources"][0]["results"][0]["travelDuration"]
Distance_10181_10152=API_10181_10152.json()["resourceSets"][0]["resources"][0]["results"][0]["travelDistance"]
Time_10181_10152=API_10181_10152.json()["resourceSets"][0]["resources"][0]["results"][0]["travelDuration"]
Distance_10152_10181=API_10152_10181.json()["resourceSets"][0]["resources"][0]["results"][0]["travelDistance"]
Time_10152_10181=API_10152_10181.json()["resourceSets"][0]["resources"][0]["results"][0]["travelDuration"]
Distance_10181_10021=API_10181_10021.json()["resourceSets"][0]["resources"][0]["results"][0]["travelDistance"]
Time_10181_10021=API_10181_10021.json()["resourceSets"][0]["resources"][0]["results"][0]["travelDuration"]
#Saving as .csv 
Y={}
ts = int(time.time())
Y["Timestamp"] = ts
Y["Segment_1"]= 1022110181
Y["Time_1"] = Time_10221_10181
Y["Distance_1"] = Distance_10221_10181
Y["Segment_2"]= 1018110152
Y["Time_2"] = Time_10181_10152
Y["Distance_2"] = Distance_10181_10152
Y["Segment_3"]= 1015210181
Y["Time_3"] = Time_10152_10181
Y["Distance_3"] = Distance_10152_10181
Y["Segment_4"]= 1018110021
Y["Time_4"] = Time_10181_10021
Y["Distance_4"] = Distance_10181_10021
filename = "Bing_map_CoronationDrive.csv"
file_exists = os.path.isfile(filename)
with open(filename, "a") as f:  # Just use "w" mode in 3.x
    w = csv.DictWriter(f, Y.keys(), delimiter=",", lineterminator="\n")
    # condition checks if the .csv file exists. In case its true, no need to add the headers on to the existing csv instead just append the information on to the next row.
    if not file_exists:
        w.writeheader()

    w.writerow(Y)

#Milton Road
#API calls 
API_10182_10080=requests.get("https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins=-27.4661776437,153.012619214&destinations=-27.4706772112,152.999830575&travelMode=driving&timeUnit=second&key=AmNLMVwCflw6GxKxfDThujTfsVEkABm1zx6aWyhfBfwJ2o0MMu9VRjjXsSwHrGnn")
API_10080_10128=requests.get("https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins=-27.4706772112,152.999830575&destinations=-27.4785649175,152.989312127&travelMode=driving&timeUnit=second&key=AmNLMVwCflw6GxKxfDThujTfsVEkABm1zx6aWyhfBfwJ2o0MMu9VRjjXsSwHrGnn")
API_10128_10080=requests.get("https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins=-27.4784986653,152.989285786&destinations=-27.4706044855,152.999814321&travelMode=driving&timeUnit=second&key=AmNLMVwCflw6GxKxfDThujTfsVEkABm1zx6aWyhfBfwJ2o0MMu9VRjjXsSwHrGnn")
API_10080_10182=requests.get("https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins=-27.4706044855,152.999814321&destinations=-27.4659986099,153.012601375&travelMode=driving&timeUnit=second&key=AmNLMVwCflw6GxKxfDThujTfsVEkABm1zx6aWyhfBfwJ2o0MMu9VRjjXsSwHrGnn")
#Json extraction 
Distance_10182_10080=API_10182_10080.json()["resourceSets"][0]["resources"][0]["results"][0]["travelDistance"]
Time_10182_10080=API_10182_10080.json()["resourceSets"][0]["resources"][0]["results"][0]["travelDuration"]
Distance_10080_10128=API_10080_10128.json()["resourceSets"][0]["resources"][0]["results"][0]["travelDistance"]
Time_10080_10128=API_10080_10128.json()["resourceSets"][0]["resources"][0]["results"][0]["travelDuration"]
Distance_10128_10080=API_10128_10080.json()["resourceSets"][0]["resources"][0]["results"][0]["travelDistance"]
Time_10128_10080=API_10128_10080.json()["resourceSets"][0]["resources"][0]["results"][0]["travelDuration"]
Distance_10080_10182=API_10080_10182.json()["resourceSets"][0]["resources"][0]["results"][0]["travelDistance"]
Time_10080_10182=API_10080_10182.json()["resourceSets"][0]["resources"][0]["results"][0]["travelDuration"]
#Saving as .csv 
Z={}
ts = int(time.time())
Z["Timestamp"] = ts
Z["Segment_1"]= 1018210080
Z["Time_1"] = Time_10182_10080
Z["Distance_1"] = Distance_10182_10080
Z["Segment_2"]= 1008010128
Z["Time_2"] = Time_10080_10128
Z["Distance_2"] = Distance_10080_10128
Z["Segment_3"]= 1012810080
Z["Time_3"] = Time_10128_10080
Z["Distance_3"] = Distance_10128_10080
Z["Segment_4"]= 1008010182
Z["Time_4"] = Time_10080_10182
Z["Distance_4"] = Distance_10080_10182
filename = "Bing_map_MiltonRoad.csv"
file_exists = os.path.isfile(filename)
with open(filename, "a") as f:  # Just use "w" mode in 3.x
    w = csv.DictWriter(f, Z.keys(), delimiter=",", lineterminator="\n")
    # condition checks if the .csv file exists. In case its true, no need to add the headers on to the existing csv instead just append the information on to the next row.
    if not file_exists:
        w.writeheader()

    w.writerow(Z)
