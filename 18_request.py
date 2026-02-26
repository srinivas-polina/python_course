#Requesting the data from the internet using the  request package.
#how to install the requests package using pip.

#lets create aprogram that gets current data from the internet,instead of creating or own data and using data from local files from our computer.

#we are using the data that is openly avalible is the current people in the space.
#lets create a program that requests the data and then displays the current people in the space.
#when we are finished, if we run run our program,
#it would make an HTTP request or web request to the web server for the website that stores this space data, then the website would respond with the current people in space and our program would print those people to the screen.

#http request is a way forour program to communicate with a web server and request data from it, and then the web server would respond with the data that we requested.
#it was like sending a request to view a certain site like example.com, and then the web server would repond with data that we requested, which is the website itself.
#Some website return raw data, and usally that raw data is returned under the API(Application Programming Interface) for that website.
#for example twitter has a API at api.twitter.com, which allows us to request data from twitter, and then twitter would respond with the data that we requested, which is in form of JSON(JavaScript Object Notation) data, which is a format for storing and exchaning data.
# HTTP request send from our system to twitter API web server
# we get HTTP response from twitter API web server to our system, which contains the data that we requested.

import requests

response =  requests.get("http://api.open-notify.org/astros.json")

json = response.json()

print("The Details of the people currently in the space are: ")
for person in json["people"]:
    print("Craft name: ", person["craft"], ",", "Person Name: ", person["name"])
