import json
import pickle

#Serialization using JSON
data = {"name":"john", "age":30}


json_serialized = json.dumps(data)
print(json_serialized)

#Deserialization using JSON
json_deserialized = json.loads(json_serialized)
print(json_deserialized)

#Serialization using Pickle
pickle_serialized = pickle.dumps(data)
print(pickle_serialized)

#Deserialization using Pickle
pickle_deserialized = pickle.loads(pickle_serialized)
print(pickle_deserialized)