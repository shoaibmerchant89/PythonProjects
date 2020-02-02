import pickle

friends1 = {"Dan": [20, "London", 32324356], "Maria": [20, "Manchester", 78864823]}
friends2 = {"Dan": [20, "London", 32324356], "Maria": [20, "Manchester", 78864823]}
friends3 = {"Dan": [20, "London", 32324356], "Maria": [20, "Manchester", 78864823]}
friends = (friends1,friends2,friends3)
enemies = 'These are my enemies'


with open('AddDictToFile.dat', 'wb') as f:
    pickle.dump(friends, f)

with open('AddDictToFile.dat', 'rb') as f:
    obj = pickle.load(f)
    print(type(obj))
    print(obj)

print(friends[0])