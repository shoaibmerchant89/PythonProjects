# Import python library. Use the official python docs documentation for the json library.

import json

friends1 = {"Shoaib": (30, "Pune", 32324356), "Heena": [31, "Kharadi", 78864823]}
friends2 = {"Arzoo": [26, "Mumbai", 32324356], "Rizwan": [38, "Borivali", 78864823]}
friends3 = {"Naaz": [52, "Kalina", 32324356], "Shanu": [58, "Dongri", 78864823]}
friends = (friends1,friends2,friends3)
enemies = 'No enemies'

# json.dump - write and encode dict objects into a json file
with open('friends.json', 'w+') as f:
    json.dump(friends, f, indent=2)


# json.dumps - write and encode dict objects into a json string
json_obj = json.dumps(friends)
print(json_obj)


# json.load - decode and load a json file into a python dict
with open('friends.json') as f:
    fl = json.load(f)
    print(fl)


# json.loads - decode and load a json string into a python dict
fl = json.loads(json_obj)
print(type(fl[0]['Shoaib']))
print(fl[0]['Shoaib'])

# json data structures are not the same as python's. Python's tuple is represented as a array in JSON
print(type(friends[0]['Shoaib']))
print(friends[0]['Shoaib'])
