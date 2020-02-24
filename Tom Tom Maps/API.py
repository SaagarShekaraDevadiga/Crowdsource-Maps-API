import json
import requests
import csv
import time
import os.path
#The numbers used as variable and the geolocations are w.r.t the BCC sensor ID and the placement of those sensors in the selecetd road network.
#Kelvin Grove road 
#API calls 
API_10035_10303=requests.get("https://api.tomtom.com/routing/1/calculateRoute/-27.4596556832,153.014583501:-27.4511774594,153.010885566/json?avoid=unpavedRoads&key=VBz3oFonbyusBA7QhJgbDRQAwNIJoXSx")
API_10303_10307=requests.get("https://api.tomtom.com/routing/1/calculateRoute/-27.4511774594,153.010885566:-27.4443529585,153.007455934/json?avoid=unpavedRoads&key=VBz3oFonbyusBA7QhJgbDRQAwNIJoXSx")
API_10307_10303=requests.get("https://api.tomtom.com/routing/1/calculateRoute/-27.4446214308,153.007716062:-27.4511855477,153.011021478/json?avoid=unpavedRoads&key=VBz3oFonbyusBA7QhJgbDRQAwNIJoXSx")
API_10303_10035=requests.get("https://api.tomtom.com/routing/1/calculateRoute/-27.4511855477,153.011021478:-27.4598909273,153.014964537/json?avoid=unpavedRoads&key=VBz3oFonbyusBA7QhJgbDRQAwNIJoXSx")
#To check the status of the api call 
X={}
ts = int(time.time())
X["Timestamp"] = ts
X["Segment_1"]= 1003510303 
X["Distance_1"]=API_10035_10303.json()["routes"][0]["summary"]["lengthInMeters"]
X["Travel_Time_1"]=API_10035_10303.json()["routes"][0]["summary"]["travelTimeInSeconds"]
X["Delay_Time_1"]=API_10035_10303.json()["routes"][0]["summary"]["trafficDelayInSeconds"]
X["Segment_2"]= 1030310307 
X["Distance_2"]=API_10303_10307.json()["routes"][0]["summary"]["lengthInMeters"]
X["Travel_Time_2"]=API_10303_10307.json()["routes"][0]["summary"]["travelTimeInSeconds"]
X["Delay_Time_2"]=API_10303_10307.json()["routes"][0]["summary"]["trafficDelayInSeconds"]
X["Segment_3"]= 1030710303 
X["Distance_3"]=API_10307_10303.json()["routes"][0]["summary"]["lengthInMeters"]
X["Travel_Time_3"]=API_10307_10303.json()["routes"][0]["summary"]["travelTimeInSeconds"]
X["Delay_Time_3"]=API_10307_10303.json()["routes"][0]["summary"]["trafficDelayInSeconds"]
X["Segment_4"]= 1030310035 
X["Distance_4"]=API_10303_10035.json()["routes"][0]["summary"]["lengthInMeters"]
X["Travel_Time_4"]=API_10303_10035.json()["routes"][0]["summary"]["travelTimeInSeconds"]
X["Delay_Time_4"]=API_10303_10035.json()["routes"][0]["summary"]["trafficDelayInSeconds"]
# saving the dictonary into a csv
filename = "TomTom_map_KelvinGrove.csv"
file_exists = os.path.isfile(filename)
with open(filename, "a") as f:  # Just use "w" mode in 3.x
    w = csv.DictWriter(f, X.keys(), delimiter=",", lineterminator="\n")
    # condition checks if the .csv file exists. In case its true, no need to add the headers on to the existing csv instead just append the information on to the next row.
    if not file_exists:
        w.writeheader()

    w.writerow((X))
