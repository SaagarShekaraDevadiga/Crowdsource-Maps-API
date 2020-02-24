import json
import requests
import csv
import time
import os.path
#Kelvin Grove road 
#API calls 
API_10035_10303 = requests.get("https://api.mapbox.com/directions-matrix/v1/mapbox/driving/153.014583501,-27.4596556832;153.010885566,-27.4511774594?approaches=curb;curb&access_token=pk.eyJ1IjoiY3J5c2l6OTExIiwiYSI6ImNqdHM2dm95czB4bjIzeW0ybThpc3ZkMHYifQ.skuy-zMscBznv01zmZzSfg")
API_10303_10307 = requests.get("https://api.mapbox.com/directions-matrix/v1/mapbox/driving/153.010885566,-27.4511774594;153.007455934,-27.4443529585?approaches=curb;curb&access_token=pk.eyJ1IjoiY3J5c2l6OTExIiwiYSI6ImNqdHM2dm95czB4bjIzeW0ybThpc3ZkMHYifQ.skuy-zMscBznv01zmZzSfg")
API_10307_10303 = requests.get("https://api.mapbox.com/directions-matrix/v1/mapbox/driving/153.007716062,-27.4446214308;153.011021478,-27.4511855477?approaches=curb;curb&access_token=pk.eyJ1IjoiY3J5c2l6OTExIiwiYSI6ImNqdHM2dm95czB4bjIzeW0ybThpc3ZkMHYifQ.skuy-zMscBznv01zmZzSfg")
API_10303_10035 = requests.get("https://api.mapbox.com/directions-matrix/v1/mapbox/driving/153.011021478,-27.4511855477;153.014964537,-27.4598909273?approaches=curb;curb&access_token=pk.eyJ1IjoiY3J5c2l6OTExIiwiYSI6ImNqdHM2dm95czB4bjIzeW0ybThpc3ZkMHYifQ.skuy-zMscBznv01zmZzSfg")
#Json extraction 
Time_10035_10303 = API_10035_10303.json()["durations"][0][1]
Distance_10035_10303 = API_10035_10303.json()["destinations"][1]["distance"]
Time_10303_10307 = API_10303_10307.json()["durations"][0][1]
Distance_10303_10307 = API_10303_10307.json()["destinations"][1]["distance"]
Time_10307_10303 = API_10307_10303.json()["durations"][0][1]
Distance_10307_10303 = API_10307_10303.json()["destinations"][1]["distance"]
Time_10303_10035 = API_10303_10035.json()["durations"][0][1]
Distance_10303_10035 = API_10303_10035.json()["destinations"][1]["distance"]
#Saving traveller information into .csv 
X = {}
ts = int(time.time())
X["Timestamp"] = ts
X["Segment_1"]= 1003510303 
X["Distance_1"] = Distance_10035_10303
X["Time_1"] = Time_10035_10303
X["Segment_2"]= 1030310307 
X["Distance_2"] = Distance_10303_10307 
X["Time_2"] = Time_10303_10307 
X["Segment_3"]= 1030710303 
X["Distance_3"] = Distance_10307_10303 
X["Time_3"] = Time_10307_10303 
X["Segment_4"]= 1030310035
X["Distance_4"] = Distance_10303_10035 
X["Time_4"] = Time_10303_10035 
# saving the dictonary into a csv
filename = "MapBox_map_KelvinGrove.csv"
file_exists = os.path.isfile(filename)
with open(filename, "a") as f:  # Just use "w" mode in 3.x
    w = csv.DictWriter(f, X.keys(), delimiter=",", lineterminator="\n")

    if not file_exists:
        w.writeheader()

    w.writerow(X)
