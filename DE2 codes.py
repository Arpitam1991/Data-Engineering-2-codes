##Code for API call
import requests

#Calling the API-test
r = requests.get("https://creativecommons.tankerkoenig.de/json/detail.php?id=00060545-18e2-4444-8888-acdc00000001&apikey=65a76f69-ef34-db20-b016-0c88e60c742d")

print(r.json())

#Dataset for details of stations
import pandas as pd
dataset= pd.read_csv(r"C:\\Users\\Arpita\\Downloads\\2022-12-15-stations-num.csv")
print(dataset.head())

uuid_list = dataset['uuid']
print(uuid_list)

#Call for price API
price = requests.get("https://creativecommons.tankerkoenig.de/json/prices.php?ids=00060545-18e2-4444-8888-acdc00000001,44444444-4444-4444-4444-444444444444&apikey=65a76f69-ef34-db20-b016-0c88e60c742d")

print(price.json())

#Iterating through station ids
for i in range (0, 5):
    temp_uuid = "https://creativecommons.tankerkoenig.de/json/detail.php?id="+uuid_list[i]+"&apikey=65a76f69-ef34-db20-b016-0c88e60c742d"
    detail = requests.get(temp_uuid)
    data = detail.json()
detail = requests.get("https://creativecommons.tankerkoenig.de/json/detail.php?id=4429a7d9-fb2d-4c29-8cfe-2ca90323f9f8&apikey=65a76f69-ef34-db20-b016-0c88e60c742d")

print(detail.json())

import json
#with open('detail.json') as f:
#    data = json.load(f)
with open('new_file.json', 'w') as f:
    json.dump(data, f, indent=2)
    print("New json file is created from data.json file")