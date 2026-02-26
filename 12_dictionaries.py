# A dictionary maps keys to values.

acronyms = {
    "LOL" : "Laugh Out Loud",
    "IDK" : "I don't Know",
    "TBH" : "To Be Hones"
}

# variable = {Key : Value}
#each item in the dictionary is known as a "key-value pair"

print(acronyms["LOL"])

#dictionaries can hold anything we want, including other dictionaries
#we can create a dictionary by frist creating an empty list
acronymss = {}
#and then we can add key-value pair items to the dictionary by using square brackets and the assignment operator
acronymss["LOL"] = "Laug Out Loud"
acronymss["IDK"] = "I don't Know"
acronymss["TBH"] = "To Be Honest"
print(acronymss)
#updating
acronymss["TBH"] = "Honestly"

print(acronymss)

#deleting a value from the dictionary
del acronymss["LOL"]
print(acronymss)

#if we try to access a key that is not in the dictionary, we will get a KeyError
#print(acronymss["BTW"])


#to avoid this we can use the get method of the dictionary, which will return None if the key is not in the dictionary instead of raising an error and breaking the program.
#None means absence of the value
print(acronymss.get("BTW"))

#
acronyms = {"LOL": "Laugh Out Loud", "IDK": "I don't Know", "TBH": "To Be Honest"}
definition = acronyms.get("BTW")

if definition:
    print(definition)
else:
    print("Key not found in the dictionary")


#creating sentences
acronyms = {"LOL": "Laugh Out Loud", "IDK": "I don't Know", "TBH": "To Be Honest"}
sentence = "IDK" + " what to do " + "TBH"
definition = acronyms.get("IDK") + " What to do " + acronyms.get("TBH")
print("Sentence:" , sentence)
print("Definition:",definition)