#Milton road 
#API calls 
API_10182_10080 = requests.get("https://api.mapbox.com/directions-matrix/v1/mapbox/driving/153.012619214,-27.4661776437;152.999830575,-27.4706772112?approaches=curb;curb&access_token=pk.eyJ1IjoiY3J5c2l6OTExIiwiYSI6ImNqdHM2dm95czB4bjIzeW0ybThpc3ZkMHYifQ.skuy-zMscBznv01zmZzSfg")
API_10080_10128 = requests.get("https://api.mapbox.com/directions-matrix/v1/mapbox/driving/152.999830575,-27.4706772112;152.989312127,-27.4785649175?approaches=curb;curb&access_token=pk.eyJ1IjoiY3J5c2l6OTExIiwiYSI6ImNqdHM2dm95czB4bjIzeW0ybThpc3ZkMHYifQ.skuy-zMscBznv01zmZzSfg")
API_10128_10080 = requests.get("https://api.mapbox.com/directions-matrix/v1/mapbox/driving/152.989285786,-27.4784986653;152.999814321,-27.4706044855?approaches=curb;curb&access_token=pk.eyJ1IjoiY3J5c2l6OTExIiwiYSI6ImNqdHM2dm95czB4bjIzeW0ybThpc3ZkMHYifQ.skuy-zMscBznv01zmZzSfg")
API_10080_10182 = requests.get("https://api.mapbox.com/directions-matrix/v1/mapbox/driving/152.999814321,-27.4706044855;153.012601375,-27.4659986099?approaches=curb;curb&access_token=pk.eyJ1IjoiY3J5c2l6OTExIiwiYSI6ImNqdHM2dm95czB4bjIzeW0ybThpc3ZkMHYifQ.skuy-zMscBznv01zmZzSfg")
#Json extraction 
Time_10182_10080 = API_10182_10080.json()["durations"][0][1]
Distance_10182_10080 = API_10182_10080.json()["destinations"][1]["distance"]
Time_10080_10128 = API_10080_10128.json()["durations"][0][1]
Distance_10080_10128 = API_10080_10128.json()["destinations"][1]["distance"]
Time_10128_10080 = API_10128_10080.json()["durations"][0][1]
Distance_10128_10080 = API_10128_10080.json()["destinations"][1]["distance"]
Time_10080_10182 = API_10080_10182.json()["durations"][0][1]
Distance_10080_10182 = API_10080_10182.json()["destinations"][1]["distance"]
#Saving traveller information into .csv 
Y = {}
ts = int(time.time())
Y["Timestamp"] = ts
Y["Segment_1"]= 1018210080 
Y["Distance_1"] = Distance_10182_10080
Y["Time_1"] = Time_10182_10080
Y["Segment_2"]= 1008010128
Y["Distance_2"] = Distance_10080_10128 
Y["Time_2"] = Time_10080_10128 
Y["Segment_3"]= 1012810080
Y["Distance_3"] = Distance_10128_10080 
Y["Time_3"] = Time_10128_10080 
Y["Segment_4"]= 1008010182
Y["Distance_4"] = Distance_10080_10182 
Y["Time_4"] = Time_10080_10182 
# saving the dictonary into a csv
filename = "MapBox_map_MiltonRoad.csv"
file_exists = os.path.isfile(filename)
with open(filename, "a") as f:  # Just use "w" mode in 3.x
    w = csv.DictWriter(f, Y.keys(), delimiter=",", lineterminator="\n")

    if not file_exists:
        w.writeheader()

    w.writerow(Y)
#Coronation Drive
#API calls 
API_10221_10181 = requests.get("https://api.mapbox.com/directions-matrix/v1/mapbox/driving/153.010921146,-27.4688091406;152.999575331,-27.4785548882?approaches=curb;curb&access_token=pk.eyJ1IjoiY3J5c2l6OTExIiwiYSI6ImNqdHM2dm95czB4bjIzeW0ybThpc3ZkMHYifQ.skuy-zMscBznv01zmZzSfg")
API_10181_10152 = requests.get("https://api.mapbox.com/directions-matrix/v1/mapbox/driving/152.999575331,-27.4785548882;152.993312789,-27.4860809025?approaches=curb;curb&access_token=pk.eyJ1IjoiY3J5c2l6OTExIiwiYSI6ImNqdHM2dm95czB4bjIzeW0ybThpc3ZkMHYifQ.skuy-zMscBznv01zmZzSfg")
API_10152_10181 = requests.get("https://api.mapbox.com/directions-matrix/v1/mapbox/driving/152.993206339,-27.4859933765;152.999516649,-27.4784860649?approaches=curb;curb&access_token=pk.eyJ1IjoiY3J5c2l6OTExIiwiYSI6ImNqdHM2dm95czB4bjIzeW0ybThpc3ZkMHYifQ.skuy-zMscBznv01zmZzSfg")
API_10181_10021 = requests.get("https://api.mapbox.com/directions-matrix/v1/mapbox/driving/152.999516649,-27.4784860649;153.011057327,-27.4686911369?approaches=curb;curb&access_token=pk.eyJ1IjoiY3J5c2l6OTExIiwiYSI6ImNqdHM2dm95czB4bjIzeW0ybThpc3ZkMHYifQ.skuy-zMscBznv01zmZzSfg")
#Json extraction 
Time_10221_10181 = API_10221_10181.json()["durations"][0][1]
Distance_10221_10181 = API_10221_10181.json()["destinations"][1]["distance"]
Time_10181_10152 = API_10181_10152.json()["durations"][0][1]
Distance_10181_10152 = API_10181_10152.json()["destinations"][1]["distance"]
Time_10152_10181 = API_10152_10181.json()["durations"][0][1]
Distance_10152_10181 = API_10152_10181.json()["destinations"][1]["distance"]
Time_10181_10021 = API_10181_10021.json()["durations"][0][1]
Distance_10181_10021 = API_10181_10021.json()["destinations"][1]["distance"]
#Saving traveller information into .csv 
Y = {}
ts = int(time.time())
Y["Timestamp"] = ts
Y["Segment_1"]= 1022110181
Y["Distance_1"] = Distance_10221_10181
Y["Time_1"] = Time_10221_10181
Y["Segment_2"]= 1018110152
Y["Distance_2"] = Distance_10181_10152 
Y["Time_2"] = Time_10181_10152 
Y["Segment_3"]= 1015210181
Y["Distance_3"] = Distance_10152_10181 
Y["Time_3"] = Time_10152_10181 
Y["Segment_4"]= 1018110021
Y["Distance_4"] = Distance_10181_10021 
Y["Time_4"] = Time_10181_10021 
# saving the dictonary into a csv
filename = "MapBox_map_CoronationDrive.csv"
file_exists = os.path.isfile(filename)
with open(filename, "a") as f:  # Just use "w" mode in 3.x
    w = csv.DictWriter(f, Y.keys(), delimiter=",", lineterminator="\n")

    if not file_exists:
        w.writeheader()

    w.writerow(Y)