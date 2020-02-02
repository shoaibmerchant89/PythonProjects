import json

friends1 = {"Dan": [20, "London", 32324356], "Maria": [20, "Manchester", 78864823]}
friends2 = {"Dan": [20, "London", 32324356], "Maria": [20, "Manchester", 78864823]}
friends3 = {"Dan": [20, "London", 32324356], "Maria": [20, "Manchester", 78864823]}
friends = (friends1,friends2,friends3)
enemies = 'These are my enemies'

with open('friends.json', 'w+') as f:
    json.dump(friends1, f, indent=4)

json_string = json.dumps(friends1, indent=2)
print(json_string)