#Milton Road  
#API calls 
API_10182_10080=requests.get("https://api.tomtom.com/routing/1/calculateRoute/-27.4661776437,153.012619214:-27.4706772112,152.999830575/json?avoid=unpavedRoads&key=VBz3oFonbyusBA7QhJgbDRQAwNIJoXSx")
API_10080_10128=requests.get("https://api.tomtom.com/routing/1/calculateRoute/-27.4706772112,152.999830575:-27.4785649175,152.989312127/json?avoid=unpavedRoads&key=VBz3oFonbyusBA7QhJgbDRQAwNIJoXSx")
API_10128_10080=requests.get("https://api.tomtom.com/routing/1/calculateRoute/-27.4784986653,152.989285786:-27.4706044855,152.999814321/json?avoid=unpavedRoads&key=VBz3oFonbyusBA7QhJgbDRQAwNIJoXSx")
API_10080_10182=requests.get("https://api.tomtom.com/routing/1/calculateRoute/-27.4706044855,152.999814321:-27.4659986099,153.012601375/json?avoid=unpavedRoads&key=VBz3oFonbyusBA7QhJgbDRQAwNIJoXSx")
#To check the status of the api call 
Y={}
ts = int(time.time())
Y["Timestamp"] = ts
Y["Segment_1"]= 1018210080
Y["Distance_1"]=API_10182_10080.json()["routes"][0]["summary"]["lengthInMeters"]
Y["Travel_Time_1"]=API_10182_10080.json()["routes"][0]["summary"]["travelTimeInSeconds"]
Y["Delay_Time_1"]=API_10182_10080.json()["routes"][0]["summary"]["trafficDelayInSeconds"]
Y["Segment_2"]= 1008010128
Y["Distance_2"]=API_10080_10128.json()["routes"][0]["summary"]["lengthInMeters"]
Y["Travel_Time_2"]=API_10080_10128.json()["routes"][0]["summary"]["travelTimeInSeconds"]
Y["Delay_Time_2"]=API_10080_10128.json()["routes"][0]["summary"]["trafficDelayInSeconds"]
Y["Segment_3"]= 1012810080 
Y["Distance_3"]=API_10128_10080.json()["routes"][0]["summary"]["lengthInMeters"]
Y["Travel_Time_3"]=API_10128_10080.json()["routes"][0]["summary"]["travelTimeInSeconds"]
Y["Delay_Time_3"]=API_10128_10080.json()["routes"][0]["summary"]["trafficDelayInSeconds"]
Y["Segment_4"]= 1008010182 
Y["Distance_4"]=API_10080_10182.json()["routes"][0]["summary"]["lengthInMeters"]
Y["Travel_Time_4"]=API_10080_10182.json()["routes"][0]["summary"]["travelTimeInSeconds"]
Y["Delay_Time_4"]=API_10080_10182.json()["routes"][0]["summary"]["trafficDelayInSeconds"]
# saving the dictonary into a csv
filename = "TomTom_map_MiltonRoad.csv"
file_exists = os.path.isfile(filename)
with open(filename, "a") as f:  # Just use "w" mode in 3.x
    w = csv.DictWriter(f, Y.keys(), delimiter=",", lineterminator="\n")
    # condition checks if the .csv file exists. In case its true, no need to add the headers on to the existing csv instead just append the information on to the next row.
    if not file_exists:
        w.writeheader()

    w.writerow((Y))

#Coronation Drive:
#API calls 
API_10221_10181=requests.get("https://api.tomtom.com/routing/1/calculateRoute/-27.4688091406,153.010921146:-27.4785548882,152.999575331/json?avoid=unpavedRoads&key=VBz3oFonbyusBA7QhJgbDRQAwNIJoXSx")
API_10181_10152=requests.get("https://api.tomtom.com/routing/1/calculateRoute/-27.4785548882,152.999575331:-27.4860809025,152.993312789/json?avoid=unpavedRoads&key=VBz3oFonbyusBA7QhJgbDRQAwNIJoXSx")
API_10152_10181=requests.get("https://api.tomtom.com/routing/1/calculateRoute/-27.4859933765,152.993206339:-27.4784860649,152.999516649/json?avoid=unpavedRoads&key=VBz3oFonbyusBA7QhJgbDRQAwNIJoXSx")
API_10181_10021=requests.get("https://api.tomtom.com/routing/1/calculateRoute/-27.4784860649,152.999516649:-27.4686911369,153.011057327/json?avoid=unpavedRoads&key=VBz3oFonbyusBA7QhJgbDRQAwNIJoXSx")
#To check the status of the api call 
Z={}
ts = int(time.time())
Z["Timestamp"] = ts
Z["Segment_1"]= 1022110181
Z["Distance_1"]=API_10221_10181.json()["routes"][0]["summary"]["lengthInMeters"]
Z["Travel_Time_1"]=API_10221_10181.json()["routes"][0]["summary"]["travelTimeInSeconds"]
Z["Delay_Time_1"]=API_10221_10181.json()["routes"][0]["summary"]["trafficDelayInSeconds"]
Z["Segment_2"]= 1018110152
Z["Distance_2"]=API_10181_10152.json()["routes"][0]["summary"]["lengthInMeters"]
Z["Travel_Time_2"]=API_10181_10152.json()["routes"][0]["summary"]["travelTimeInSeconds"]
Z["Delay_Time_2"]=API_10181_10152.json()["routes"][0]["summary"]["trafficDelayInSeconds"]
Z["Segment_3"]= 1015210181
Z["Distance_3"]=API_10152_10181.json()["routes"][0]["summary"]["lengthInMeters"]
Z["Travel_Time_3"]=API_10152_10181.json()["routes"][0]["summary"]["travelTimeInSeconds"]
Z["Delay_Time_3"]=API_10152_10181.json()["routes"][0]["summary"]["trafficDelayInSeconds"]
Z["Segment_4"]= 1018110021
Z["Distance_4"]=API_10181_10021.json()["routes"][0]["summary"]["lengthInMeters"]
Z["Travel_Time_4"]=API_10181_10021.json()["routes"][0]["summary"]["travelTimeInSeconds"]
Z["Delay_Time_4"]=API_10181_10021.json()["routes"][0]["summary"]["trafficDelayInSeconds"]
# saving the dictonary into a csv
filename = "TomTom_map_CoronationDrive.csv"
file_exists = os.path.isfile(filename)
with open(filename, "a") as f:  # Just use "w" mode in 3.x
    w = csv.DictWriter(f, Z.keys(), delimiter=",", lineterminator="\n")
    # condition checks if the .csv file exists. In case its true, no need to add the headers on to the existing csv instead just append the information on to the next row.
    if not file_exists:
        w.writeheader()

    w.writerow((Z)) 