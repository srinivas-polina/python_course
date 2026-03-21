#we can presist python objects into binary files.
#why do we need to persist pyhton objects?
# as a developer , it is necessary to serve the internal state of our application to disk, a database, or send details over the network.
#and this is why persisting an object might come in handy.
#we can do this python by using the pickle module.
import pickle

#we are creating aperson class

class Person:
    age = 45
    name = "John Smith"
    kids = ["pete", "Lilly", "kate"]
    employers = {"AWS": 2022, "Microsoft" : 2023, "Yahoo" : 2005}
    shoe_sizes = (10, 11)


#now we are going to use python's picke module to serialize this class and its values and store this in a binary file.
#so to do that lets create serialize function to which we pass an object.
def serialize(obj):
    #this function invokes the pickle.dumps method, which converts the object being passed into binary object using this serialization protocol.
    pickled = pickle.dumps(obj, protocol = pickle.HIGHEST_PROTOCOL)
    print(f'Serialized object: \n{pickled}\n')
    return pickled


#now converting binary object into python object is called deserialization, and we can do that by using th pickle.loads method
def deserialize(obj):
    unpickled = pickle.loads(obj)
    print(f"Deserialized: \n{unpickled}\n")

def deserialize_employee(obj):
    unpickled = pickle.loads(obj)
    print(f"Deserialized employee: \n{unpickled}\n")

#two extra functions,  one is to take a python object and save that to a binary file, and the other is to read a binary file and convert that back to a pyhton object.
def obj_to_file(fn, obj):
    with open(fn, "wb") as pf:
        pickle.dump(obj, pf, protocol = pickle.HIGHEST_PROTOCOL)

def file_to_obj(fn, obj):
    with open(fn, 'rb') as pf:
        obj = pickle.load(pf)
        print(obj)
        return obj

#lets inoke the serialise function
pickled = serialize(Person())
#deserialize the pickled object
deserialize(pickled)
#deserialize the empoyee object
deserialize_employee(pickled)

obj = obj_to_file("./files_to_read/person.bin", Person())
person = file_to_obj("./files_to_read/person.bin", obj)
